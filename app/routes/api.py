from flask import Blueprint, request
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db
    
    # we use the dictionary data type here instead of an object (dot notation) as we are not attaching methods to this data response
    newUser = User(
        username = data['username'],
        email = data['email'],
        password = data['password']
    )

    db.add(newUser)
    db.commit()

    return ''