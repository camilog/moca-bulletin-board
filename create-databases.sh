#!/bin/bash

# Create databases

# Authority Public Key database
curl -X PUT http://localhost:5984/authority_public_key

# Voters Public Keys database
curl -X PUT http://localhost:5984/voters_public_keys

# Candidates List database
curl -X PUT http://localhost:5984/candidates_list

# Ballots database
curl -X PUT http://localhost:5984/ballots

# Multiplied Ballots database
curl -X PUT http://localhost:5984/multiplied_ballots

# Dummy Share database
curl -X PUT http://localhost:5984/dummy_share

# Partial Decryptions database
curl -X PUT http://localhost:5984/partial_decryptions

# Result of the Election database
curl -X PUT http://localhost:5984/election_result


# Create users

# Create user:admin pass:admin
curl -X PUT http://localhost:5984/_config/admins/admin -d '"admin"'