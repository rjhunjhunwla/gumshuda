class FaceMatcherBase:
    def __init__(self, data, is_url):
        self.data = data
        self.is_url = is_url
        self.picture_id = None
        self.person_id = None
        self.face_id = None
        pass

    def match(self):
        """
        check if the image has a match in database
        """
        raise NotImplementedError('Derived class should override this function')

    def find_face(self):
        raise NotImplementedError('Derived class should override this function')
        
    def add_pic_to_person(self, person_id):
        """
        add the picture_id picture to person_id
        :returns: face_id
        """
        raise NotImplementedError('Derived class should override this function')
