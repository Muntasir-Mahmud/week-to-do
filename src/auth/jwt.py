from google.oauth2.id_token import verify_oauth2_token
from google.auth.transport import requests
from fastapi import HTTPException, status

CLIENT_ID = 'os.environ.get("GOOGLE_CLIENT_ID", "")'


def verify_token_google(token: str):
    try:
        token_data = verify_oauth2_token(
            token,
            requests.Request(),
            CLIENT_ID,
        )
        return token_data
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
