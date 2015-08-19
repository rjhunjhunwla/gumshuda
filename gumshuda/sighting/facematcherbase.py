class FaceMatcherBase:
	def __init__( self, data, isUrl = True ):
		self.isUrl = isUrl
		self.data = data

	"""
	check if the image has a match in database 
	"""
	def match( ):
		raise NotImplementedError( 'Derived class should override this function' )

	"""
	add image to dataset
	"""
	def add_pic_to_set( p ):
		raise NotImplementedError( 'Derived class should override this function' )