import facematcherbase
import faceplusplus
from .models import picture
FPP_API_KEY='c0a7934f98fcdd0765bca604c5962ca6'
FPP_API_SECRET='UHjCbfZk0RWu5U74-c7BkOpb-L00Ilnz'
FPP_API_HOST='https://apius.faceplusplus.com/'


"""
Faceplusplus API based face recognition.
@see http://www.faceplusplus.com
"""
class FacePPFM( facematcherbase.FaceMatcherBase ):
	def __init__( self, data, isUrl = True ):
		super( FacePPFM, self ).__init__( data, isUrl )

	def match( ):
		raise NotImplementedError( 'Not yet implemented, TODO' )
	
	def get_current_faceset( ):
		return ""

	def get_face_id( j ):
		return None

	def add_pic_to_set( p ):
		api = faceplusplus.API(FPP_API_KEY, FPP_API_SECRET, FPP_API_HOST)
		if self.isUrl:
			fpobj = api.detection.detect( url = self.data )
		else:
			fpobj = api.detection.detect( post=True, img = self.data )
		if fpobj is not None:
			p.prop = fpobj
			p.save()
		else:
			return False
		face_set = get_current_faceset()
		face_id = get_face_id(p.prop)
		api.faceset.add_face( faceset = face_set, faceid = face_id )
		raise True