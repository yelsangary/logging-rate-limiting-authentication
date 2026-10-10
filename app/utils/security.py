from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.config import settings

# TODO: create the API key header scheme here.
# Reminder: APIKeyHeader is already imported above.
# Reminder: it is used below in Security(api_key_header).

api_key_header = APIKeyHeader(name="X-API-Key")


async def verify_api_key(api_key: str | None = Security(api_key_header)) -> str:
    """Resolve an API key to an internal user id.

    TODO: implement.
    """
    if not api_key or api_key not in settings.api_keys:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or Missing API Key (header: X-API-Key).")
    user_id = settings.api_keys[api_key]
    return user_id
