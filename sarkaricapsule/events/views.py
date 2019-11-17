from django.utils.timezone import timezone
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Event
from django.apps import apps
from django.http import Http404
from django.core.paginator import Paginator

# -- class to get unique events
class UniqueEvent:

  @staticmethod
  def get(objs):
    prev = None
    uobjs = []
    for obj in objs:
      if prev is not None:
        if prev.event.id == obj.event.id:
          continue
      uobjs.append(obj)
      prev = obj
    return uobjs


# Home View

class HomeView(View):

  def get(self, request, *args, **kwargs):

    object_list = {}

    for list_type in ['job', 'admission', 'scholarship']:
      # list_type = str(list_type)
      object_list[list_type] = Event.objects.filter(is_active=True, event_type__name=(list_type.capitalize())).order_by('-modified_at')[:10]
      
      for ob in object_list[list_type]:
        ob.recently_added = ob.is_recently_added
        ob.recently_updated = ob.is_recently_updated

    for list_type in ['result', 'answerkey', 'admitcard',
                      'syllabus', 'importantdate', 'importantupdate' ]:
      Model = apps.get_model('events', model_name=list_type)
      oblist = Model.objects.filter(event__is_active=True).distinct('event__id').order_by('-event__id', '-modified_at')[:10]
      oblist = Model.objects.filter(event__is_active=True).order_by('-modified_at')[:30]
      oblist = UniqueEvent.get(oblist)

      # get event from objects
      events = []
      for i in oblist:
        i.event.title = i.event.title + " : " +  i.title
        i.event.recently_added = i.is_recently_added()
        i.event.recently_updated = i.is_recently_updated()
        events.append(i.event)
        
      object_list[list_type] = events

    return render(request, 'events/home.html', {
      
      'combined_object_list': object_list,

      # 'title': 'Sarkari Capsule',
      # (IMPORTANT): all views should contain these fields in their context (SEO FIELDS)
      'page_title': "Sarkari Result | Get Latest Govt Jobs, Result, Admission, Admit Card Alerts | SarkariResults | Sarkari Capsule",
      'meta_key': "Sarkari Capsule, Sarkari Result, sarkari Jobs, Sarkari Exams, Sarkari Jobs, Sarkari Naukari,Sarkariresult, job, admission, scholarship, admit Card, result, syllabus, best job portals in india, best job search sites in india, best job sites in india,india job portal, top job sites in india",
      'meta_desc': """ Sarkari Capsule Provides information of all the Sarkari Results,Sarkari Result 2019, Sarkari Naukri Job 2019, SarkariResult.com, Sarkari Jobs, Sarkari Exams, Admit Cards, Answer Keys . Sarkari Capsule Provides all the latest information of Railway, Bank, SSC, Army, Navy, Police, UPPSC, UPSSSC, and more Sarkari Jobs alert at one place. We Provides Information of sarkari result
        sarkari results, sarkariresult,sarkari result com, sarkari result. com, sarkari result 2019, sarkari result hindi, sarkari result info,sarkari naukri result, sarkari result 10th 2019, sarkari result exam, sarkari result bihar, sarkari result in bihar, sarkari result group d, sarkari result up board, sarkari result 12th 2019, sarkari result up, sarkari result ccc, sarkari result sarkari result, sarkari result ssc gd,sarkari result job,sarkari result iti
        sarkari result latest, sarkari result rpf, sarkari result up police, sarkari result result, sarkari result live, sarkari result alp,sarkari result 10th, sarkari result upp,sarkari result online,sarkari result information,sarkari result 2019 up board, sarkari result find, sarkari result ntpc,sarkari result railway, sarkari result 2019 10th, sarkari result rrb, sarkari result ssc, sarkari result 12th, sarkari result new,sarkari result mp, sarkari result polytechnic, sarkari result upsc, sarkari result upsssc, sarkari result matric, sarkari result 10th result 2018, sarkari result 12th 2018, sarkari result up board 2018,sarkari result high school 2019, sarkari result 2019 latest job, sarkari result answer key, sarkari result airforce,sarkari result rajasthan, sarkari result ctet, sarkari result hssc, sarkari result vdo, sarkari result nda, sarkari result ba, sarkari result download, sarkari result offline, sarkari result website, sarkari result cisf, sarkari result in hindi 2019, etc
    """ ,

    })

  def post(self, request, *args, **kwargs):
    pass


#  --------------- UNIVERSAL VIEW CLASS --------

# -- Universal List View

class UniversalListView(View):

  def get(self, request, *args, **kwargs):
    # print(self)
    # print("request", request)
    # print("Args:", args)
    # print("KWargs:", kwargs)

    list_type = kwargs['listtype']
    try: 
      page_no = kwargs['pageno']
    except KeyError:
      page_no = 1
    
    if list_type in [ 'job', 'admission', 'scholarship']:
      # load event model  
      Event = apps.get_model('events', model_name='event')
      events = Event.objects.filter(is_active=True, event_type__name=list_type.capitalize())[:300]
      
    elif list_type in [  'result', 'answerkey', 'admitcard',
                      'syllabus', 'importantdate', 'importantupdate' ]:
      # load specified model
      Model = apps.get_model('events', model_name=list_type)
      oblist = Model.objects.filter(event__is_active=True).order_by('-modified_at')[:300]
      oblist = UniqueEvent.get(oblist)
      # get event from objects
      events = []
      for i in oblist:
        events.append(i.event)
    else:
      raise Http404


    pagination = Paginator(events, 20)
    event_list = pagination.get_page(page_no)
    

    #TODO ## find a better way
    # --- get page name 
    page_name = list_type.lower()
    if 'important' in page_name:
      page_name = str(page_name).split('important')
      page_name = 'important' + page_name[1]
    elif page_name.find('admitcard') != -1:
      page_name = 'admit card'
    elif page_name.find('answerkey') != -1:
      page_name = 'answer key'
    # --------

    return render(request, 'events/list.html', {
      'title': list_type.capitalize(),
      'list_type': list_type,
      'events': event_list,

      'pagename': page_name.capitalize(),

      # (IMPORTANT): all views should contain these fields in their context (SEO FIELDS)
      'page_title': "Sarkari Result 2019 | Get Latest Govt Jobs, Result, Admission, Admit Card Alerts | SarkariResults | Sarkari Capsule",
      'meta_key': "Sarkari Capsule, Sarkari Result, Sarkari Exams, Sarkari Jobs, Sarkari Naukari,Sarkariresult, job, admission, scholarship, admit Card, result, syllabus, best job portals in india, best job search sites in india, best job sites in india,india job portal, top job sites in india",
      'meta_desc': "Sarkari Capsule Provides information of all the Sarkari Results, Sarkari Jobs, Sarkari Exams, Admit Cards, Answer Keys . Sarkari Capsule Provides all the latest information of Railway, Bank, SSC, Army, Navy, Police, UPPSC, UPSSSC and more Sarkari Jobs alert at one place. ",
      
    })

  def post(self, request, *args, **kwargs):
    raise Http404


class UniversalDetailView(View):

  def get(self, request, *args, **kwargs):
    
    try:
      list_type = kwargs['listtype']
      slug = kwargs['slug']
      pk = kwargs['pk']
    except:
      raise Http404
    
    if list_type in [ 'job', 'admission', 'scholarship',
                      'result', 'answerkey', 'admitcard',
                      'syllabus', 'importantdate', 'importantupdate' ]:

      try:
        # Model = apps.get_model('events', model_name=list_type)
        event = Event.objects.get(pk=pk, is_active=True, slug=slug)
        # event = obj.event.get(pk=pk)
      except:
        raise Http404("Event Not found!")
        
      # --- get page name 
      page_name = list_type
      if 'important' in page_name:
        page_name = str(page_name).partition('important')
        page_name = 'important' + page_name[2]
      elif page_name.find('admitcard') != -1:
        page_name = 'admit card'
      elif page_name.find('answerkey') != -1:
        page_name = 'answer key'
      # --------

      return render(request, 'events/detail.html', {
        'title': event.page_title,
        'list_type': list_type,
        'event': event,

        'pagename': page_name.capitalize(),

        # (IMPORTANT): all views should contain these fields in their context (SEO FIELDS)
        'page_title':  event.title,
        'meta_key': "Sarkari Capsule, Sarkari Result, Sarkari Exams, Sarkari Jobs, Sarkari Naukari,Sarkariresult, job, admission, scholarship, admit Card, result, syllabus, best job portals in india, best job search sites in india, best job sites in india,india job portal, top job sites in india",
        'meta_desc':"Sarkari Capsule Provides information of all the Sarkari Results, Sarkari Jobs, Sarkari Exams, Admit Cards, Answer Keys . Sarkari Capsule Provides all the latest information of Railway, Bank, SSC, Army, Navy, Police, UPPSC, UPSSSC and more Sarkari Jobs alert at one place. ",
      
      })

    else:
      raise Http404("Not in List_Type!")

    def post(self, request, *args, **kwargs):
      pass

# custom error handling
def customhandler404(request, exception=None):
    response = render(request, 'events/error.html', { 'error_code': 404})
    response.status_code = 404
    return response

def customhandler403(request, exception=None):
    response = render(request, 'events/error.html', { 'error_code': 403})
    response.status_code = 404
    return response

def customhandler400(request, exception=None):
    response = render(request, 'events/error.html', { 'error_code': 400})
    response.status_code = 404
    return response

def customhandler500(request, exception=None):
    response = render(request, 'events/error.html', { 'error_code': 500})
    response.status_code = 404
    return response




# # Royal Rajwade

# def royal(request):
#   return render(request, 'royal.html', {})