from facematcherbase import *
from .models import MissingPerson
import os.path
import sys
import requests

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'gumshuda'))
import config


class OxFpp(FaceMatcherBase):

    def get_request_header(self):
        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = ''
        headers['Content-Type'] = 'application/json'
        return headers
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
        url = "https://api.projectoxford.ai/face/v1.0/detect"
        params = { 'returnFaceAttributes': 'age,gender', 'returnFaceLandmarks': 'true'}
        response = requests.request('post', url, data=self.picture.data, headers=self.get_request_header(), params=params)
        if response.status_code == 429:
            print "Message: %s" % ( response.json()['error']['message'] )

        if retries <= _maxNumRetries:
            time.sleep(1)
            retries += 1
            continue
        else:
            print 'Error: failed after retrying!'
            break
        elif response.status_code == 200 or response.status_code == 201:

        if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
            result = None
        elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
            if 'application/json' in response.headers['content-type'].lower():
                result = response.json() if response.content else None
            elif 'image' in response.headers['content-type'].lower():
                result = response.content
        else:
            print "Error code: %d" % ( response.status_code )
            print "Message: %s" % ( response.json()['error']['message'] )
        
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
