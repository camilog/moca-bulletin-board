from app import application, db
from flask import request, make_response, jsonify
from app.models.dummy_share_key import DummyShareKey
from app.models.authority_public_key import AuthorityPublicKey
from app.models.voter_public_key import VoterPublicKey
from app.models.ballot import Ballot
from app.models.partial_decryption import PartialDecryption
from app.models.final_outcome import FinalOutcome
from app.models.election import Election
from app.models.candidate import Candidate
from app.models.multiplied_ballots import MultipliedBallots


@application.route('/api/auth_public_key', methods=['POST'])
def create_auth_public_key():
    if not request.json or not all(key in request.json for key in ('n', 'threshold', 'nsplusone')):
        return 'Bad Request: One or more attributes missing', 400

    n = request.json['n']
    threshold = request.json['threshold']
    nsplusone = request.json['nsplusone']

    authority_public_key = AuthorityPublicKey(n, threshold, nsplusone)

    # Delete previous authority public key
    AuthorityPublicKey.query.delete()

    db.session.add(authority_public_key)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/ballot', methods=['POST'])
def create_ballot():
    if not request.json or not all(key in request.json for key in ('voter_id', 'encrypted_vote', 'signature')):
        return 'Bad Request: One or more attributes missing', 400

    voter_id = request.json['voter_id']
    encrypted_vote = request.json['encrypted_vote']
    signature = request.json['signature']

    ballot = Ballot(voter_id, encrypted_vote, signature)

    db.session.add(ballot)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/election', methods=['POST'])
def create_election():
    if not request.json or not all(key in request.json for key in ('question', 'number_of_candidates', 'candidates')):
        return 'Bad Request: One or more attributes missing', 400

    question = request.json['question']
    number_of_candidates = request.json['number_of_candidates']
    candidates = request.json['candidates']

    election = Election(question, number_of_candidates)

    db.session.add(election)
    db.session.commit()

    election_id = Election.query.filter(Election.question == question).first().id

    for candidate in candidates:
        candidate_for_db = Candidate(candidate['id'], candidate['name'])
        candidate_for_db.election_id = election_id
        db.session.add(candidate_for_db)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/dummy_share_key', methods=['POST'])
def create_dummy_share_key():
    if not request.json or not all(key in request.json for key in ('n', 'l', 'w', 'v', 'i', 'si', 'vi')):
        return 'Bad Request: One or more attributes missing', 400

    n = request.json['n']
    l = request.json['l']
    w = request.json['w']
    v = request.json['v']
    si = request.json['si']
    i = request.json['i']
    vi = request.json['vi']

    dummy_share_key = DummyShareKey(n, l, w, v, si, i, vi)

    # Delete previous dummy share
    DummyShareKey.query.delete()

    db.session.add(dummy_share_key)

    try:
        db.session.commit()
        return '', 201
    except Exception as e:
        db.session.rollback()
        return '', 403


@application.route('/api/final_outcome', methods=['POST'])
def create_final_outcome():
    if not request.json or not all(key in request.json for key in ('candidate_id', 'votes')):
        return 'Bad Request: One or more attributes missing', 400

    candidate_id = request.json['candidate_id']
    votes = request.json['votes']

    final_outcome = FinalOutcome(candidate_id, votes)

    db.session.add(final_outcome)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/partial_decryption', methods=['POST'])
def create_partial_decryption():
    if not request.json or not all(key in request.json for key in ('authId', 'value')):
        return 'Bad Request: One or more attributes missing', 400

    auth_id = request.json['authId']
    value = request.json['value']

    partial_decryption = PartialDecryption(auth_id, value)

    db.session.add(partial_decryption)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/voter_public_key', methods=['POST'])
def create_voter_public_key():
    if not request.json or not all(key in request.json for key in ('voter_id', 'value')):
        return 'Bad Request: One or more attributes missing', 400

    voter_id = request.json['voter_id']
    value = request.json['value']

    voter_public_key = VoterPublicKey(voter_id, value)

    db.session.add(voter_public_key)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/multiplied_ballots', methods=['POST'])
def create_multiplied_ballots():
    if not request.json or not all(key in request.json for key in 'value'):
        return 'Bad Request: One or more attributes missing', 400

    value = request.json['value']

    multiplied_ballots = MultipliedBallots(value)

    db.session.add(multiplied_ballots)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
