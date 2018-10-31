from . import auth
from flask import jsonify
from flask_login import login_user, logout_user, login_required
from ..models import Person, Organization
from .. import wallet_client


@auth.route("/person/register", methods=["GET", "POST"])
def person_register(task):
    task["type"] = "Person"
    _, resp = wallet_client.register({"Bc-Invoke-Mode": "sync"}, task)
    return resp


@auth.route("/organization/register", methods=["GET", "POST"])
def organization_register(task):
    task["type"] = "Organization"
    _, resp = wallet_client.register({"Bc-Invoke-Mode": "sync"}, task)
    return resp


@auth.route("/person/login", methods=["GET", "POST"])
def person_login(task):
    pass


@auth.route("/organization/login", methods=["GET", "POST"])
def organization_login(task):
    pass


@auth.route("/person/logout")
@login_required
def person_logout():
    pass


@auth.route("/organization/logout")
@login_required
def organization_logout():
    pass