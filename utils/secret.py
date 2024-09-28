
from passlib.context import CryptContext

password_manger  = CryptContext(schemes=["bcrypt"], deprecated="auto")

