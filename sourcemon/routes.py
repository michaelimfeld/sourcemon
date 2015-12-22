# -*- coding: utf-8 -*-
"""
    Holds handler functions for web api routes
"""

import os
import json
from valve.source.a2s import NoResponseError, ServerQuerier
from valve.source.messages import BrokenMessageError
from flask import Blueprint, send_from_directory, request

from sourcemon.model.servermodel import ServerModel
from sourcemon.model.ipmodel import IPModel

api = Blueprint("api", __name__)

STATIC_PATH = "/var/www/sourcemon"

@api.route("/", methods=["GET"])
def index():
    """
        Returns static index.html
    """
    path = os.path.join(STATIC_PATH, "templates")
    return send_from_directory(path, "index.html")

@api.route("/api/servers", methods=["GET"])
def servers():
    """
        Returns a list of sourcemod servers
    """
    data = []
    for server in ServerModel.select().join(IPModel):
        server_address = (server.ip.address, server.port)

        online = True
        try:
            querier = ServerQuerier(server_address, 1)
            info = querier.get_info()
        except NoResponseError:
            online = False

        server_data = {
            "id": server.id,
            "ip_addr": server.ip.address,
            "port": server.port,
            "online": online
        }
        if online:
            for key in info:
                server_data[key] = str(info[key])

        data.append(server_data)
    return json.dumps(data)

@api.route("/api/server/add", methods=["POST"])
def add_server():
    """
        Adds a server to database if not exists
    """
    data = json.loads(request.data)
    ip_addr = IPModel.get_or_create(address=data["ip_addr"])[0]
    ServerModel.create(ip=ip_addr, port=data["port"])
    return 'OK'

@api.route("/api/server/remove/<server_id>", methods=["POST"])
def remove_server(server_id):
    """
        Removes a server from the database
    """
    ServerModel.delete().where(ServerModel.id == server_id).execute()
    return 'OK'

@api.route("/api/server/<server_id>", methods=["GET"])
def server(server_id):
    """
        Returns a list of sourcemod servers
    """
    data = {}
    db_server = ServerModel.select().join(IPModel)
    db_server = db_server.where(ServerModel.id == server_id).get()
    server_address = (db_server.ip.address, db_server.port)

    info = {}
    try:
        querier = ServerQuerier(server_address, 1)
        info = querier.get_info()
    except NoResponseError:
        pass

    players = []
    try:
        players = querier.get_players()["players"]
    except BrokenMessageError:
        pass
    except NoResponseError:
        pass

    data["id"] = db_server.id
    for key in info:
        data[key] = str(info[key])

    data["players"] = []
    for player in players:
        player_data = {}
        for key in player:
            if type(player[key]) == str:
                player_data[key] = player[key].encode('utf8')
                continue
            player_data[key] = player[key]

        data["players"].append(player_data)

    return json.dumps(data)
