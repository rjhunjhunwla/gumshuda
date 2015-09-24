class FaceMatcherBase:
    def __init__(self):
        pass

    def match(self, picture_id):
        """
        check if the image has a match in database
        """
        raise NotImplementedError('Derived class should override this function')

    def get_face_id(self, pic_data):
        raise NotImplementedError('Derived class should override this function')
        
    def add_pic_to_person(self, person_id, pic_id):
        """
        add the picture_id picture to person_id
        """
        raise NotImplementedError('Derived class should override this function')
