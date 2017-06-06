from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy 
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from recall.models import Schedule
from recall.forms import ContactForm




class CreateScheduleView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    #Powers a form to create a new recall

	model = Schedule
	template_name = 'recall/create_recall.html'
	fields = ['card_number', 'patient', 'date_of_visit', 'summary_of_visit', 'date_of_recall', 'reason_for_recall', 'recall_status', 'phone_number']
	success_url = reverse_lazy('recall:create_recall')
	success_message = 'Recall successfully created'


class ViewScheduleView(LoginRequiredMixin, ListView):

	#Shows users a list of appointments

	model = Schedule
	template_name = 'recall/view_recall.html'
	context_object_name = 'view_recall' 
	#paginate_by = 5


	def get_queryset(self, *args, **kwargs):
		queryset_list = Schedule.objects.all()
		query = self.request.GET.get("q")
		
		if query:
			queryset_list = queryset_list.filter(
				Q(card_number__icontains=query)|
				Q(patient__icontains=query)
				).distinct()
		return queryset_list


	
class ScheduleDetailView(DetailView):

	#Shows users a single appointment

	model = Schedule
	template_name = 'recall/detail_recall.html'
	context_object_name = 'schedule'

class ScheduleUpdateView(SuccessMessageMixin, UpdateView):
	#powers a form to edit existing recall

	model = Schedule
	template_name = 'recall/schedule_form.html'
	fields = ['card_number', 'patient', 'date_of_visit', 'summary_of_visit', 'date_of_recall', 'reason_for_recall', 'recall_status', 'phone_number']
	success_url = reverse_lazy('recall:view_recall')
	success_message = 'Recall successfully updated'



class ScheduleDeleteView(SuccessMessageMixin, DeleteView):
	#prompts user to confirm deletion of a recall

	model = Schedule
	success_url = reverse_lazy('recall:view_recall')



class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'


    def form_valid(self, form):
        contact_name = self.form.cleaned_data['contact_name']
        contact_email = self.form.cleaned_data['contact_email']
        form_content = self.form.cleaned_data['content']

        template = get_template('contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content
        })
        content = template.render(context)

        email = EmailMessage(
            'New contact form submission',
            content,
            'Your website ' + '',
            ['youremail@gmail.com'],
            headers = {'Reply-To': contact_email}
        )
        email.send()
        return super(ContactView, self).form_valid(form)

