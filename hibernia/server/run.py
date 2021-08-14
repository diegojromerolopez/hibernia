from aiohttp import web

from hibernia.server.kvstore.routes import ROUTES

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(ROUTES)
    web.run_app(app)
