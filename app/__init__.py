# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# flask_app = Flask(__name__)
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///covid_data.db'
# flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy()
# db.init_app(flask_app)

# from . import routes



# from flask import Flask
# import os

 
# app = Flask(__name__)
# #CORS(app, support_credentials=True)
 
# app_settings = os.getenv(
#     'APP_SETTINGS',
#     'app.config.DevelopmentConfig'
# )
# app.config.from_object(app_settings)
 
# app.config['SECRET_KEY'] = 'some-secret-string'
 
# #ENV Variables

# from app.api.views import auth_blueprint
 
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Origin,Access-Control-Allow-Methods,Allow,Content-Length,Access-Control-Allow-Headers,Age,Server,Via,Date')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,PATCH')
#     return response
 
# app.register_blueprint(auth_blueprint)
