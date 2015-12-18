"""
    BaseModel for database models
"""
from peewee import Model, SqliteDatabase


DATABASE = SqliteDatabase('/var/sourcemon/sourcemon.db')

class BaseModel(Model):
    """
        BaseModel for database models
    """
    def database(self):
        """
            Returns database connection
        """
        return DATABASE

    class Meta:
        """
            Meta
        """
        database = DATABASE
