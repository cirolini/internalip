# -*- coding: utf-8 -*-
"""This file contain all routes to manipulate and list the internal IPs"""
import ipaddress
from functools import wraps
import iptools
from flask import Blueprint, jsonify, request
from internalip.db import get_db

# Create bluepint in default route
BP = Blueprint('api', __name__, url_prefix='/')

def valid_ip(f):
    """Decorator to check if the ip is validself.

    Args:
        ip (str): valid IP address.
    Except:
        return json: IP is not valid.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """Decorator function. Recive args e kwargs"""
        if kwargs.get('ipaddr') is not None:
            ipaddr = kwargs.get('ipaddr')
        if request.values.get('ipaddr') is not None:
            ipaddr = request.values['ipaddr']

        if 'ipaddr' not in locals():
            return jsonify({"error": "You need specify an IP address."}), 500

        try:
            ipaddress.ip_interface(ipaddr)
        except ValueError:
            return jsonify({"error": "is not a valid IP"}), 500
        return f(*args, **kwargs)
    return decorated_function

@BP.route('/add_ip/', methods=['POST'])
@valid_ip
def add_ip():
    """Route to add new IP to internal list

    Args:
        ipaddr (str): valid IP address.
    """

    try:
        get_db().sadd('internalip', request.values['ipaddr'])
        return jsonify({"action": "success"})
    except Exception:
        return jsonify({"action": "database error"}), 500

@BP.route('/remove_ip/', methods=['POST'])
@valid_ip
def remove_ip():
    """Route to remove IP to internal list

    Args:
        ipaddr (str): valid IP address.
    """
    try:
        get_db().srem('internalip', request.values['ipaddr'])
        return jsonify({"action": "success"})
    except Exception:
        return jsonify({"action": "database error"}), 500

@BP.route('/list_all_internal')
def list_all_internal():
    """Route to list all interal IPs

    Return:
        json: with a list of all internal IPs
    """
    return jsonify(list(get_db().smembers('internalip')))

@BP.route('/is_internal/<ipaddr>')
@valid_ip
def is_internal(ipaddr):
    """Route if a ip has part list all interal IPs

    Args:
        ipaddr (str): valid IP address.

    Return:
        json: True if successful, False otherwise.
    """
    internal_ips = iptools.IpRangeList(*list(get_db().smembers('internalip')))

    if ipaddr in internal_ips:
        return jsonify({"internal": "True"})
    return jsonify({"internal": "False"})
