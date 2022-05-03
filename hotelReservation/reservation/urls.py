from django.urls import path
from . import views
from . import forms


urlpatterns = [
        # paths for each of my CRUD actions
        path('list_reservations/', views.ListReservation.as_view(), name='listreservations'),
        path('detail_reservation/<int:pk>/', views.DetailReservation.as_view(), name='detailreservation'),
        path('create_reservation/', views.CreateReservation.as_view(), name='createreservation'),
        path('delete_reservation/', views.DeleteReservation.as_view(), name='deletereservation'),
        path('update_reservation/', views.UpdateReservation.as_view(), name='updatereservation'),
        path('user_form/', forms.UserFormView.as_view(), name='userform'),
        path('reservation_form/', forms.ReservationFormView.as_view(), name='reservationform')
        ]
