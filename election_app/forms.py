from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from election_app.models import Candidate,Voter


class RegistrationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
	address = StringField('Address', validators=[DataRequired()])
	party = StringField('Party', validators=[DataRequired()])
	submit = SubmitField('Vote')

	def validate_data(self, name, address):
		db_voter = Voter.query.filter_by(voter_name=name.data).first()
		if db_voter:
			if db_voter.address == address.data :
				raise ValidationError("You've already voted!")

class Candidate_registraion_form(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
	party = StringField('Party', validators=[DataRequired()])
	submit = SubmitField('Register')

	def validate_candidate(self, name):
		cand = Candidate.query.filter_by(name=name.data).first()
		if cand:
			raise ValidationError("Candidate of this name already exist")
