import secrets
import string
from . import crud
from sqlalchemy.orm import Session


def create_random_keys(length: int = 5) -> str:
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_key(db: Session) -> str:
    key = create_random_keys()
    while crud.get_db_url_by_key(db, key):
        key = create_random_keys()
    return key