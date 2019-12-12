from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Event
from django.utils.html import strip_tags, escape
# from django.utils.text import slugify

class LatestJobsFeed(Feed):
    title = "Sarkari Capsule Job Feed"
    link = '/jobs/'
    description = "Latest Government Job Alert"

    def items(self):
        return Event.objects.filter(is_active=True, event_type__name='Job').order_by('-modified_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.description)

class LatestAdmissionFeed(Feed):
    title = "Sarkari Capsule Admission Feed"
    link = '/admissions/'
    description = "Latest Government Job Alert"

    def items(self):
        return Event.objects.filter(is_active=True, event_type__name='Admission').order_by('-modified_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.description)

class LatestScholarshipFeed(Feed):
    title = "Sarkari Capsule Scholarship Feed"
    link = '/scholarships/'
    description = "Latest Government Job Alert"

    def items(self):
        return Event.objects.filter(is_active=True, event_type__name='Scholarship').order_by('-modified_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.description)

class LatestAllFeed(Feed):
    title = "Sarkari Capsule Latest Feed"
    link = '/'
    description = "Latest Government Job Alert"

    def items(self):
      total_list = []
      jobs = Event.objects.filter(is_active=True, event_type__name='Job').order_by('-modified_at')[:60]
      for i in jobs:
        total_list.append({ 'title': i.title, 'description': i.description, 'link': reverse('events:detail', kwargs={'listtype': 'job', 'slug': i.slug, 'pk':i.pk})})  
      admisions = Event.objects.filter(is_active=True, event_type__name='Admission').order_by('-modified_at')[:40]
      for i in admisions:
        total_list.append({ 'title': i.title, 'description': i.description, 'link': reverse('events:detail', kwargs={'listtype': 'admission', 'slug': i.slug, 'pk':i.pk})})      
      scholarships = Event.objects.filter(is_active=True, event_type__name='Scholarship').order_by('-modified_at')[:40]
      for i in scholarships:
        total_list.append({ 'title': i.title, 'description': i.description, 'link': reverse('events:detail', kwargs={'listtype': 'scholarship', 'slug': i.slug, 'pk':i.pk})})
      print(len(total_list))
      return total_list

    def item_title(self, item):
        return item['title']

    def item_description(self, item):
        return strip_tags(item['description'])

    def item_link(self, item):
      return item['link']