"""
    Database model for sourcemod server
"""
from peewee import IntegerField, ForeignKeyField
from sourcemon.model.basemodel import BaseModel
from sourcemon.model.ipmodel import IPModel

class ServerModel(BaseModel):
    """
        Database model for sourcemod server
    """
    ip = ForeignKeyField(IPModel)
    port = IntegerField()
