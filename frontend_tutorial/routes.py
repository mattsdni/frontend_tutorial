from frontend_tutorial import app, db
from frontend_tutorial.models import Applicant
from flask import request, jsonify, abort


@app.route("/api/v1/applicants", methods=['POST'])
def create_applicant():
    applicant = Applicant()
    db.session.add(applicant)
    db.session.commit()
    return applicant.to_json()


@app.route("/api/v1/applicants/<int:id>", methods=['GET'])
def read_applicant(id):
    applicant = Applicant.query.get_or_404(id)
    return applicant.to_json()


@app.route("/api/v1/applicants/<int:id>", methods=['PUT', 'PATCH'])
def update_applicant(id):
    if request.data:
        data = request.get_json()
        applicant = Applicant.query.get_or_404(id)
        applicant.from_json(source=data)
        db.session.add(applicant)
        db.session.commit()
        applicant = Applicant.query.get_or_404(id)
        return applicant.to_json()


@app.route("/api/v1/applicants/<int:id>", methods=['DELETE'])
def delete_applicant(id):
    Applicant.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify()
