# -*- coding: utf-8 -*-
from contacts.models import contact
from contacts.forms import ContactForm
from django.views.generic import ListView

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

class PostsListView(ListView): # представление в виде списка
    model = contact                   # модель для представления

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			
			recipients = ['antoshinas@gmail.com']
			try:
				send_mail(subject, message, 'admin@ecologist.myjino.ru', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'contact_list.html', {'form': form, 'object_list' : contact.objects.all()})