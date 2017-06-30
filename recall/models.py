from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import date 
from django.core.exceptions import ValidationError


# Create your models here.

class Patient(models.Model):
	card_number = models.CharField("Card Number", unique=True, max_length=30, blank=False)
	patient_name = models.CharField("Patient Name", max_length=50, help_text="Title Surname Firstname", blank=False)
	sex = (
		('Male', 'Male'),
		('Female', 'Female'),
	)

	sex = models.CharField("Sex", max_length=7, choices=sex, blank=False)
	date_of_birth = models.DateField("Date of Birth", help_text="Please use the following format: <em>YYYY-MM-DD</em>", blank=True)
	phone_number = models.CharField("Phone Number", max_length=30, blank=False)
	email = models.EmailField("Email", max_length=50, blank=True)
	address = models.CharField("Address", max_length=100, blank=True)
	occupation = models.CharField("Occupation", max_length=50, blank=True)
	hmo = models.CharField("HMO", max_length=100, help_text="Name of HMO(HMO ID Number)", blank=True)


	class Meta:
		ordering = ['card_number']

	def __str__(self):
		return self.patient_name

	def get_absolute_url(self):
		return reverse('recall:patient_detail', kwargs={'pk': self.pk})



class Schedule(models.Model):
	patient = models.CharField("Patient Name", max_length=50, help_text="Title Surname Firstname", blank=False)
	date_of_visit = models.DateField("Date of Visit", help_text="Please use the following format: <em>YYYY-MM-DD</em>", blank=False)
	summary_of_visit = models.TextField("Summary of Visit", max_length=500, blank=True)
	date_of_recall = models.DateField("Date of Recall", help_text="Please use the following format: <em>YYYY-MM-DD</em>", blank=False)
	reason_for_recall = models.TextField("Reason for Recall", max_length=200, blank=True)

	RECALL_STATUS = (
		('On Schedule', 'On Schedule'),
		('A Reminder', 'A Reminder'),
	)

	recall_status = models.CharField("Recall Status", max_length=15, choices=RECALL_STATUS, blank=True, default='On Schedule')




	class Meta:
		ordering = ['date_of_recall']
		

	def __str__(self):
		return self.patient

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

	

	

