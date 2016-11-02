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
        mysql = MySQL()

        self.password = {
            'user': 'l74z3oC1=1V>5J7',
            'developer': 'nvSEXvXXUU9E2QFu',
        }

        self.app = app

        # MySQL configurations
<<<<<<< HEAD
=======
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'l74z3oC1=1V>5J7'
        app.config['MYSQL_DATABASE_DB'] = 'SEDB'
>>>>>>> 4de2fec536772231ee693147d55fc3a0b68bfff5
        app.config['MYSQL_DATABASE_HOST'] = '54.186.181.45'
        app.config['MYSQL_DATABASE_PORT'] = 3306

        self.use_account()
        self.use_database()

        mysql.init_app(app)

        # Members variables initialization
        self.mysql = mysql
        self.data = {}


    def use_account(self, username = 'user'):
        if username not in self.password.keys():
            print "Invalid Username"
            username = 'user'
        self.app.config['MYSQL_DATABASE_USER'] = username
        self.app.config['MYSQL_DATABASE_PASSWORD'] = self.password[username]

    def use_database(self, dbName = 'SEDB'):
        self.app.config['MYSQL_DATABASE_DB'] = dbName


    def insert_push(self, field_name, record_value):
        """Add pair of key and value for one cell

        Args:
            field_name (string): filed name in database
            record_value (string): instance value of the field

        """
        self.data[field_name] = record_value

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

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
            connection.commit()

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
