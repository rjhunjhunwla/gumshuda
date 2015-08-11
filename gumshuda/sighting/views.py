from django.shortcuts import render
from django.http import HttpResponse
from .models import sighting
import hashlib


# Create your views here.
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
	return HttpResponse('')