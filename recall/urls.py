from django.conf.urls import url
from recall import views
from .views import CreateScheduleView, ViewScheduleView, ScheduleDetailView, ScheduleUpdateView, ScheduleDeleteView, ContactView

app_name = 'recall'
urlpatterns = [
	url(r'^detail_recall(?P<pk>\d+)$', ScheduleDetailView.as_view(), name='detail_recall'),
	url(r'^update_recall(?P<pk>\d+)$', ScheduleUpdateView.as_view(), name='update_recall'),
	url(r'^delete_recall(?P<pk>\d+)$', ScheduleDeleteView.as_view(), name='delete_recall'),
	url(r'^view_recall/$', ViewScheduleView.as_view(), name='view_recall'),
	url(r'^create_recall/$', CreateScheduleView.as_view(), name='create_recall'),
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),
]