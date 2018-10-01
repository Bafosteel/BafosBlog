from django.conf.urls import url
from . import views

urlpatterns = [

               # indexes
               url(r'^$', views.index, name='blog_index'),
               url(r'^category/(?P<id>\d+)-(?P<slug>\w+)/$', views.category, name='blog_category'),

               # archives
               url(r'^archive/(?P<year>\d{4})/$', views.archive_year, name='blog_archive_year'),
               url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive_month, name='blog_archive_month'),
               url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.archive_day,
                   name='blog_archive_day'),

               # details
               url(r'^details/$', views.details,
                   name='blog_details'),

               # youtube
               url(r'^youtube/$', views.youtube,
                   name='blog_youtube'),

               # youtube
               url(r'^youtube/$', views.youtube_data_view,
                   name='blog_youtube'),
]
