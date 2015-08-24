
from django.shortcuts import render
from django.http import HttpResponse
from .models import sighting
import faceplusplus
import utils
import fppfacematcher
# Create your views here.


FPP_API_KEY='c0a7934f98fcdd0765bca604c5962ca6'
FPP_API_SECRET=''
FPP_API_HOST='https://apius.faceplusplus.com/'

def get_facematcher( data, isUrl ):
	return fppfacematcher.FacePPFM(data,isUrl)

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

		out,reason = detect_face(s.data)
		if out is False:
			return HttpResponse(reason)		
		
		s.csum = hashlib.sha256(s.data).hexdigest()
		s.save()

	return HttpResponse('')

@login
def add_pic_to_person(request):
	pass


def detect_face( data, isUrl ):
	f = get_facematcher(data,isUrl)
	status, reason = f.add_pic_to_set()
	return status, reason