from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from backend.services.auth_client import AuthClient

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        success, message = AuthClient.signup(username, password)

        if success:
            session["username"] = username
            flash(message, "success")
            return redirect(url_for("main.home"))

        flash(message, "error")

    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        success, message = AuthClient.login(username, password)

        if success:
            session["username"] = username
            flash(message, "success")
            return redirect(url_for("main.home"))

        flash(message, "error")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))