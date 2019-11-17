from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event
from django.apps import apps
from django.core.paginator import Paginator

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['events:home',]

    def location(self, item):
        return reverse(item)


class AllDetailSiteMap(Sitemap):
  changefreq = "daily"
  priority = 0.5

  def items(self):
    object_list = []

    for list_type in ['job', 'admission', 'scholarship']:
      # list_type = str(list_type)
      ev = Event.objects.filter(is_active=True, event_type__name=(list_type.capitalize())).order_by('-modified_at')
      object_list.append({'field': list_type,'data': ev})

    for list_type in ['result', 'answerkey', 'admitcard',
                      'syllabus', 'importantdate', 'importantupdate' ]:
      Model = apps.get_model('events', model_name=list_type)
      oblist = Model.objects.filter(event__is_active=True).distinct('event__pk').order_by('event__pk', '-modified_at')
      # get event from objects
      events = []
      for i in oblist:
        i.event.title = i.event.title + " : " +  i.title
        events.append(i.event)
        
      object_list.append({'field': list_type,'data': events})
    
    final_list = []

    for i in object_list:
      for j in i['data']:
        j.vacancy_details = i['field']
        final_list.append(j)

    return final_list

  def location(self, obj):    
    return reverse( 'events:detail', kwargs={'listtype':obj.vacancy_details, 'pk':obj.pk, 'slug':obj.slug}) 


class AllListSiteMap(Sitemap):
  changefreq = "daily"
  priority = 0.5

  def items(self):
    object_list = []

    for list_type in ['job', 'admission', 'scholarship']:
      events = Paginator(Event.objects.filter(is_active=True).order_by('-modified_at'), 20)
      for i in range(events.num_pages):
        object_list.append({'list_type': list_type, 'pageno': i + 1})

    for list_type in ['result', 'answerkey', 'admitcard',
                      'syllabus', 'importantdate', 'importantupdate' ]:
      Model = apps.get_model('events', model_name=list_type)
      oblist = Model.objects.filter(event__is_active=True).distinct('event__pk').order_by('event__pk','-modified_at')
      events = Paginator(oblist, 20)
      
      for i in range(events.num_pages):
        object_list.append({'list_type': list_type, 'pageno': i + 1})
    
    return object_list

  def location(self, obj):
    return reverse( 'events:list', kwargs={ 'listtype': obj['list_type'], 'pageno': obj['pageno'] })