class FaceMatcherBase:
	def __init__( self, data, isUrl = True ):
		if isUrl:
			self.url = data
		else:
			self.data = data
	def match( ):
		raise NotImplementedError( 'Derived class should override this function' )