from .extensions import db


class ExampleRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<ExampleRecord {self.title}>"

class Members(db.Model):
    __tablename__ = "members"

    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    membership_level = db.Column(db.String(30), nullable=False)
    join_date = db.Column(db.Date, nullable=False)
    created_date = db.Column(db.Date, nullable=False)


class Trainers(db.Model):
    __tablename__ = "trainers"

    trainer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    join_date = db.Column(db.Date, nullable=False)
    created_date = db.Column(db.Date, nullable=False)

