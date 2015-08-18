#from django.test import TestCase

import faceplusplus

FPP_API_KEY='c0a7934f98fcdd0765bca604c5962ca6'
FPP_API_SECRET='UHjCbfZk0RWu5U74-c7BkOpb-L00Ilnz'
FPP_API_HOST='https://apius.faceplusplus.com/'

# Create your tests here.
def detect_face( f ):
	api = faceplusplus.API(FPP_API_KEY, FPP_API_SECRET, FPP_API_HOST)
	#import pdb;pdb.set_trace()
	print api.detection.detect( img = faceplusplus.File('/Users/madhu/Downloads/child_aboutus.jpg'))
	#print api.detection.detect( url = 'https://raw.githubusercontent.com/rjhunjhunwla/testimages/master/1.jpg')
detect_face( None )




from brpy import init_brpy

br = init_brpy(br_loc='/usr/local/lib/')
br.br_initialize_default()

img = open('catpic.jpg','rb').read()

br.br_set_property('algorithm','MyCatFaceDetectionModel')
br.br_set_property('enrollAll','true')

tmpl = br.br_load_img(img, len(img))
catfaces = br.br_enroll_template(tmpl)

print('This pic has %i cats in it!' % br.br_num_templates(catfaces))

br.br_free_template(tmpl)
br.br_free_template_list(catfaces)
br.br_finalize()
