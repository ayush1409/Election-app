from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from election_app.models import Candidate,Voter
from flask import flash


class RegistrationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
	aadhar_number = StringField('Aadhar Number', validators=[DataRequired(), Length(min=12,max=12)])
	party = StringField('Party', validators=[DataRequired()])
	submit = SubmitField('Vote')

	def validate_voter(self, aadhar_number):
		db_voter = Voter.query.filter_by(aadhar_number=aadhar_number.data).first()
		if db_voter:
			flash("You've already voted.",'success')
			return 1
		return 0

class Candidate_registraion_form(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
	party = StringField('Party', validators=[DataRequired()])
	submit = SubmitField('Register')

	def validate_candidate(self, name):
		cand = Candidate.query.filter_by(name=name.data).first()
		if cand:
			raise ValidationError("Candidate of this name already exist")
