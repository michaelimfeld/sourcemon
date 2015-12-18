"""
    Database model for IP address
"""
from peewee import CharField
from sourcemon.model.basemodel import BaseModel

class IPModel(BaseModel):
    """
        Database model for IP address
    """
    address = CharField()
