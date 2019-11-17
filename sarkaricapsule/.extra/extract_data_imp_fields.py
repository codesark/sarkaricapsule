
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
  if d['model'] == 'sarkari.impdates':
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
      "date": fields['date'],
      "description": fields['description'],
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = ImportantDate.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()
    

  elif d['model'] == 'sarkari.impupdates':
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
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = ImportantUpdate.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()

  elif d['model'] == 'sarkari.implinks':
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
      "created_at": fields['date_added'],
      "modified_at": fields['date_modified']  
    }

    obj = ImportantLink.objects.create(**new_data)

    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()

# import code
# code.interact(local=locals())