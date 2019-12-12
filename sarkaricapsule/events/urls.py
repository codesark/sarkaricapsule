
from django.contrib.sitemaps.views import sitemap
from django.urls import path
# from django.http import request
from django.utils.text import capfirst

from events.feeds import (LatestAdmissionFeed, LatestAllFeed, LatestJobsFeed,
                          LatestScholarshipFeed)
from events.sitemaps import (StaticViewSitemap, AllListSiteMap, AllDetailSiteMap)
from events.views import (HomeView, UniversalListView, UniversalDetailView)


# from events.views import royal

sitemaps = {
    'static': StaticViewSitemap,
    'allList': AllListSiteMap,
    'allDetail': AllDetailSiteMap
}


app_name = 'events'

urlpatterns = [
  # Home View
  path('', HomeView.as_view(), name="home"),

  # path('rajwadae/', royal, name="royal"), 
  # path('royal/', royal, name="royal"),  

  # RSS Feed
  path('rss/', LatestAllFeed()),
  path('rss/job/', LatestJobsFeed()),
  path('rss/admission/', LatestAdmissionFeed()),
  path('rss/scholarship', LatestScholarshipFeed()),
  
  # Sitemap
  path('sitemap.xml', sitemap, { 'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

  # Core Views
  path('', HomeView.as_view(), name='Home'),
  path('<listtype>/', UniversalListView.as_view(), name='list'),
  path('<listtype>/<int:pageno>/', UniversalListView.as_view(), name='list'),
  path('<listtype>/<slug>-<int:pk>/', UniversalDetailView.as_view(), name='detail'),
  path('<listtype>/<slug>-<int:pk>-<int:relpk>/', UniversalDetailView.as_view(), name='detail'),
]
