from .models import picture
from .models import reported_sighting
import hashlib

"""
Save a picture in database and return id,
return True if picture was not seen earlier
retrun False if picture already exists
"""
def save_picture( data ):
    csum = hashlib.sha256(data).hexdigest()
    p = picture.objects.filter(csum=csum)
    if not p:
        p =picture()
        p.csum = csum
        p.data = data
        p.save()
        return p.id,True
    return p[0].id,False

"""
Save a person data
"""
def save_person( data ):
    return None

"""

"""
def add_source_picture( data, person_id ):
    pid,status = save_picture( data )
    if status is False:
        return "Picture already exists in record", False
    s = source_picture()
    s.picture_id = pid
    s.people_id  = person_id
    s.save()
    return "Success",True


"""
data is a picture, check if the person is in  missing/found database.
"""
def check_if_person_missing( data ):
    return None:

"""
update that a person was reported by user exists in database
"""
def update_sighthing_for_person( seen_pic_id, person_id ):
    r = reported_sighting()
    r.picture_id = seen_pic_id
    r.people_id = person_id
    r.save()
    return r.id
