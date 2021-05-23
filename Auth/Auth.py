class Auth:

    _user = None

    @staticmethod
    def logged_user(user=None):

        if Auth._user == None:
            Auth._user = user

        return Auth._user

    @staticmethod
    def logout():
        Auth._user = None
