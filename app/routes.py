from flask import Blueprint, jsonify
from app.models import ConfirmedCases, RecoveredCases, CountriesToContinent
from app.application import db

# Create a blueprint for routes
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/global-data/<date>', methods=['GET'])
def get_global_data(date):
    # Query for global-level data
    confirmed_cases = db.session.query(db.func.sum(ConfirmedCases.confirmed)).filter_by(date=date).scalar()
    recovered_cases = db.session.query(db.func.sum(RecoveredCases.recovered)).filter_by(date=date).scalar()
    if confirmed_cases is not None and confirmed_cases > 0:
        recovery_ratio = recovered_cases / confirmed_cases
    else:
        recovery_ratio = 0.0
    return jsonify(global_confirmed_cases=confirmed_cases, 
                   global_recovered_cases=recovered_cases, 
                   recovery_ratio=recovery_ratio)

@routes_bp.route('/continent-data/<date>/<continent_name>', methods=['GET'])
def get_continent_data(date, continent_name):
    # Query for continent-level data
    continent_cases = db.session.query(db.func.sum(ConfirmedCases.confirmed)).join(ConfirmedCases.country_continent).filter(CountriesToContinent.continent == continent_name, ConfirmedCases.date == date).scalar()
    continent_recovered = db.session.query(db.func.sum(RecoveredCases.recovered)).join(RecoveredCases.country_continent).filter(CountriesToContinent.continent == continent_name, RecoveredCases.date == date).scalar()
    if continent_cases is not None and continent_cases > 0:
        recovery_ratio = continent_recovered / continent_cases
    else:
        recovery_ratio = 0.0
    return jsonify(continent=continent_name, 
                   confirmed_cases=continent_cases, 
                   recovered_cases=continent_recovered, 
                   recovery_ratio=recovery_ratio)

@routes_bp.route('/country-data/<date>/<country_name>', methods=['GET'])
def get_country_data(date, country_name):
    # Query for country-level data
    country_cases_query = db.session.query(db.func.sum(ConfirmedCases.confirmed)).filter_by(date=date, country_region=country_name)
    breakpoint()
    country_cases = db.session.query(db.func.sum(ConfirmedCases.confirmed)).filter_by(date=date, country_region=country_name).scalar()
    country_recovered = db.session.query(db.func.sum(RecoveredCases.recovered)).filter_by(date=date, country_region=country_name).scalar()
    if country_cases is not None and country_cases > 0:
        recovery_ratio = country_recovered / country_cases
    else:
        recovery_ratio = 0.0
    return jsonify(country=country_name, 
                   confirmed_cases=country_cases, 
                   recovered_cases=country_recovered, 
                   recovery_ratio=recovery_ratio)

@routes_bp.route('/state-data/<date>/<state_name>', methods=['GET'])
def get_state_data(date, state_name):
    # Query for state-level data
    state_cases = db.session.query(db.func.sum(ConfirmedCases.confirmed)).filter_by(date=date, province_state=state_name).scalar()
    state_recovered = db.session.query(db.func.sum(RecoveredCases.recovered)).filter_by(date=date, province_state=state_name).scalar()
    if state_cases is not None and state_cases > 0:
        recovery_ratio = state_recovered / state_cases
    else:
        recovery_ratio = 0.0
    return jsonify(state=state_name, 
                   confirmed_cases=state_cases, 
                   recovered_cases=state_recovered, 
                   recovery_ratio=recovery_ratio)

@routes_bp.route('/country-state-data/<date>/<country_name>/<state_name>', methods=['GET'])
def get_country_state_data(date, country_name, state_name):
    # Query for data at the intersection of country and state
    country_state_cases = db.session.query(db.func.sum(ConfirmedCases.confirmed)).filter_by(date=date, country_region=country_name, province_state=state_name).scalar()
    country_state_recovered = db.session.query(db.func.sum(RecoveredCases.recovered)).filter_by(date=date, country_region=country_name, province_state=state_name).scalar()
    if country_state_cases is not None and country_state_cases > 0:
        recovery_ratio = country_state_recovered / country_state_cases
    else:
        recovery_ratio = 0.0
    return jsonify(country=country_name, state=state_name, 
                   confirmed_cases=country_state_cases, 
                   recovered_cases=country_state_recovered, 
                   recovery_ratio=recovery_ratio)
