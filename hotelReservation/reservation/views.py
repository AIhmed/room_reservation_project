from django.views import generic as views
from .models import Room, Reservation

# views take a request as arg and return a responce

# redirection from filling a form
# redirection to a ListView
# redirection to a DetailView


class ListReservation(views.ListView):
    context_object_name = 'reservations'
    template_name = 'reservation/list_res.html'
    model = Reservation
    # i can override the get_context_data() for return the context data bullshit


class DetailReservation(views.DetailView):
    context_object_name = 'reservations'
    template_name = 'reservation/detail_res.html'
    # we can specif the model argument or specify the queryset arg
    # we can specify the model by telling it which model to use
    model = Reservation
    # or we can give it the list of object we will be working with
    # queryset = Room.objects().all() # or with some kind of a filter
    # i can override the get_context_data() to insert the form data into the context object


class CreateReservation(views.CreateView):
    template_name = 'reservation/create_res.html'
    model = Reservation


class DeleteReservation(views.DeleteView):
    template_name = 'reservation/delete_res.html'
    model = Reservation


class UpdateReservation(views.UpdateView):
    template_name = 'reservation/update_res.html'
    model = Reservation
