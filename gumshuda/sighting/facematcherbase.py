class FaceMatcherBase:
    def __init__(self):
        pass

    def match(picture_id):
        """
        check if the image has a match in database
        """
        raise NotImplementedError('Derived class should override this function')

    def add_pic_to_set(p):
        """
        add image to dataset
        """
        raise NotImplementedError('Derived class should override this function')

    def add_pic_to_person(person_id, pic_id):
        """
        add the picture_id picture to person_id
        """
        raise NotImplementedError('Derived class should override this function')
