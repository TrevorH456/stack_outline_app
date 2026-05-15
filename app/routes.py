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
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    email = request.form["email"].strip()
    membership_level = request.form["membership_level"].strip()

    if first_name == "" or last_name == "" or email == "" or membership_level == "":
        return "Error: Required fields cannot be empty."
    if "@" not in email:
        return "Error: Invalid email address."
    if membership_level not in ["Basic", "Pro", "Elite"]:
        return "Error: Membership level must be Basic, Pro, or Elite."

    new_member = Members(
        member_id=request.form["member_id"],
        first_name=first_name,
        last_name=last_name,
        email=email,
        membership_level=membership_level,
        join_date=datetime.strptime(request.form["join_date"], "%Y-%m-%d").date(),
        created_date=datetime.today().date()
    )
    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/add_trainer", methods=["POST"])
def add_trainer():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    email = request.form["email"].strip()

    if first_name == "" or last_name == "" or email == "":
        return "Error: Required fields cannot be empty."
    if "@" not in email:
        return "Error: Invalid email address."

    new_trainer = Trainers(
        trainer_id=request.form["trainer_id"],
        first_name=first_name,
        last_name=last_name,
        email=email,
        join_date=datetime.strptime(request.form["join_date"], "%Y-%m-%d").date(),
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



@main.route("/edit_member/<int:member_id>", methods=["GET", "POST"])
def edit_member(member_id):
    member = Members.query.get_or_404(member_id)

    if request.method == "POST":
        first_name = request.form["first_name"].strip()
        last_name = request.form["last_name"].strip()
        email = request.form["email"].strip()
        membership_level = request.form["membership_level"].strip()

        if first_name == "" or last_name == "" or email == "" or membership_level == "":
            return "Error: Required fields cannot be empty."
        if "@" not in email:
            return "Error: Invalid email address."
        if membership_level not in ["Basic", "Pro", "Elite"]:
            return "Error: Membership level must be Basic, Pro, or Elite."

        member.first_name = first_name
        member.last_name = last_name
        member.email = email
        member.membership_level = membership_level
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("edit_member.html", member=member)

@main.route("/edit_trainer/<int:trainer_id>", methods=["GET", "POST"])
def edit_trainer(trainer_id):
    trainer = Trainers.query.get_or_404(trainer_id)

    if request.method == "POST":
        first_name = request.form["first_name"].strip()
        last_name = request.form["last_name"].strip()
        email = request.form["email"].strip()
        if first_name == "" or last_name == "" or email == "":
            return "Error: Required fields cannot be empty."
        if "@" not in email:
            return "Error: Invalid email address."

        trainer.first_name = first_name
        trainer.last_name = last_name
        trainer.email = email
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("edit_trainer.html", trainer=trainer)