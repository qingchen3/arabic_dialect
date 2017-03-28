import shutil
import os
import uuid
import random
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render_to_response

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def store_mp3_form(request):
    return Response("""
    <html>
    <title>Arabic Dialect Demo</title>
    <body>
    <h1>Upload Audio File</h1>
    <form action="/store_mp3_view" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <label for="mp3">Mp3</label>
        <input id="mp3" name="mp3" type="file" value=""/>
        <input type="submit" value="submit"/>
    </form>
    </body>
    </html>
    """)
    #return render_to_response('templates/store_mp3_form.pt', {}request=request)

def store_mp3_view(request):

    # get the file name and the data of the submitted aduio
    filename = request.POST['mp3'].filename
    input_file = request.POST['mp3'].file

    #store the data file under directory "/tmp"
    file_path = os.path.join('/tmp', '%s.mp3' % uuid.uuid4())

    # We first write to a temporary file to prevent incomplete files from
    # being used.

    temp_file_path = file_path + '~'
    final_file_path = os.path.join('/tmp', filename)

    # Finally write the data to a temporary file
    input_file.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    os.rename(temp_file_path, final_file_path)
    #import pdb; pdb.set_trace()

    # return the predictation
    res = "Dialect 1:" + str(random.random()) + "\n Dialect 2:" + str(random.random()) + \
          "\n Dialect 3:" + str(random.random()) + "\n Dialect 4:" + str(random.random()) + \
          "\n Dialect 5:" + str(random.random())

    return Response(res)

if __name__ == '__main__':
    config = Configurator()

    config.add_route('store_mp3_form', '/store_mp3_form')
    config.add_view(store_mp3_form, route_name='store_mp3_form')

    config.add_route('store_mp3_view', '/store_mp3_view')
    config.add_view(store_mp3_view, route_name='store_mp3_view')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()