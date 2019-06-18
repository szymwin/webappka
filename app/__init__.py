from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'


    # if os.environ.get('Foo') is not None:
    #     app.config['SECRET_KEY'] = os.environ['']

    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    # db = SQLAlchemy(app)
    db.init_app(app)
    # db = SQLAlchemy(app)

    # with app.test_request_context():
    #     db.create_all()
    #     db.session.commit()

    # Create app blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


#TODO: nie wchodzi wgl w ten blok
if __name__ == "__main__":
    app = create_app('default')
    app.debug = True
    app.run(host='0.0.0.0')

