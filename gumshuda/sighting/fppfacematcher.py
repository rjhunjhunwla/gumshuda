from facematcherbase import *
import faceplusplus
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'gumshuda'))
import config


class FacePPFM(FaceMatcherBase):
    """
    Faceplusplus API based face recognition.
    @see http://www.faceplusplus.com
    """
    def __init__(self, data, is_url):
        FaceMatcherBase.__init__(self, data, is_url)
        self.api = faceplusplus.API(config.FPP_API_KEY, config.FPP_API_SECRET, config.FPP_API_HOST)

    def match(self):
        raise NotImplementedError('Not yet implemented, TODO')

    def get_current_faceset(self):
        return ""

    @staticmethod
    def get_face_id(json_response):
        try:
            if len(json_response['face']) == 1:
                return json_response['face'][0]['face_id']
            else:
                return None, "Multiple or no face found"
        except:
            return None, "No face found"

    def add_pic_to_set(self):
        status, reason = self.find_face()
        if status is False:
            return False, reason

        face_set = self.get_current_faceset()
        self.api.faceset.add_face(faceset=face_set, faceid=self.face_id)
        return True, "Success"

    def add_pic_to_person(self, person_id):
        self.person_id = person_id
        status, reason = self.add_pic_to_set()
        if status is False:
            return status, reason
        try:
            out = self.api.person.add_face(face_id=self.face_id, person=person_id)
        except:
            return False, out
        return True, "Success"

    def find_face(self):
        try:
            if self.isUrl:
                fpobj = self.api.detection.detect(url=self.data)
            else:
                fpobj = self.api.detection.detect(post=True, img=self.data)
        except Exception as e:
            # handle all errors
            return False, str(e)
        self.face_id = FacePPFM.get_face_id(fpobj)
        if self.face_id is None:
            return False, "No face found"
        return True, "Success"
