
from django.shortcuts import render
from django.http import HttpResponse
from .models import sighting
import hashlib
import faceplusplus
import os
import sys
# Create your views here.


FPP_API_KEY='c0a7934f98fcdd0765bca604c5962ca6'
FPP_API_SECRET='	'
FPP_API_HOST='https://apius.faceplusplus.com/'

def index(request):
    return render( request, 'index.html', {})


def handle_uploaded_file(f):
	data = []
	for chunk in f.chunks():
		data.append(chunk)
	return data

def upload(request):
	if request.method == 'POST':
		s = sighting()
		s.data =  request.FILES['file'].read()
		if len( s.data ) is 0:
			return HttpResponse('no data')
		s.csum = hashlib.sha256(s.data).hexdigest()
		s.save()
		detect_face(s.data)
	return HttpResponse('')


def detect_face( f ):
	api = faceplusplus.API(FPP_API_KEY, FPP_API_SECRET, FPP_API_HOST)
	import pdb;pdb.set_trace()
	print api.detection.detect( post=True, img = faceplusplus.File('/Users/madhu/Downloads/test2.jpeg'))

detect_face( None )