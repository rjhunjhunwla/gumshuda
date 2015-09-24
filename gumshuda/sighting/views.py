from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Sighting

import utils
import fppfacematcher
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def get_facematcher(data, isUrl):
    return fppfacematcher.FacePPFM(data, isUrl)


def index(request):
    return render(request, 'index.html', {})


def handle_uploaded_file(request):
    if request.method == 'POST':
        s = Sighting()
        s.data = request.FILES['file'].read()
        if len(s.data) is 0:
            return None, 'No data'

        out, reason = detect_face(s.data)
        if out is False:
            return None, reason

        return s, ""


def upload(request):
    s, reason = handle_uploaded_file(request)
    if s is None:
        return HttpResponse(reason)
    f = get_facematcher(data, isUrl)
    picture_id, status = utils.save_picture(s.data)
    if status is True:
        f.match(picture_id)
    return HttpResponse(success)


@login_required
def add_pic_to_person(request):

    # validate if this user owns this profile, then only she can add picture to this profile.
    if 'person_id' not in request.GET:
        raise Http404
    objs = people.objects.filter(user=request.user.id, id=request.GET['person_id'])
    if objs is None:
        raise Http404

    ''' 
    Steps:
    1. Detect Face in picture.
    2. Save the picture locally
    3. Add the picture in FaceMatcher module to person.
    '''
    s, reason = handle_uploaded_file(request)
    if s is None:
        return HttpResponse(reason)

    # save picture in local database
    cause, statue = utils.add_source_picture(s.data, request.GET['person_id'])

    # Face reco. module may need to preprocess the picture for matching add it to person
    if status is True:
        f= get_facematcher(s.data,False)
        f.add_pic_to_person( request.GET['person_id'])


def detect_face(data, isUrl):
    f = get_facematcher(data, isUrl)
    status, reason = f.add_pic_to_set()
    return status, reason


def login(request):
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    print request.user
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/sighting/')
