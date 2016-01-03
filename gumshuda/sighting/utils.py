from .models import Picture
from .models import ReportedSighting
from .models import SourcePicture
from .models import People
from .models import Sighting
import hashlib


def save_picture(data):
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
        p.save()
        return p.id, True
    return p[0].id, False


def save_person(data, user_id):
    """
    Save a person data
    """
    p = People()
    if data.has_key('name'):
        p.name = data['name']
    if data.has_key('father_name'):
        p.father_name = data['father_name']
    if data.has_key('mother_name'):
        p.mother_name = data['mother_name']
    if data.has_key('age'):
        p.age = data['age']
    if data.has_key('gender'):
        p.gender = data['gender']
    p.user = user_id
    p.save()

    return p.id


def add_source_picture(person_id, face_matcher):
    """
    add a source picture to a person
    :type face_matcher: FaceMatcherBase
    """
    if face_matcher.face_id is None:
        raise Exception('No face id found')
    pid, status = save_picture(face_matcher.data)
    if status is False:
        # TODO: At this point it should be verified if picture belongs to same person
        # if not then it seems that 2 profiles for same person is being created.
        raise Exception( "Picture already exists in record" )
    s = SourcePicture()
    s.picture_id = pid
    s.people_id = person_id
    face_matcher.person_id = person_id
    face_matcher.add_pic_to_person(person_id)
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
    r.people_id = person_id
    if reporter is not None:
        r.reporting_user_id = reporter
    else:
        r.reporting_user_id = 0
    r.save()
    return r.id


def handle_uploaded_file(request):
    if request.method == 'POST':
        s = Sighting()
        s.data = request.FILES['file'].read()
        if len(s.data) is 0:
            return None, 'No data'

        out, reason = detect_face(s.data)
        if out is False:
            return None, reason

        return s, ""


def upload(request):
    s, reason = handle_uploaded_file(request)
    if s is None:
        return HttpResponse(reason)
    f = get_facematcher(data, isUrl)
    picture_id, status = utils.save_picture(s.data)
    if status is True:
        f.match(picture_id)
    return HttpResponse(success)