from facematcherbase import *
from .models import MissingPerson
import os.path
import sys
from projectoxford import Client

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'gumshuda'))
import config


class OxFpp(FaceMatcherBase):


    """
    Impl based on MS Project Oxford.
    https://www.projectoxford.ai/
    """
    def add_person(self, missing_person):
        """
        :type missing_person: MissingPerson
        """
        missing_person.person_group_id = missing_person.gender+"_"+str(missing_person.age)
        projectoxford.Person.Person.Create()
        pass

    def __init__(self, pic):
        FaceMatcherBase.__init__(self, pic)


    def match(self):
        """
        check if the image has a match in database
        """
        raise NotImplementedError('Derived class should override this function')

    def find_face(self):
        client = Client(config.API_KEY)
        result = client.face.detect({'stream':self.picture.data})
        if result is None or len(result) > 0:
            return False
        self.picture.face_id = result[0]['face_id']
        return True


    def add_pic_to_person(self, person_id):
        """
        add the picture_id picture to person_id
        :param person_id:
        """
        raise NotImplementedError('Derived class should override this function')

    def test(self):
        out = self.face.detect({'url': 'https://upload.wikimedia.org/wikipedia/commons/1/19/Bill_Gates_June_2015.jpg',
                                'analyzesAge': True, 'analyzesGender': True})
        print out


x = OxFpp(None)
#x.test()
