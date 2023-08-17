from auth.security.verify_password import verify_password


def verify_login_attempt(collab_repo, input_username, input_pw):
    username_check = collab_repo.get_by_username(input_username)
    if len(username_check) == 1:
        user = username_check[0]
        return verify_password(input_pw, user.password)
    return False
