from .models import Picture
from .models import ReportedSighting
from .models import SourcePicture
import hashlib


def save_picture(data):
    """
    Save a picture in database and return id,
    return True if picture was not seen earlier
    retrun False if picture already exists
    """
    csum = hashlib.sha256(data).hexdigest()
    p = Picture.objects.filter(csum=csum)
    if not p:
        p = Picture()
        p.csum = csum
        p.data = data
        p.save()
        return p.id, True
    return p[0].id, False


def save_person(data):
    """
    Save a person data
    """
    p = person()
    if data.has_key('name'):
        p.name = data['name']
    if data.has_key('father_name'):
        p.father_name = data['father_name']
    if data.has_key('mother_name'):
        p.mother_name = data['mother_name']
    if data.has_key('age'):
        p.age = data['age']
    p.save()

    return p.id


def add_source_picture(data, person_id):
    """
    add a source picture to a person
    """
    pid, status = save_picture(data)
    if status is False:
        return "Picture already exists in record", False
    s = SourcePicture()
    s.picture_id = pid
    s.people_id = person_id
    s.save()
    return "Success", True


def check_if_person_in_db(data):
    """
    data is a picture, check if the person is in  missing/found database.
    """
    csum = hashlib.sha256(data).hexdigest()
    f = Picture.objects.filter(csum=csum)
    if not f:
        return f[id]

    # If csum is not matching, go and do face recognition.
    # TODO: Implement face recognition
    return None


def update_sighthing_for_person(seen_pic_id, person_id):
    """
    update that a person was reported by user exists in database
    """
    r = ReportedSighting()
    r.picture_id = seen_pic_id
    r.people_id = person_id
    r.save()
    return r.id
