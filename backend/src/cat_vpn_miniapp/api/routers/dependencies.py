import logging

from aiogram.utils.web_app import WebAppInitData, safe_parse_webapp_init_data
from fastapi import HTTPException
from fastapi.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED

from cat_vpn_miniapp.core.config import Config

logger = logging.getLogger(__name__)

config = Config()


def auth(request: Request) -> WebAppInitData | None:
    try:
        auth_string = request.headers.get("initData")
        if auth_string:
            data = safe_parse_webapp_init_data(
                init_data=auth_string,
                token=config.bot_config.token.get_secret_value(),
            )
            return data
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

    except Exception as e:
        logger.warning("Trying unauthorized request: %s", e)
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        ) from e
