from flaskext.mysql import MySQL


class Singleton(type):
    """Singleton metaclass"""

    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MysqlUtil(object):
    # Make this class of metaclass Singleton
    __metaclass__ = Singleton

    def __init__(self, app):
        """Initialize the instance
        Args:
            app: the app object import from 'app' library
        """
        mysql = MySQL()

        # Members variables initialization
        self.mysql = mysql
        self.data = {}
        self.password = {
            'user': 'l74z3oC1=1V>5J7',
            'developer': 'nvSEXvXXUU9E2QFu',
        }

        self.app = app

        # MySQL configurations
        app.config['MYSQL_DATABASE_HOST'] = '54.186.181.45'
        app.config['MYSQL_DATABASE_PORT'] = 3306

        self.use_account('user')
        self.use_database('SEDB')

        mysql.init_app(app)


    def use_account(self, username = 'user'):
        """Specify the user to login
        Args:
            dbName (string): name of the user to use, default as 'user'
        Returns:
            -1: if the username not found in the lookup dictionary
        """
        if username not in self.password.keys():
            print ("Invalid Username")
            username = 'user'
        self.app.config['MYSQL_DATABASE_USER'] = username
        self.app.config['MYSQL_DATABASE_PASSWORD'] = self.password[username]


    def use_database(self, dbName = 'SEDB'):
        """Specify the database to use
        Args:
            dbName (string): name of the database to use, default as 'SEDB'
        """
        self.app.config['MYSQL_DATABASE_DB'] = dbName


    def insert_push(self, field_name, record_value):
        """Add pair of key and value for one cell
        Args:
            field_name (string): filed name in database
            record_value (string): instance value of the field
        """
        self.data[field_name] = record_value


    def batch_insert_push(self, batch_data):
        """Insert all the pairs in a batch
        Args:
            batch_data (dict): a dictionary of all the key(db field) and value(record value) pairs
        """
        data = self.data
        for key, value in batch_data.items():
            data[key] = value


    def insert_execute(self, table_name):
        """Concatenate to get a query string and execute the inserting
        Args:
            table_name (string): name of the table to be inserted into:
        Raises:
            Error: raise error if creating new cursor fails
        """
        keys, values = zip(*self.data.items())
        query = "INSERT INTO `" + table_name + "`"
        query += " (`" + "`,`".join(keys) + "`) "
        query += "VALUES (" + ("%s," * len(keys))[:-1] + ");"

        connection = self.mysql.connect()

        insert_id = 0
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                insert_id = cursor.lastrowid
            connection.commit()

        finally:
            connection.close()

        return insert_id


    def select_all(self, query):
        connection = self.mysql.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                data = cursor.fetchall()
                return data
        finally:
            connection.close()


    def select_one(self, query):
        connection = self.mysql.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                data = cursor.fetchone()
                return data
        finally:
            connection.close()


    def clear(self):
        """Clear the pushed data"""
        self.data = {}


# """ Example """
# from app import app
# sql = MysqlUtil(app)
# sql.insert_push('name', 'peizhe2')
# sql.insert_push('gender', 'male')
# sql.insert_execute("student")
# sql.clear()
