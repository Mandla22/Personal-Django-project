from django.shortcuts import render, get_object_or_404
from django.core.files import File
from django.shortcuts import HttpResponse
from . models import *
from django.conf import settings
import os


def index(request):
    return render(request, 'index.html')


def projects(request):
    binary_objects = ProjectBinary.objects.all()
    src_objects = ProjectSRC.objects.all()

    context = {'binary_objects': binary_objects, 'src_objects': src_objects}
    return render(request, 'projects.html', context=context)


def about(request):
    return render(request, 'about.html')


def download(request, filename):
    if filename.find('-') == -1:
        path = settings.MEDIA_ROOT + filename
    else:
        path = settings.MEDIA_ROOT + "src/" + filename
    file = open(path, 'rb')
    download_file = File(file)

    response = HttpResponse(download_file, content_type='application/octet-stream')
    response['x-Sendfile'] = path
    response['Content-Length'] = os.stat(path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    file.close()
    return response



