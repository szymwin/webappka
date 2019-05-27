from datetime import datetime
from .. import db


class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    age = db.Column(db.Integer)
    home = db.Column(db.String)
    gender = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    education = db.Column(db.Integer)
    faith = db.Column(db.Integer)
    friends = db.Column(db.Integer)
    family = db.Column(db.Integer)
    view = db.Column(db.Integer)
    openminded = db.Column(db.Integer)
    support = db.Column(db.Integer)
    manifest = db.Column(db.Integer)
    partnership = db.Column(db.Integer)
    kids = db.Column(db.Integer)
    status = db.Column(db.Integer)

    def __init__(self, age, home, gender, sex, education, faith, friends, family, view, openminded, support, manifest,
                 partnership, kids, status):
        self.age = age
        self.home = home
        self.gender = gender
        self.sex = sex
        self.education = education
        self.faith = faith
        self.friends = friends
        self.family = family
        self.view = view
        self.openminded = openminded
        self.support = support
        self.manifest = manifest
        self.partnership = partnership
        self.kids = kids
        self.status = status


    @staticmethod
    def generate_fake(count=100):
        """Generate a number of fake users for testing."""
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice
        from faker import Faker

        fake = Faker()
        seed()

        for i in range(count):
            f = Formdata(
                firstname=fake.first_name(),
                email=fake.email(),
                age=(fake.pyint() % 99)+1,
                income=fake.pyint(),
                satisfaction=fake.pyint()%6,
                q1=fake.pyint()%6,
                q2=fake.pyint()%6)
            db.session.add(f)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
