class FaceMatcherBase:
	def __init__( self ):
		pass

	"""
	check if the image has a match in database 
	"""
	def match( picture_id ):
		raise NotImplementedError( 'Derived class should override this function' )

	"""
	add image to dataset
	"""
	def add_pic_to_set( p ):
		raise NotImplementedError( 'Derived class should override this function' )


	"""
	add the picture_id picture to person_id
	"""
	def add_pic_to_person( person_id, pic_id ):
		raise NotImplementedError( 'Derived class should override this function' )