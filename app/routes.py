from flask import Blueprint, render_template

from .models import (
    Members,
    Trainers,
    Classes,
    Registration
)
main = Blueprint("main", __name__)

@main.route("/")
def index():
    members = Members.query.all()
    trainers = Trainers.query.all()
    classes = Classes.query.all()
    registrations = Registration.query.all()
    return render_template(
        "index.html",
        members=members,
        trainers=trainers,
        classes=classes,
        registrations=registrations
    )
