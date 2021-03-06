class FaceMatcherBase:
    def __init__(self, picture):
        self.picture = picture
        self.person = None
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

    def add_person(self, missing_person):
        """
        Add a missing person to matcher core DB
        :param missing_person:
        :return:
        """
        raise NotImplementedError("Derived class should override this function")
