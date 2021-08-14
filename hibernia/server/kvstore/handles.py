from aiohttp import web

from hibernia.server.kvstore.storage import KV_STORE


async def set_handle(request):
    key = request.match_info.get('key')
    val = await request.text()
    stored = KV_STORE.set(key, val)
    if not stored:
        return web.Response(status=400)
    return web.Response(status=201)


async def get_handle(request):
    key = request.match_info.get('key')
    value = KV_STORE.get(key)
    return web.Response(body=value, status=200)


async def del_handle(request):
    key = request.match_info.get('key')
    found = KV_STORE.del_item(key)
    if not found:
        return web.Response(status=404)
    return web.Response(status=200)
