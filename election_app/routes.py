
from flask import render_template, url_for, flash, redirect, request, abort
from election_app import app, db
from election_app.models import Candidate, Voter
from election_app.forms import RegistrationForm,Candidate_registraion_form


@app.route("/")
@app.route("/home")
def home():
	total_candidates = Candidate.query.order_by(Candidate.votes.desc()).all()
	return render_template("home.html", total_candidates=total_candidates)

@app.route("/register", methods=['GET','POST'])
#@login_required
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		new_voter = Voter(voter_name=form.name.data, address=form.address.data, voting_party=form.party.data)
		db.session.add(new_voter)
		current_candidate = Candidate.query.filter_by(party=form.party.data).first()
		current_candidate.votes += 1
		db.session.commit()
		flash("Your vote has been submitted.")

	return render_template("register.html", title='Vote', form=form)

@app.route("/new_candidate")
def add_candidate():
	form  = Candidate_registraion_form()
	if form.validate_on_submit():
		new_cand = Candidate(name=form.name.data, party=form.party.data)
		db.session.add(new_cand)
		db.session.commit()
		flash("Candidate has been added.")
		return redirect(url_for('home'))

	return render_template("candidate.html", title='Candidate Registration', form=form)
