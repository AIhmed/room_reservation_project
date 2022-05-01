from django.urls import path
from . import views


urlpatterns = [
        # paths for each of my CRUD actions
        path('list_reservations/', views.ListReservation.as_view(), name='listreservations'),
        path('detail_reservation/<id: int>/', views.DeteailReservation.as_view(), name='detailreservation'),
        path('create_reservation/', views.CreateReservation.as_view(), name='createreservation'),
        path('delete_reservation/', views.DeleteReservation.as_view(), name='deletereservation'),
        path('update_reservation/', views.UpdateReservation.as_view(), name='updatereservation'),
        ]
