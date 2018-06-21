
from election_app import db
from flask_login import UserMixin

class Candidate(db.Model, UserMixin):
	name = db.Column(db.String(40), unique=False, nullable=False, primary_key=True)
	party = db.Column(db.String(20), unique=False, nullable=False)
	votes = db.Column(db.BigInteger, unique=False, default=0)

	def __repr__(self):
		return "Candidate({},{},{})".format(self.name, self.party, self.votes)

class Voter(db.Model, UserMixin):
	voter_name = db.Column(db.String(40),unique=False, nullable=True, primary_key=True)
	address = db.Column(db.String(120),unique=False, nullable=False)
	voting_party = db.Column(db.String(20),unique=False, nullable=False)

	def __repr__(self):
		return "Voter({},{},{})".format(self.voter_name, self.address, self.voting_party)
