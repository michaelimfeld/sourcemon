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

        querier = valve.source.a2s.ServerQuerier(server_address)
        info = querier.get_info()

        server_data = {
            "ip_addr": server.ip.address,
            "port": server.port
        }
        for key in info:
            server_data[key] = str(info[key])

        data.append(server_data)
    return json.dumps(data)
