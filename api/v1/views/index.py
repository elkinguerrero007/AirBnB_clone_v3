#!/usr/bin/python3
""" index file to shoe responses of request """
from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ status view function """
    return jsonify({"status": "OK"})
