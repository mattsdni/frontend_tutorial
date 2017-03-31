from flask import redirect, url_for, render_template, flash

from frontend_tutorial import app, db
from frontend_tutorial.forms import ApplicantForm
from frontend_tutorial.models import Applicant


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    applicant_form = ApplicantForm()
    if applicant_form.validate_on_submit():
        applicant = Applicant()
        applicant.email = applicant_form.email.data
        applicant.fname = applicant_form.fname.data
        applicant.lname = applicant_form.lname.data
        db.session.add(applicant)
        db.session.commit()
        flash('Thanks for signing up!', 'success')
        return redirect(url_for('view_applicant', applicant_id=applicant.id))
    return render_template('index.html', applicant_form=applicant_form)


@app.route('/applicant/<int:applicant_id>', methods=['GET'])
def view_applicant(applicant_id):
    applicant = Applicant.query.get_or_404(applicant_id)
    return render_template('applicant.html', applicant=applicant)


@app.route('/dashboard/<int:applicant_id>', methods=['GET'])
def dashboard(applicant_id):
    return render_template('dashboard.html', applicant_id=applicant_id)


