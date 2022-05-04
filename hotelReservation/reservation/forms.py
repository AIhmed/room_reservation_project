from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.views import generic as views
from django.shortcuts import redirect
from reservation.models import Reservation
from django.core.exceptions import ValidationError
import datetime
import pytz


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ['client', 'price', 'end_date', 'start_date']


class ReservationFormView(views.FormView):
    template_name = 'reservation/reservation_form.html'
    form_class = ReservationForm

    def post(self, request):
        print('\n\n\n')
        print(request.user)
        print(request.POST)
        if request.method == 'POST':
            request.POST['client'] = request.user
            request.POST['start_date'] = pytz.timezone('Africa/Algiers').localize(datetime.datetime.now())
            print(request.POST)
        print('\n\n\n')
        return redirect('reservation/list_reservation/')


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, label='confirm password', error_messages={'pass2': 'you done fucking up'})

    def clean_password2(self):
        if self.field['password2'] != self.field['password']:
            raise ValidationError(self.fields['password2'].error_messages['password2'])
        return self.field['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


class UserFormView(views.FormView):
    template_name = 'reservation/user_form.html'
    form_class = UserForm

    def post(self, request):
        if request.method == 'POST':
            print(request.POST.keys())
            print(request.POST)
            if request.POST['password'] != request.POST['password2']:
                return redirect(request.META.get('HTTP_REFERER'), different_password=True)
                # redirect to the same page and add warnings
            else:
                data = request.POST
                print(data.keys())
                print(data)
                u = User(username=data['username'],
                        email=data['email'],
                        password=data['password'])
                u.save()
                return redirect('/reservation/reservation_form/')

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        print(context.keys())
        context['different_password'] = context['password'] == context['password2']
        print(context)
        return super.form_valid(form)







