from fastapi import HTTPException,status
from typing import Any
NotFoundException = HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user not foind')
class UserNotFound(HTTPException):
    def __init__(self,)->None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'user not found'

class UserAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = 'user already exists'
class PasswordOrUserIncorrect(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'Password or user not found'

class PostNotFound(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'Post not found '

