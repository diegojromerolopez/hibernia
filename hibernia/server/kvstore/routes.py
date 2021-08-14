from aiohttp import web

from hibernia.server.kvstore.handles import set_handle, get_handle, del_handle

ROUTES = [
    web.post('/{key}', set_handle),
    web.get('/{key}', get_handle),
    web.delete('/{key}', del_handle)
]
