from .models import Picture
from .models import ReportedSighting
from .models import SourcePicture
from .models import MissingPerson
from .models import Sighting
from oxfordaifacematcher import OxFpp
import hashlib


def find_picture(data):
    csum = hashlib.sha256(data).hexdigest()
    return Picture.objects.filter(csum=csum)


def save_picture(data, face_data):
    """
    Save a picture in database and return id,
    :param data: picture data
    :return: True if picture was not seen earlier
             False if picture already exists
    """
    csum = hashlib.sha256(data).hexdigest()
    p = Picture.objects.filter(csum=csum)
    if not p:
        p = Picture()
        p.csum = csum
        p.data = data
        p.prop = face_data
        p.save()
        return p.id, True
    return p[0].id, False


def save_person(data, user_id):
    """
    Save a person data
    """
    p = MissingPerson()

    if data.has_key('name'):
        p.name = data['name']
    else:
        raise KeyError("Missing Name of missing person")
    if data.has_key('father_name'):
        p.father_name = data['father_name']
    if data.has_key('mother_name'):
        p.mother_name = data['mother_name']
    if data.has_key('age'):
        p.age = data['age']
    else:
        raise KeyError("Missing age of missing person")
    if data.has_key('gender'):
        p.gender = data['gender']
    else:
        raise KeyError("Missing gender of missing person")
    p.user = user_id

    p.save()

    return p.id


def add_source_picture(missing_person_id, face_matcher):
    """
    add a source picture to a person
    :type face_matcher: FaceMatcherBase
    """
    if face_matcher.face_id is None:
        raise Exception('No face id found')
    pid, status = save_picture(face_matcher.data, face_matcher.face_data())
    if status is False:
        # TODO: At this point it should be verified if picture belongs to same person
        # if not then it seems that 2 profiles for same person is being created.
        raise Exception("Picture already exists in record")
    s = SourcePicture()
    s.picture_id = pid
    s.missing_person_id = missing_person_id
    face_matcher.person_id = missing_person_id
    face_matcher.add_pic_to_person(missing_person_id)
    s.face_id = face_matcher.face_id
    s.save()


def check_if_picture_in_db(data):
    """
    data is a picture, check if the person is in  missing/found database.
    :param data: data is picture data
    :return: picture id if found, none otherwise
    """
    csum = hashlib.sha256(data).hexdigest()
    f = Picture.objects.filter(csum=csum)
    if f:
        return f[id]
    return None


def update_sighting_for_person(seen_pic_id, person_id, reporter):
    """
    update that a person was reported by user exists in database
    """
    r = ReportedSighting()
    r.picture_id = seen_pic_id
    r.missing_person_id = person_id
    if reporter is not None:
        r.reporting_user_id = reporter
    else:
        r.reporting_user_id = 0
    r.save()
    return r.id


def get_matcher(data):
    return OxFpp(data)


def handle_uploaded_file(data):
    p = find_picture(data)
    if p is not None:
        raise Exception("This picture already exists and has been checked")
    face_matcher = get_matcher(p)
    if face_matcher.find_face() is True and face_matcher.picture.face_id is not None:
        return face_matcher
    else:
        raise Exception("No face found")



def get_face_ids_for_missing_person_from_db(person_id):
    """
    return all face_ids associated with person as stored in local db.
    :param person_id: missing person id.
    :return: array of face ids.
    """
    return SourcePicture.objects.filter(missing_person_id=person_id).value_list('face_id', flat=True)