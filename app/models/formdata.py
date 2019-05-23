from datetime import datetime
from .. import db


class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    firstname = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    satisfaction = db.Column(db.Integer)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)

    def __init__(self, firstname, email, age, income, satisfaction, q1, q2):
        self.firstname = firstname
        self.email = email
        self.age = age
        self.income = income
        self.satisfaction = satisfaction
        self.q1 = q1
        self.q2 = q2

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
