from backend.db.connection import session_scope
from backend.db.models import Post, User

def create_post(user_id, title, body):
    '''insert new post into the database'''
    with session_scope() as session:
        post = Post(user_id=user_id, title=title, body=body)
        session.add(post)

def get_all_user_posts(user_id):
    '''get all posts for a specific user'''
    with session_scope() as session:
        posts = session.query(Post).all()
        # return as list of dicts so Posts can be accessed after session closes
        return [
            {"id": p.id, "title": p.title, "body": p.body, "user_id": p.user_id, "created_at": p.created_at}
            for p in posts
        ]

def get_all_posts():
    '''displays posts for all users'''
    with session_scope() as session:
        users = session.query(User).all()
        return [
            get_all_user_posts(u.id)
            for u in users
        ]
