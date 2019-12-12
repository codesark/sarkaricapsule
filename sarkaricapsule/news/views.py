from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .models import News


class NewsHome(View):

    def get(self, request, *args, **kwargs):
        
        news = News.objects.all()
        
        return render(request, 'news/index.html', {
            'news': news
        })
