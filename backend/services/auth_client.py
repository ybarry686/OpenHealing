from werkzueg.security import generate_password_hash

from backend.db.queries.user_queries import (
    create_user, 
    is_existing_user,
    is_valid_login
)


class AuthClient:

    @staticmethod
    def signup(username: str, password: str) -> tuple[bool, str]:
        ''' Creates new user if the username is available '''

        if is_existing_user(username):
            return False, "Username already exists."
        
        password_hash = generate_password_hash(password)
        create_user(username, password_hash)

        return True, "Account created successfully!"


    @staticmethod
    def login(username: str, password: str) -> tuple[bool, str]:
        ''' Attempts to log a user in, if the account exists '''
                
        if is_valid_login(username, password):
            return True, "Login successful!"
        
        return False, "Invalid username or password"
