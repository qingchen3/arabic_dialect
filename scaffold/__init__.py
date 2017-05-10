from pyramid.config import Configurator
from wsgiref.simple_server import make_server

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)


    config.add_route('index', '/')

    config.add_route('store_text_view', '/store_text_view')
    config.add_route('submit_audio_view', '/submit_audio_view')

    config.scan()

    app = config.make_wsgi_app()
    port = 8080
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()


    return config.make_wsgi_app()
