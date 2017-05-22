from pyramid.view import view_config
from pyramid.response import Response
import os, random, shutil, uuid


@view_config(route_name='index', renderer='templates/test.jinja2')
def my_client(request):
    return {'index': 'index'}

@view_config(route_name='store_text_view')
def store_text_view(request):

    # get the file name and the data of the submitted aduio
    filename = request.POST['text'].filename
    input_file = request.POST['text'].file
    print(filename)
    #store the data file under directory "/tmp"
    file_path = os.path.join('/tmp', '%s.txt' % uuid.uuid4())

    # We first write to a temporary file to prevent incomplete files from
    # being used.

    temp_file_path = file_path + '~'
    final_file_path = os.path.join('/tmp', filename)

    # Finally write the data to a temporary file
    input_file.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    os.rename(temp_file_path, file_path)

    return Response(filename + "\n uploaded.")

@view_config(route_name='submit_audio_view')
def submit_audio_view(request):

    # get the file name and the data of the submitted aduio

    audio_name = 'audio'
    filename = request.POST[audio_name].filename
    input_file = request.POST[audio_name].file

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

    os.rename(temp_file_path, file_path)

    print (file_path)
    ############################
    prediction_f = "dialect.done"
    while not os.path.exists(prediction_f):
       time.sleep(5)

    #dialect_info={}
    #with open('dialect.done') as f:
    #   dialect_info = dict(x.rstrip().split(None, 1) for x in f)

    # read file

    #ave_reader = wave.open(file_path, 'r')

    #econds = int(wave_reader.getnframes() / wave_reader.getframerate())
    response = []
    freader = open(prediction_f, 'r')
    for line in freader.readlines():
        response.append(line.strip())
    print(','.join(response))
    #for i in range(0, seconds, 5):
    #   response.append('{} {} {} {} {}'.format(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))


    #import pdb; pdb.set_trace()

    # run the model and get the predictation
    cmdstr = "./scaffold/run_model.sh"
    #res = os.popen(cmdstr).read()
    #return Response(filename + "\nPrediction:" + res)
    return Response(','.join(response))
