from backend.db.connection import session_scope
from backend.db.models import Post, User

def create_post(user_id, title, body, category=None):
    '''insert new post into the database'''
    with session_scope() as session:
        post = Post(user_id=user_id, title=title, body=body, category=category)
        session.add(post)

def _post_to_dict(post, username):
    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "category": post.category,
        "user_id": post.user_id,
        "username": username,
        "created_at": post.created_at,
    }

def get_all_posts():
    '''returns every post, newest first, with the author's username joined in'''
    with session_scope() as session:
        rows = (
            session.query(Post, User.username)
            .join(User, User.id == Post.user_id)
            .order_by(Post.created_at.desc(), Post.id.desc())
            .all()
        )
        return [_post_to_dict(post, username) for post, username in rows]

def get_all_user_posts(user_id):
    '''get all posts for a specific user'''
    with session_scope() as session:
        rows = (
            session.query(Post, User.username)
            .join(User, User.id == Post.user_id)
            .filter(Post.user_id == user_id)
            .order_by(Post.created_at.desc(), Post.id.desc())
            .all()
        )
        return [_post_to_dict(post, username) for post, username in rows]

def get_post(post_id):
    '''returns a single post by id, with the author's username joined in, or None'''
    with session_scope() as session:
        row = (
            session.query(Post, User.username)
            .join(User, User.id == Post.user_id)
            .filter(Post.id == post_id)
            .first()
        )
        if row is None:
            return None
        post, username = row
        return _post_to_dict(post, username)