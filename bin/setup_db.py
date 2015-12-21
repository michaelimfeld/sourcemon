#!/usr/bin/python
"""
    setup database script
"""
from sourcemon.model.basemodel import BaseModel
from sourcemon.model.ipmodel import IPModel
from sourcemon.model.servermodel import ServerModel

TABLES = [
    IPModel,
    ServerModel
]


def main():
    """
        create database tables
    """
    database = BaseModel().database()
    database.connect()
    database.create_tables(TABLES, safe=True)

if __name__ == "__main__":
    main()
