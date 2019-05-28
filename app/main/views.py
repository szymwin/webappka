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

    data = [['czy osoba wierzaca', 'wspiera', 'nie wspiera', 'trudno powiedziec'], ['tak', wt, wn, wtp],
            ['Nie', nt, nn, ntp], ['trudno powiedziec', tt, tn, ttp]]

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

@main.route("/choose", methods=['POST'])
def choose():
    fd_list = db.session.query(Formdata).all()

    option1 = request.form['option1']
    option2 = request.form['option2']

    optname1 = "niewybrano"
    optname2= "niewybrano"
    var11 = 0
    var12 = 0
    var13 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var31 = 0
    var32 = 0
    var33 = 0

    for el in fd_list:
        if option1 == 1:
            el.co1 = el.age
            optname1="Wiek"
        elif option1 == 2:
            el.co1 = el.home
            optname1="Miejsce zamieszkania"
        elif option1 == 3:
            el.co1 = el.gender
            optname1 = "Płeć"
        elif option1 == 4:
            el.co1 = el.sex
            optname1 = "Orientacja"
        elif option1 == 5:
            el.co1 = el.education
            optname1 = "Wykształcenie"
        elif option1 == 6:
            el.co1 = el.faith
            optname1 = "Wiara"

    for el in fd_list:
        if option2 == 1:
            el.co2 = el.friends
            optname2 = "Wiek"
        elif option2 == 2:
            el.co2 = el.home
            optname2 = "Miejsce zamieszkania"
        elif option2 == 3:
            el.co2 = el.gender
            optname2 = "Płeć"
        elif option2 == 4:
            el.co2 = el.sex
            optname2 = "Orientacja"
        elif option2 == 5:
            el.co2 = el.education
            optname2 = "Wykształcenie"
        elif option2 == 6:
            el.co2 = el.faith
            optname2 = "Wiara"
        elif option2 == 7:
            el.co2 = el.sex
            optname2 = "Orientacja"
        elif option2 == 8:
            el.co2 = el.education
            optname2 = "Wykształcenie"
        elif option2 == 9:
            el.co2 = el.faith
            optname2 = "Wiara"



    for el in fd_list:
        if el.co1 == 1:
            if el.co2 == 1:
                var11 += 1
            elif el.co2 == 2:
                var12 +=1
            elif el.co2 == 3:
                var13 += 1
        if el.co1 == 2:
            if el.co2 == 1:
                var21 += 1
            elif el.co2 == 2:
                var22 += 1
            elif el.co2 == 3:
                var23 += 1
        if el.co1 == 3:
            if el.co2 == 1:
                var31 += 1
            elif el.co2 == 2:
                var32 += 1
            elif el.co2 == 3:
                var33 += 1

    data = [[optname1, 'wspiera', 'nie wspiera', 'trudno powiedziec'], ['tak', var11, var12, var13],
            ['Nie', var21, var22, var23], ['trudno powiedziec', var31, var32, var33]]

    return redirect('/result'), render_template('main/result.html', data=data)