import json

import httplib2
from django.contrib.sites.models import Site
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from oauth2client.service_account import ServiceAccountCredentials

from core.utils import generate_random_string
from .models import Event

@receiver(post_save, sender=Event)
def send_to_google_indexing_api(sender, instance, created, **kwargs):
  try:
    if instance.is_active and instance.event_type.name == "Job":
      content = json.dumps({
        'url': "https://" + str(Site.objects.get_current()) + instance.get_absolute_url(),
        'type': "URL_UPDATED"
      })
    
      SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
      ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
      JSON_KEY_FILE = "json/google_indexing_api_key.json"

      credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
      http = credentials.authorize(httplib2.Http())
      response, content = http.request(ENDPOINT, method="POST", body=content)
      print(vars(response))
    else:
      print("Event added but not pinged to google!")

  except:
    print("Error while sending request to google indexing api")


@receiver(pre_save, sender=Event)
def add_slug_to_event(sender, instance, *args, **kwargs):
  if instance and not instance.slug:
    slug = slugify(instance.page_title)
    random_string = generate_random_string()
    instance.slug = slug + "-" + random_string
