from flask import render_template, redirect, request, Blueprint
import statistics
from .. import db
from app.models import Formdata

main = Blueprint('main', __name__)


@main.route("/")
def welcome():
    return render_template('main/welcome.html')

# TODO: utworzenie dodatkowych modulow / pakietow
@main.route("/form")
def show_form():
    return render_template('main/form.html')


@main.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('main/raw.html', formdata=fd)


@main.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    satisfaction = []
    q1 = []
    q2 = []
    for el in fd_list:
        satisfaction.append(int(el.satisfaction))
        q1.append(int(el.q1))
        q2.append(int(el.q2))

    if len(satisfaction) > 0:
        mean_satisfaction = statistics.mean(satisfaction)
    else:
        mean_satisfaction = 0

    if len(q1) > 0:
        mean_q1 = statistics.mean(q1)
    else:
        mean_q1 = 0

    if len(q2) > 0:
        mean_q2 = statistics.mean(q2)
    else:
        mean_q2 = 0

    # Prepare data for google charts
    data = [['Satisfaction', mean_satisfaction], ['Python skill', mean_q1], ['Flask skill', mean_q2]]

    return render_template('main/result.html', data=data)


@main.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    age = request.form['age']
    home = request.form['home']
    gender = request.form['gender']
    sex = request.form['sex']
    education = request.form['education']
    faith = request.form['faith']
    friends = request.form['friends']
    family = request.form['family']
    view = request.form['view']
    openminded = request.form['openminded']
    support = request.form['support']
    manifest = request.form['manifest']
    partnership = request.form['partnership']
    kids = request.form['kids']
    status = request.form['status']

    # Save the data
    fd = Formdata(age, home, gender, sex, education, faith, friends, family, view, openminded, support, manifest,
                  partnership, kids, status)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')

