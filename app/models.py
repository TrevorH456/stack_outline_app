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


class Classes(db.Model):
    __tablename__ = "classes"

    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    class_date = db.Column(db.Date, nullable=False)
    class_time = db.Column(db.Time, nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainers.trainer_id"), nullable=False)
    created_date = db.Column(db.Date, nullable=False)


class Registration(db.Model):
    __tablename__ = "registration"

    registration_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.class_id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.member_id"), nullable=False)
    registration_date = db.Column(db.Date, nullable=False)
    created_date = db.Column(db.Date, nullable=False)

    __table_args__ = (
        db.UniqueConstraint("class_id", "member_id", name="unique_member_class_registration"),
    )