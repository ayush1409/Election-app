
from election_app import db
from flask_login import UserMixin

class Candidate(db.Model, UserMixin):
	name = db.Column(db.String(40), unique=False, nullable=False, primary_key=True)
	party = db.Column(db.String(20), unique=False, nullable=False)
	votes = db.Column(db.BigInteger, unique=False, default=0)

	def __repr__(self):
		return "Candidate({},{},{})".format(self.name, self.party, self.votes)

class Voter(db.Model, UserMixin):
	aadhar_number = db.Column(db.String(12), unique=True, nullable=False, primary_key=True)
	voter_name = db.Column(db.String(40),unique=False, nullable=True)
	voting_party = db.Column(db.String(20),unique=False, nullable=False)

	def __repr__(self):
		return "Voter({},{},{})".format(self.voter_name, self.address, self.voting_party)
