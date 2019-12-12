
# -------- DJANGO ENV ACCESS ------------
import os

try:
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sarkaricapsule.settings")
  import django
  django.setup()
except:
  print("Django Env Setup Failed!!!")
  exit()
finally:
  print('Django Env Setup Sucessful!!!')
# ---------------------------------------- 

import json
from events.models import Event, EventType, ImportantDate, ImportantLink, ImportantUpdate
from events.models import Syllabus, Result, AnswerKey, AdmitCard, Fee, Eligibility
from organizations.models import Organization
import pytz

with open('sarkari_data.json', "r") as ffile:
  file_content = ffile.read()

data = json.loads(file_content)

print("Data Length: ", len(data))

active_entries = 0
inactive_entries = 0

obj = None

for d in data:
  if d['model'] == 'sarkari.syllabus':
    
    fields = d['fields']
    tz = pytz.timezone("Asia/Calcutta")

    try:
      ev = Event.objects.get(pk=fields['event'])
    except:
      continue

    new_data = {
      "pk": d['pk'],
      "event": ev,
      "title": fields['title'],
      "description": fields['description'],
      "link": fields['link'],
      "file": fields['files'],
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = Syllabus.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()
    

  elif d['model'] == 'sarkari.results':
    # It is a event instance
    fields = d['fields']
    tz = pytz.timezone("Asia/Calcutta")

    try:
      ev = Event.objects.get(pk=fields['event'])
    except:
      continue

    new_data = {
      "pk": d['pk'],
      "event": ev,
      "title": fields['title'],
      "description": fields['description'],
      "link": fields['link'],
      "file": fields['files'],
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    if fields['type'] == 1:
      obj = Result.objects.create(**new_data)
    elif fields['type'] == 2:
      obj = AnswerKey.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()

  elif d['model'] == 'sarkari.admitcards':
    # It is a event instance
    fields = d['fields']
    tz = pytz.timezone("Asia/Calcutta")

    try:
      ev = Event.objects.get(pk=fields['event'])
    except:
      continue

    new_data = {
      "pk": d['pk'],
      "event": ev,
      "title": fields['title'],
      "link": fields['link'],
      "file": fields['files'],
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = AdmitCard.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()


  elif d['model'] == 'sarkari.fees':
    # It is a event instance
    fields = d['fields']
    tz = pytz.timezone("Asia/Calcutta")

    try:
      ev = Event.objects.get(pk=fields['event'])
    except:
      continue

    new_data = {
      "pk": d['pk'],
      "event": ev,
      "title": fields['title'],
      "amount": fields['fee'],
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = Fee.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()

  elif d['model'] == 'sarkari.eligibility':
    # It is a event instance
    fields = d['fields']
    tz = pytz.timezone("Asia/Calcutta")

    try:
      ev = Event.objects.get(pk=fields['event'])
    except:
      continue

    new_data = {
      "pk": d['pk'],
      "event": ev,
      "title": fields['title'],
      "criteria": fields['criteria'],
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = Eligibility.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()


# import code
# code.interact(local=locals())