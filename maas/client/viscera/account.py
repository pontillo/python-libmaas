"""Objects for accounts."""

__all__ = [
    "Account",
]

from . import (
    Object,
    ObjectType,
)
from ..utils.creds import Credentials
from ..utils.typecheck import typed


class AccountType(ObjectType):
    """Metaclass for `Account`."""

    @typed
    async def create_credentials(cls) -> Credentials:
        data = await cls._handler.create_authorisation_token()
        return Credentials(**data)

    @typed
    async def delete_credentials(cls, credentials: Credentials) -> None:
        await cls._handler.delete_authorisation_token(
            token_key=credentials.token_key)


class Account(Object, metaclass=AccountType):
    """The current account."""
