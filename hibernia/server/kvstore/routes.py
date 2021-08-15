from typing import Final, List

from aiohttp import web
from aiohttp.web_routedef import RouteDef

from hibernia.server.kvstore.handlers import set_handler, get_handler, del_handler

ROUTES: Final[List[RouteDef]] = [
    web.post('/{key}', set_handler),
    web.get('/{key}', get_handler),
    web.delete('/{key}', del_handler)
]
