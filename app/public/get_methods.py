from app import application, db
from flask import request, make_response, jsonify
from app.models.candidate import Candidate
from app.models.ballot import Ballot
from app.models.dummy_share_key import DummyShareKey


@application.route('/api/candidates_list', methods=['GET'])
def get_candidates_list():
    all_candidates = Candidate.query.all()

    return jsonify(all_candidates), 200


@application.route('/api/ballots', methods=['GET'])
def get_ballots():
    voter_id = request.args.get('voter_id', default=0, type=int)

    if voter_id is 0:
        # No voter_id provided, so it's asking for all ballots
        ballots = Ballot.query.all()

        return jsonify(ballots), 200
    else:
        # voter_id provided, so it's asking for a particular ballot
        ballot = Ballot.query.filter(Ballot.voter_id == voter_id).first()

        return jsonify(ballot.serialize), 200


@application.route('/api/dummy_share_key', methods=['GET'])
def get_dummy_share_key():
    dummy_share = DummyShareKey.query.first()

    return jsonify(dummy_share.serialize), 200
