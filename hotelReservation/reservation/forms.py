from django.forms import ModelForm
from django.contrib.auth import forms
from django.views import generic as views
from .models import Room


class ReservationForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['client']


class ReservationFormView(views.FormView):
    template_name = 'reservation/reservation_form.html'
    form_class = ReservationForm
    success_url = 'reservation/list_reservation/'


'''class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']'''


class UserFormView(views.FormView):
    template_name = 'reservation/user_form.html'
    form_class = forms.UserCreationForm
    success_url = '/reservation/reservation_form/'
