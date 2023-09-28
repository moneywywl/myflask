from . import user_bp


@user_bp.route("/name")
def userName():
    return "userName=test"
