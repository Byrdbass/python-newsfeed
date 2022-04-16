import json
from flask import Blueprint, request, jsonify, session
import sqlalchemy
from app.models import User, Post, Comment, Vote
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

@bp.route('/users/logout', methods=['POST'])
def logout():
    #remove session variables
    session.clear()
    return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()
    try:
        user = db.query(User).filter(User.email == data['email']).one()
    except:
        print(sys.exc_info()[0])

        return jsonify(message = 'Incorrect credentials, user may not exists or password is invalid'), 400
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials, user may not exists or password is invalid'), 400
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True

    return jsonify(id = user.id)

@bp.route('/comments', methods=['POST'])
def comment():
    data = request.get_json()
    db = get_db()
    try:
        #create a new comment
        newComment = Comment(
            comment_text = data['comment_text'],
            post_id = data['post_id'],
            user_id = session.get('user_id')
        )

        db.add(newComment)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Comment Failed'), 500
    return jsonify(id = newComment.id)