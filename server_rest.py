# gunicorn server_rest:app --worker-class aiohttp.worker.GunicornWebWorker

from aiohttp import web
from datetime import datetime

from data import users


async def get_users(request):
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] #{app["count"]}')
    app['count'] += 1

    return web.json_response({'user': users})


app = web.Application()
app.router.add_route('GET', '/users', get_users)
app['count'] = 1
