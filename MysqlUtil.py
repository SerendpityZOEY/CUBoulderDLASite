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

        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'l74z3oC1=1V>5J7'
        app.config['MYSQL_DATABASE_DB'] = 'SEDB'
        app.config['MYSQL_DATABASE_HOST'] = '54.186.181.45'
        app.config['MYSQL_DATABASE_PORT'] = 3306
        mysql.init_app(app)

        # Members variables initialization
        self.mysql = mysql
        self.data = {}

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
