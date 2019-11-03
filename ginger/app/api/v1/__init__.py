from flask import Blueprint
from app.api.v1 import book
from app.api.v1 import user


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1