from backend.db.connection import session_scope
from backend.db.models import User

#     with session_scope() as session:
def create_user(username, password_hash):
    '''signs up user for the platform'''
    with session_scope() as session:
        user = User(username=username, password_hash=password_hash)
        session.add(user)

def is_existing_user(username):
    '''checks if this user already signed up'''
    with session_scope() as session:
        user = session.query(User).filter(User.username==username).first()
        return user is not None
def is_valid_login(username, password_hash):
    '''verifies the username and password_hash combo is correct'''
    with session_scope() as session:
        user = session.query(User).filter(User.username==username).first()
        if user:
            return user.password_hash == password_hash
        return False
