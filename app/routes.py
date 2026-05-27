# Where we put our HTTP routes
from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Test"
