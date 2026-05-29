# Where we put our HTTP routes
from flask import Blueprint, request, redirect, render_template
from .models import Url
from .utilities import generate_code
from app import db
from mechanize import Browser

# Create Browser instance
br = Browser()


# allows us to split into multiple route files
main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    # Fetch previous URLs from DB
    # If no results become false to display msg front-end
    history = Url.query.all() or False
    return render_template("index.html", history = history)

# generates a shortened code saves it to the database and returns short URL and result page
@main.route("/create", methods=["POST"])
def create():
    long_url = request.form.get("url")

    # Get the title of the page
    br.open(long_url)
    page_title = br.title()
    br.close()

    code = generate_code()
    new = Url(short_code=code, long_url=long_url, page_title=page_title)
    db.session.add(new)
    db.session.commit()

    short_url = f"http://localhost:5000/{code}"
    return render_template("result.html", short_url=short_url)




# Matches shortened code and looks it in the database, redirect user to long url
@main.route("/<code>")
def redirect_url(code):
    url = Url.query.filter_by(short_code=code).first_or_404()
    return redirect(url.long_url)

