from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .extensions import db

from .models import (
    Members,
    Trainers
)
main = Blueprint("main", __name__)

@main.route("/")
def index():
    members = Members.query.all()
    trainers = Trainers.query.all()
    return render_template(
        "index.html",
        members=members,
        trainers=trainers
    )

@main.route("/add_member", methods=["POST"])
def add_member():
    new_member = Members(
        member_id=request.form["member_id"],
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        email=request.form["email"],
        membership_level=request.form["membership_level"],
        join_date=datetime.strptime(
            request.form["join_date"],
            "%Y-%m-%d"
        ).date(),
        created_date=datetime.today().date()
    )
    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/add_trainer", methods=["POST"])
def add_trainer():
    new_trainer = Trainers(
        trainer_id=request.form["trainer_id"],
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        email=request.form["email"],
        join_date=datetime.strptime(
            request.form["join_date"],
            "%Y-%m-%d"
        ).date(),
        created_date=datetime.today().date()
    )
    db.session.add(new_trainer)
    db.session.commit()
    return redirect(url_for("main.index"))



@main.route("/delete_member/<int:member_id>")
def delete_member(member_id):
    member = Members.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/delete_trainer/<int:trainer_id>")
def delete_trainer(trainer_id):
    trainer = Trainers.query.get_or_404(trainer_id)
    db.session.delete(trainer)
    db.session.commit()
    return redirect(url_for("main.index"))


