import hashlib
from typing import Dict


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShortExceptuion(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


class PermissionError(Exception):
    pass


class User:
    def __init__(self, username: str, password: str):
        """
        Create a new user object. The password will be encrypted before storing.
        """

        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password: str) -> str:
        """
        Encrypt the password with the username and return the sha digest
        """
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(
            hash_string
        ).hexdigest()  # Convert binary hash to hexadecimal string

    def check_password(self, password) -> str:
        """
        Return True if the password is valid for the user, False otherwise
        """
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    def __init__(self):
        """
        Construct an authenticator to manage users logging in and out
        """
        self.users: Dict[str, User] = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShortExceptuion(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)
        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in

        return False


class Authorizor:
    def __init__(self, authenticator: Authenticator):
        self.authenticator = authenticator
        self._permissions = {}

    def add_permission(self, perm_name):
        """
        Create a new permission that users can be added to
        """
        try:
            perm_set = self._permissions[perm_name]
        except KeyError:
            self._permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """
        Grant the given permission to the user
        """
        try:
            perm_set = self._permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self._permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist.")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            return True


authenticator = Authenticator()
authorizor = Authorizor(authenticator)

if __name__ == "__main__":
    authenticator.add_user("abrar", "userPassword")
    authorizor.add_permission("paint")
    # authorizor.check_permission("paint", "joe") # Will throw notloggedinerror
    print(authenticator.is_logged_in("abrar"))
    authenticator.login("abrar", "userPassword")
    print(authenticator.is_logged_in("abrar"))
    # print(authorizor.check_permission("paint", "abrar")) # Throws notpermittederror
    # print(authorizor.check_permission("mix", "abrar")) # Permission does not exist
    authorizor.permit_user("paint", "abrar")
    # authorizor.permit_user("mix", "abrar") # Permission does not exist
    print(authorizor.check_permission("paint", "abrar"))
