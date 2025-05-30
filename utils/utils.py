from  uuid import UUID
import re


def transform_uuid(raw_uuid: str) -> UUID:
    """Transform a raw or hyphenated UUID string into a UUID object."""
    if isinstance(raw_uuid, UUID):
        return raw_uuid
    if not isinstance(raw_uuid, str):
        raise ValueError("UUID must be a string or UUID object")

    cleaned = raw_uuid.replace("-", "")
    if not re.match(r"^[0-9a-fA-F]{32}$", cleaned):
        if re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", raw_uuid):
            try:
                return UUID(raw_uuid)
            except ValueError:
                raise ValueError("Invalid UUID format")
        raise ValueError("Invalid UUID: must be 32 hexadecimal characters or valid hyphenated UUID")

    try:
        return UUID(cleaned)
    except ValueError:
        raise ValueError("Invalid UUID format")