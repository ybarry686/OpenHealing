from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from backend.db.queries.post_queries import create_post, get_all_posts, get_post
from backend.db.queries.user_queries import get_user_id

forum_bp = Blueprint("forum", __name__, url_prefix="/forum")


@forum_bp.route("/")
def forum_home():
    posts = get_all_posts()
    return render_template("forum.html", posts=posts)


@forum_bp.route("/new", methods=["POST"])
def new_post():
    if not session.get("username"):
        flash("Please log in to post.", "error")
        return redirect(url_for("auth.login"))

    title = request.form.get("title", "").strip()
    body = request.form.get("body", "").strip()
    category = request.form.get("category", "").strip() or None

    if not title or not body:
        flash("A post needs both a title and a message.", "error")
        return redirect(url_for("forum.forum_home"))

    user_id = get_user_id(session["username"])
    if user_id is None:
        session.clear()
        flash("Your session expired. Please log in again.", "error")
        return redirect(url_for("auth.login"))

    create_post(user_id, title, body, category)

    flash("Your post is up. Thank you for sharing.", "success")
    return redirect(url_for("forum.forum_home"))


@forum_bp.route("/post/<int:post_id>")
def view_post(post_id):
    post = get_post(post_id)
    if post is None:
        flash("That post could not be found.", "error")
        return redirect(url_for("forum.forum_home"))
    return render_template("post.html", post=post)