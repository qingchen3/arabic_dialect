from pyramid.config import Configurator
from wsgiref.simple_server import make_server
from waitress import serve

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('client', '/client')
    #config.add_route('test', '/test')
    config.add_route('store_mp3_form', '/store_mp3_form')
    config.add_route('store_mp3_view', '/store_mp3_view')

    config.add_route('store_mp3_test', '/store_mp3_test')
    #config.add_route('store_audio_form', '/store_audio_form')

    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    #serve(app, listen='0.0.0.0:8080', url_scheme='https')
    server.serve_forever()

    return app
