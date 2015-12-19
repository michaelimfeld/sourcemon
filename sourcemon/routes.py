# -*- coding: utf-8 -*-
"""
    Holds handler functions for web api routes
"""

import json
import valve.source.a2s
from flask import Blueprint, send_from_directory, request
from sourcemon.model.servermodel import ServerModel
from sourcemon.model.ipmodel import IPModel

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def index():
    """
        Returns static index.html
    """
    return send_from_directory("templates", "index.html")


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
            querier = valve.source.a2s.ServerQuerier(server_address, 1)
            info = querier.get_info()
        except valve.source.a2s.NoResponseError:
            online = False

        server_data = {
            "ip_addr": server.ip.address,
            "port": server.port,
            "online": online
        }
        if online:
            for key in info:
                server_data[key] = str(info[key])

        data.append(server_data)
    return json.dumps(data)

@api.route("/api/servers", methods=["POST"])
def addserver():
    """
        Adds a server to database if not exists
    """
    data = json.loads(request.data)
    ip_addr = IPModel.create(address=data["ip_addr"])
    ServerModel.create(ip=ip_addr, port=data["port"])
    return 'OK'
