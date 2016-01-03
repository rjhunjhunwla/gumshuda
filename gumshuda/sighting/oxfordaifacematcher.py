from projectoxford import Face
from facematcherbase import *
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'gumshuda'))
import config


class OxFpp( FaceMatcherBase ):
    def __init__(self, data, is_url):
        FaceMatcherBase.__init__(self, data, is_url)
        self.face = Face.Face(config.PROJECT_OXFORD_FACE_API_KEY)

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
        :param person_id:
        """
        raise NotImplementedError('Derived class should override this function')

    def test(self):
        out = self.face.detect({'url': 'https://upload.wikimedia.org/wikipedia/commons/1/19/Bill_Gates_June_2015.jpg',
                          'analyzesAge':True, 'analyzesGender':True})
        print out

x = OxFpp(None,False)
x.test()