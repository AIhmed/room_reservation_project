from django.views import generic as views
from .models import Chamber

# views take a request as arg and return a responce

# redirection from filling a form
# redirection to a ListView
# redirection to a DetailView


class ListReservation(views.ListView):
    template_name = 'list_res.html'
    model = Chamber
    # i can override the get_context_data() for return the context data bullshit


class DetailReservation(views.DetailView):
    template_name = 'detail_res.html'
    model = Chamber


class CreateReservation(views.CreateView):
    template_name = 'create_res.html'
    model = Chamber
    # i can override the get_context_data() to insert the form data into the context object


class DeleteReservation(views.DeleteView):
    template_name = 'delete_res.html'
    model = Chamber


class UpdateReservation(views.UpdateView):
    template_name = 'update_res.html'
    model = Chamber
