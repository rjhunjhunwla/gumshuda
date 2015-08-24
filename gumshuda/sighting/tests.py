#from django.test import TestCase
import json
import fppfacematcher
j = json.load(open('test.json'))
f = fppfacematcher.FacePPFM("",False)
print f.get_face_id(j)

