from app import application, db
from flask import request, make_response, jsonify
from app.models.dummy_share_key import DummyShareKey


@application.route('/api/auth_public_key', methods=['POST'])
def create_auth_public_key():
    pass


@application.route('/api/ballots', methods=['POST'])
def create_ballot():
    pass


@application.route('/api/candidates', methods=['POST'])
def create_candidates():
    pass


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

    db.session.add(dummy_share_key)

    try:
        db.session.commit()
        return '', 201
    except:
        db.session.rollback()
        return '', 403


@application.route('/api/final_outcome', methods=['POST'])
def create_final_outcome():
    pass


@application.route('/api/partial_decryption', methods=['POST'])
def create_partial_decryption():
    pass


@application.route('/api/voter_public_key', methods=['POST'])
def create_voter_public_key():
    pass


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
