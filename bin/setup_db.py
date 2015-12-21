#!/usr/bin/python
"""
    setup database script
"""
from sourcemon.model.basemodel import BaseModel
from sourcemon.model.ipmodel import IPModel
from sourcemon.model.servermodel import ServerModel


def main():
    """
        create database tables
    """
    database = BaseModel().database()
    database .connect()
    database.create_tables([IPModel, ServerModel])

if __name__ == "__main__":
    main()
