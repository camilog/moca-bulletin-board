from app import application, db
from flask import request, make_response, jsonify
from app.models.candidate import Candidate
from app.models.ballot import Ballot
from app.models.dummy_share_key import DummyShareKey
from app.models.authority_public_key import AuthorityPublicKey
from app.models.final_outcome import FinalOutcome
from app.models.partial_decryption import PartialDecryption
from app.models.multiplied_ballots import MultipliedBallots


@application.route('/api/candidates_list', methods=['GET'])
def get_candidates_list():
    all_candidates = Candidate.query.all()

    return jsonify(list(map((lambda x: x.serialize), all_candidates))), 200


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

    if dummy_share is None:
        return '', 200

    return jsonify(dummy_share.serialize), 200


@application.route('/api/auth_public_key', methods=['GET'])
def get_auth_public_key():
    auth_public_key = AuthorityPublicKey.query.first()

    if auth_public_key is None:
        return '', 200

    return jsonify(auth_public_key.serialize), 200


@application.route('/api/election', methods=['GET'])
def get_election():
    return '', 200


@application.route('/api/final_outcome', methods=['GET'])
def get_final_outcome():
    final_outcome = FinalOutcome.query.first()

    if final_outcome is None:
        return '', 200

    return jsonify(final_outcome.serialize), 200


@application.route('/api/partial_decryptions', methods=['GET'])
def get_partial_decryption():
    auth_id = request.args.get('auth_id', default=0, type=int)

    if auth_id is 0:
        # No auth_id provided, so it's asking for all partial decryptions
        partial_decryptions = PartialDecryption.query.all()

        return jsonify(partial_decryptions), 200
    else:
        # auth_id provided, so it's asking for a particular partial decryption
        partial_decryption = PartialDecryption.query.filter(PartialDecryption.auth_id == auth_id).first()

        return jsonify(partial_decryption.serialize), 200


@application.route('/api/voters_public_keys', methods=['GET'])
def get_voter_public_key():
    return '', 200


@application.route('/api/multiplied_ballots', methods=['GET'])
def get_multiplied_ballots():
    multiplied_ballots = MultipliedBallots.query.first()

    if multiplied_ballots is None:
        return '', 200

    return jsonify(multiplied_ballots.serialize), 200

