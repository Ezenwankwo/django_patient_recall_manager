from django.conf.urls import url
from recall import views
from .views import CreateScheduleView, ViewScheduleView, PastRecallView, ScheduleDetailView, ScheduleUpdateView, ScheduleDeleteView, ContactView
from .views import PatientFormView, PatientListView, PatientDetailView, PatientUpdateView, PatientDeleteView


app_name = 'recall'
urlpatterns = [
	url(r'^contact/$', ContactView.as_view(), name='contact'),
	url(r'^patient_delete(?P<pk>\d+)$', PatientDeleteView.as_view(), name='patient_delete'),
	url(r'^patient_update(?P<pk>\d+)$', PatientUpdateView.as_view(), name='patient_update'),
	url(r'^patient_detail(?P<pk>\d+)$', PatientDetailView.as_view(), name='patient_detail'),
	url(r'^patient_list/$', PatientListView.as_view(), name='patient_list'),
	url(r'^add_patient/$', PatientFormView.as_view(), name='add_patient'),
	url(r'^detail_recall(?P<pk>\d+)$', ScheduleDetailView.as_view(), name='detail_recall'),
	url(r'^update_recall(?P<pk>\d+)$', ScheduleUpdateView.as_view(), name='update_recall'),
	url(r'^delete_recall(?P<pk>\d+)$', ScheduleDeleteView.as_view(), name='delete_recall'),
	url(r'^past_recall/$', PastRecallView.as_view(), name='past_recall'),
	url(r'^view_recall/$', ViewScheduleView.as_view(), name='view_recall'),
	url(r'^create_recall/$', CreateScheduleView.as_view(), name='create_recall'),
]