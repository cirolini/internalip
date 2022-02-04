# -*- coding: utf-8 -*-
"""
This application is an API to consult if an IP is from our organization.
You can use this aplication to get a list of uor IPs,
check if an IP is part of the list, or add and remove IPs from de list.

We use a Redis with database to store this data. We use Redis Sets,
they are an unordered collection of Strings, with have the desirable property of
not allowing repeated members.
"""
from flask import Flask, g
from flask import jsonify

def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)

    @app.route("/health")
    def health(): #pylint: disable=unused-variable
        """Route for health checks"""
        return jsonify({"status": "ok"})

    from . import db
    db.init_app(app)

    from . import api
    app.register_blueprint(api.BP)

    return app
