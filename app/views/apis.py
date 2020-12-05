from flask import Blueprint, redirect, render_template
from flask import (
    request,
    url_for,
    flash,
    send_from_directory,
    jsonify,
    render_template_string,
    make_response,
    abort,
)
from flask_user import current_user, login_required, roles_accepted

from app import db
from app.models.nba_models import Person, PersonSchema
import uuid, json, os
import datetime

# When using a Flask app factory we must use a blueprint to avoid needing 'app' for '@app.route'
api_blueprint = Blueprint("api", __name__, template_folder="templates")


@api_blueprint.route("/nbadata", methods=["GET"])
def nbadata():

    ret = {"sample return": 10}
    return (jsonify(ret), 200)
