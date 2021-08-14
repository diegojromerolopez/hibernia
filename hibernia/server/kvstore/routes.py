from aiohttp import web

from hibernia.server.kvstore.handlers import set_handler, get_handler, del_handler

ROUTES = [
    web.post('/{key}', set_handler),
    web.get('/{key}', get_handler),
    web.delete('/{key}', del_handler)
]
