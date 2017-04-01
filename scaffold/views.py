import os, random, shutil, uuid

from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='store_mp3_form')
def store_mp3_form(request):
    return Response("""
    <html>
    <title>Arabic Dialect Demo</title>
    <body>
    <h1>Upload Audio File</h1>
    <form action="/store_mp3_test" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <label for="mp3">Mp3</label>
        <input id="mp3" name="mp3" type="file" value=""/>
        <input type="submit" value="submit"/>
    </form>
    </body>
    </html>
    """)

@view_config(route_name='store_mp3_test')
def store_mp3_test(request):

    # get the file name and the data of the submitted aduio
    input_file = request.POST['mp3'].file
    print(type(input_file))
    return Response(type(input_file))


@view_config(route_name='store_mp3_view')
def store_mp3_view(request):

    # get the file name and the data of the submitted aduio


    filename = request.POST['fname']
    input_file = request.POST['data'].make_file()

    print(type(input_file))

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

    # run the model and get the predictation
    cmdstr = "./scaffold/run_model.sh"
    res = os.popen(cmdstr).read()
    return Response(filename + "\nPrediction:" + res)

@view_config(route_name='client', renderer='templates/client.jinja2')
def my_client(request):
    return {'name': 'test_demooo', 'foo': random.randint(5,10)}

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'test_demooo'}
