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


@main.route("/chooseresult")
def show_chooseresult():
    return render_template('main/chooseresult.html')


@main.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('main/raw.html', formdata=fd)


# @main.route("/result")
# def show_result():
#     fd_list = db.session.query(Formdata).all()
#
#     wt = 0
#     wn = 0
#     wtp = 0
#     nt = 0
#     nn = 0
#     ntp = 0
#     tt = 0
#     tn = 0
#     ttp = 0
#
#     for el in fd_list:
#         el.co = el.faith
#         if el.co == 1:
#             if el.support == 1:
#                 wt += 1
#             elif el.support == 2:
#                 wn +=1
#             elif el.support == 3:
#                 wtp += 1
#         if el.co == 2:
#             if el.support == 1:
#                 nt += 1
#             elif el.support == 2:
#                 nn += 1
#             elif el.support == 3:
#                 ntp += 1
#         if el.co == 3:
#             if el.support == 1:
#                 tt += 1
#             elif el.support == 2:
#                 tn += 1
#             elif el.support == 3:
#                 ttp += 1
#
#     data = [['czy osoba wierzaca', 'wspiera', 'nie wspiera', 'trudno powiedziec'], ['tak', wt, wn, wtp],
#             ['Nie', nt, nn, ntp], ['trudno powiedziec', tt, tn, ttp]]
#
#     return render_template('main/result.html', data=data)


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


@main.route("/result", methods=["POST"])
def choose():
    fd_list = db.session.query(Formdata).all()

    if 'option1' and 'option2' in globals():
        option1 = int(request.POST['option1'])
        option2 = int(request.POST['option2'])
    else:
        option1 = 1
        option2 = 1

    optname1 = "niewybrano"
    var11 = 0
    var12 = 0
    var13 = 0
    var21 = 0
    var22 = 0
    var23 = 0
    var31 = 0
    var32 = 0
    var33 = 0
    name11 = "error"
    name12 = "error"
    name13 = "error"
    name21 = "error"
    name22 = "error"
    name23 = "error"

    for el in fd_list:
        if option1 == 1:
            el.co1 = el.age
            optname1 = "Wiek"
            name11 = "poniżej 30lat"
            name12 = "pomiędzy 30 a 49 lat"
            name13 = "powyzej 50lat"
        elif option1 == 2:
            el.co1 = el.home
            optname1 = "Miejsce zamieszkania"
            name11 = "Wieś"
            name12 = "Małe miasto"
            name13 = "Duże miasto"
        elif option1 == 3:
            el.co1 = el.gender
            optname1 = "Płeć"
            name11 = "Mężczyzna"
            name12 = "Kobieta"
            name13 = "Inne"
        elif option1 == 4:
            el.co1 = el.sex
            optname1 = "Orientacja"
            name11 = "Heteroseksulana"
            name12 = "Homoseksualna"
            name13 = "Inne"
        elif option1 == 5:
            el.co1 = el.education
            optname1 = "Wykształcenie"
            name11 = "Podstawowe"
            name12 = "Średnie/Zawodowe"
            name13 = "Wyższe"
        elif option1 == 6:
            el.co1 = el.faith
            optname1 = "Wiara"
            name11 = "wierzący"
            name12 = "nie wierzący"
            name13 = "trudno powiedzieć"

    for el in fd_list:
        if option2 == 1:
            el.co2 = el.friends
            name21 = "Ktoś ze znajomych w środowisku LGBT - Tak"
            name22 = "Ktoś ze znajomych w środowisku LGBT - Nie"
            name23 = "Ktoś ze znajomych w środowisku LGBT - Trudno powiedzieć"
        elif option2 == 2:
            el.co2 = el.family
            name21 = "Członek rodziny w środowisku LGBT - Tak"
            name22 = "Członek rodziny w środowisku LGBT - Nie"
            name23 = "Członek rodziny w środowisku LGBT - Trudno powiedzieć"
        elif option2 == 3:
            el.co2 = el.view
            name21 = "Orientacja wpływa na postrzeganie - Tak"
            name22 = "Orientacja wpływa na postrzeganie - Zależy od sytuacji"
            name23 = "Orientacja wpływa na postrzeganie - Nie"
        elif option2 == 4:
            el.co2 = el.openminded
            name21 = "Czy jesteś osobą tolerancyjną? - Tak"
            name22 = "Czy jesteś osobą tolerancyjną? - Nie"
            name23 = "Czy jesteś osobą tolerancyjną? - Trudno powiedzieć"
        elif option2 == 5:
            el.co2 = el.support
            name21 = "Wspieranie osób LGBT - Tak"
            name22 = "Wspieranie osób LGBT - Nie"
            name23 = "Wspieranie osób LGBT - Jest mi to obojętne"
        elif option2 == 6:
            el.co2 = el.manifest
            name21 = "Aktywne wsparcie osób LGBT - Tak"
            name22 = "Aktywne wsparcie osób LGBT - Nie"
            name23 = "Aktywne wsparcie osób LGBT - Jestem przeciwko manifestacjom"
        elif option2 == 7:
            el.co2 = el.partnership
            name21 = "Poparcie dla związków partnerskich - Tak"
            name22 = "Poparcie dla związków partnerskich - Nie"
            name23 = "Poparcie dla związków partnerskich - Ciężko powiedzieć"
        elif option2 == 8:
            el.co2 = el.kids
            name21 = "Poparcie dla adopcji przez pary jednopłciowe - Tak"
            name22 = "Poparcie dla adopcji przez pary jednopłciowe - Nie"
            name23 = "Poparcie dla adopcji przez pary jednopłciowe - Nie jestem pewien/pewna"
        elif option2 == 9:
            el.co2 = el.status
            name21 = "Ocena sytuacji środowiska LGBT w polsce - Źle"
            name22 = "Ocena sytuacji środowiska LGBT w polsce - Neutralnie"
            name23 = "Ocena sytuacji środowiska LGBT w polsce - Dobrze"

    for el in fd_list:
        if el.co1 == 1:
            if el.co2 == 1:
                var11 += 1
            elif el.co2 == 2:
                var12 += 1
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

    data = [[optname1, name21, name22, name23], [name11, var11, var12, var13],
            [name12, var21, var22, var23], [name13, var31, var32, var33]]

    return render_template('main/result.html', data=data)
