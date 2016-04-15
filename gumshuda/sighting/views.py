from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Sighting
from .models import MissingPerson

import utils
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


@login_required
def add_pic_to_person(request): 
    # validate if this user owns this profile, then only she can add picture to this profile.
    if 'person_id' not in request.GET:
        raise Http404
    objs = MissingPerson.objects.filter(reporting_user_id=request.user.id, id=request.GET['person_id'])
    if objs is None:
        raise Http404

    ''' 
    Steps:
    1. Detect Face in picture.
    2. Save the picture locally
    3. Add the picture in FaceMatcher module to person.
    '''
    try:
        matcher = utils.handle_uploaded_file(request)
        utils.add_source_picture(request.GET['person_id'],matcher)
    except Exception as e:
        raise Http404(e)
    return HttpResponse("done")


def check_if_missing(request):
    matcher = utils.handle_uploaded_file(request)
    matcher.match()
    pass


@login_required
def create_new_missing_profile(request):
    saved_id = utils.save_person(request, request.user.id)
    if saved_id is None:
        return "Failed. Try again"

    return "Successfully saved, add pictures of missing person."


######################################################################
def login(request):
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    print request.user
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/sighting/')
