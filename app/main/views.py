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

    wt = 0
    wn = 0
    wtp = 0
    nt = 0
    nn = 0
    ntp = 0
    tt = 0
    tn = 0
    ttp = 0

    for el in fd_list:
        el.co = el.faith
        if el.co == 1:
            if el.support == 1:
                wt += 1
            elif el.support == 2:
                wn +=1
            elif el.support == 3:
                wtp += 1
        if el.co == 2:
            if el.support == 1:
                nt += 1
            elif el.support == 2:
                nn += 1
            elif el.support == 3:
                ntp += 1
        if el.co == 3:
            if el.support == 1:
                tt += 1
            elif el.support == 2:
                tn += 1
            elif el.support == 3:
                ttp += 1

    data = [['Tak', wt], ['Nie', wn], ['Trudno powiedziec', wtp]]

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

