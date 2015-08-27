
from django.shortcuts import render
from django.http import HttpResponse
from .models import sighting
import faceplusplus
import utils
import fppfacematcher
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


FPP_API_KEY='c0a7934f98fcdd0765bca604c5962ca6'
FPP_API_SECRET=''
FPP_API_HOST='https://apius.faceplusplus.com/'

def get_facematcher( data, isUrl ):
	return fppfacematcher.FacePPFM(data,isUrl)

def index(request):
    return render( request, 'index.html', {})


def handle_uploaded_file(request):
	if request.method == 'POST':
		s = sighting()
		s.data =  request.FILES['file'].read()
		if len( s.data ) is 0:
			return None,'No data'

		out,reason = detect_face(s.data)
		if out is False:
			return None,reason
		
		return s,""

def upload(request):
	s,reason = handle_uploaded_file(request)
	if s is None:
		return HttpResponse(reason)
	f = get_facematcher(data,isUrl)
	picture_id, status = utils.save_picture(s.data)
	if status is True:
		f.match(picture_id)
	return HttpResponse(success)

@login_required
def add_pic_to_person(request):
	s,reason = handle_uploaded_file(request)
	if s is None:
		return HttpResponse(reason)

	#This is a security issue, it should not take person id from url without verifying
	#TODO: verify is this person is owner of this profile.
	utils.add_source_picture(s.data, request.GET['person_id'])


def detect_face( data, isUrl ):
	f = get_facematcher(data,isUrl)
	status, reason = f.add_pic_to_set()
	return status, reason



def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    print request.user
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/sighting/')