
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
from events.models import Event, EventType
from organizations.models import Organization
import pytz
from django.utils.text import slugify
with open('sarkari_data.json', "r") as ffile:
  file_content = ffile.read()

data = json.loads(file_content)

print("Data Length: ",len(data))

active_entries = 0
inactive_entries = 0

obj = None

for d in data:
  if d['model'] == 'sarkari.events':
    # It is a event instance
    
    fields = d['fields']
    if fields['active'] == False:
      print("Inactive Entry Ignoring!!")
      inactive_entries += 1
      continue
    else:
      active_entries += 1

    new_data = {}

    tz = pytz.timezone("Asia/Calcutta")
    
    new_data['pk'] = d['pk']
    new_data['event_type'] = EventType.objects.get(pk=fields['type'])
    new_data['title'] = fields['title']
    new_data['page_title'] = fields['title']
    new_data['slug'] = slugify(fields['title'])
    new_data['is_active'] = fields['active']
    new_data['description'] = fields['description']
    new_data['vacancy_details'] = fields['vacancy']
    new_data['payment_method'] = fields['pmode']
    new_data['created_at'] = fields['date_modified']
    new_data['modified_at'] = fields['date_modified']

    orgs = Organization.objects.filter(name__startswith=fields['org'])

    if len(orgs) == 0:
      # create organisation
      org = Organization.objects.create(name=fields['org'])
    else:
      # get organisation
      org = orgs[0]
    
    # org = org.save()

    new_data['organization'] = org  

    obj = Event.objects.create(**new_data)
    
    obj.created_at.replace(tzinfo=tz)
    obj.modified_at.replace(tzinfo=tz)

    obj.save()




import code
code.interact(local=locals())