import uuid
import datetime

from instance import db
from app.auth.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode("utf-8")
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_all_users():
    return User.query.all()


def get_paginated_list(results, url, page, per_page):
    page = int(page)
    per_page = int(per_page)
    # import pdb;pdb.set_trace()
    count = len(results)
    if count < page or per_page < 0:
        abort(404)
    # make response
    obj = {}
    obj['page'] = page
    obj['per_page'] = per_page
    obj['count'] = count
    # make URLs
    # make previous url
    if page == 1:
        obj['previous'] = ''
    else:
        page_copy = max(1, page - per_page)
        per_page_copy = page - 1
        obj['previous'] = url + '?page=%d&per_page=%d' % (page_copy, per_page_copy)
    # make next url
    if page + per_page > count:
        obj['next'] = ''
    else:
        page_copy = page + per_page
        obj['next'] = url + '?page=%d&per_page=%d' % (page_copy, per_page)
    # finally extract result according to bounds
    obj['results'] = results[(page - 1):(page - 1 + per_page)]
    return obj



def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()