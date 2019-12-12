from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from events import feeds as EventFeeds
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admindash/', admin.site.urls),
    path('texteditor/', include('django_summernote.urls')),
    path('api/', GraphQLView.as_view(graphiql=True), name="api"),

    # always keep it at last
    path('', include('events.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# ----- Error hadler page configuration --------
handler404 = 'events.views.customhandler404'
handler500 = 'events.views.customhandler500'
handler403 = 'events.views.customhandler403'
#  ----------------- END ----------------------
