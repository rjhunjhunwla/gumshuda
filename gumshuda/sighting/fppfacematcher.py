from facematcherbase import *
import faceplusplus
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'gumshuda'))
import config


"""
Faceplusplus API based face recognition.
@see http://www.faceplusplus.com
"""


class FacePPFM(FaceMatcherBase):
    def __init__(self, data, isUrl=True):
        FaceMatcherBase.__init__(self)
        self.data = data
        self.isUrl = isUrl

    def match(self,picture_id):
        raise NotImplementedError('Not yet implemented, TODO')

    def get_current_faceset(self):
        return ""

    def get_face_id(self, json_response):
        try:
            if len(json_response['face']) == 1:
                return json_response['face'][0]['face_id']
            else:
                return None, "Multiple or no face found"
        except:
            return None, "No face found"

    def add_pic_to_set(self, p):
        api = faceplusplus.API(config.FPP_API_KEY, config.FPP_API_SECRET, config.FPP_API_HOST)
        try:
            if self.isUrl:
                fpobj = api.detection.detect(url=self.data)
            else:
                fpobj = api.detection.detect(post=True, img=self.data)
        except Exception as e:
            # handle all errors
            return False, str(e)

        if fpobj is not None:
            p.prop = fpobj
        else:
            return False, "Face detection failed"

        face_set = self.get_current_faceset()
        face_id, reason = self.get_face_id(p.prop)
        if face_id is None:
            return False, reason
        api.faceset.add_face(faceset=face_set, faceid=face_id)
        return True, face_id

    def add_pic_to_person(self, person_id, face_id):
        raise NotImplementedError('Todo')
