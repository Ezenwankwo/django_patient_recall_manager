from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import date 
from django.core.exceptions import ValidationError


# Create your models here.

class Schedule(models.Model):
	card_number = models.CharField("Patient ID", max_length=30, help_text="Registration or Card Number", blank=False)
	patient = models.CharField("Patient Name", max_length=50, help_text="Surname  Firstname  Othername", blank=False)
	date_of_visit = models.DateField("Date of Visit", help_text="YYYY-MM-DD", blank=False)
	summary_of_visit = models.TextField("Summary of Visit", max_length=500, blank=True)
	date_of_recall = models.DateField("Date of Recall", help_text="YYYY-MM-DD", blank=False)
	reason_for_recall = models.TextField("Reason for Recall", max_length=200, blank=True)

	RECALL_STATUS = (
		('On Schedule', 'On Schedule'),
		('A Reminder', 'A Reminder'),
	)

	recall_status = models.CharField("Recall Status", max_length=15, choices=RECALL_STATUS, blank=True, default='On Schedule')
	phone_number = models.CharField(max_length=30, blank=False)




	class Meta:
		ordering = ['date_of_recall']
		

	def __str__(self):
		return self.card_number

	def get_absolute_url(self):
		return reverse('recall:detail_recall', kwargs={'pk': self.pk})

	def clean(self):
		date_of_recall = self.date_of_recall

		if date_of_recall < date.today():
			raise ValidationError('You cannot schedule a recall for the past. Please check your date')


	
	def is_past_due(self):
		return date.today() <= self.date_of_recall

	def new_recall_date(self):
		return date.today() > self.date_of_recall

	

	

