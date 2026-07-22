from flask import Blueprint, render_template

findhelp_bp = Blueprint("findhelp", __name__)


@findhelp_bp.route("/find-help")
def find_help():
    return render_template("find_help.html")
