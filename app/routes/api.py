import json
from flask import Blueprint, request, jsonify, session
import sqlalchemy
from app.models import User
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()
    
    try:
    # we use the dictionary data type here instead of an object (dot notation) as we are not attaching methods to this data response
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )

        db.add(newUser)
        db.commit()
        print('successfully added new user')

    except AssertionError:
        print('validation error')
        db.rollback()
        # NOTE THAT THIS ERROR RETURNS QUICKLY AND BEFORE THE DESCRIPTION IN THE TRACEBACK
    except sqlalchemy.exc.IntegrityError:
        print ('mysql error')
        print(sys.exc_info()[0])
        db.rollback()
        return jsonify(message = 'Signup failed, may be an existing account, email incorrect or password is not long enough'), 500
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(id = newUser.id)