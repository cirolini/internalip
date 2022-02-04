# -*- coding: utf-8 -*-
"""Functions to establish a redis db connection"""
import os
import redis
import click

from flask import g
from flask.cli import with_appcontext

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.

    Enviroment:
        Get enviroment variable to connect redis
        REDIS_HOST
        REDIS_PORT
        REDIS_DB

    Return:
        conection object to global
    """
    if 'db' not in g:
        g.db = redis.StrictRedis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=os.getenv("REDIS_PORT", "6379"),
            db=os.getenv("REDIS_DB", "0")
        )

    return g.db

def init_db():
    """import data from text file."""

    with open('./internalip/internal_ip.txt', 'r') as data:
        for ipaddress in data.read().strip().split("\n"):
            click.echo('Cadastrando IP: %s.' % ipaddress)
            get_db().sadd('internalip', ipaddress)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data and import data."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.cli.add_command(init_db_command)
