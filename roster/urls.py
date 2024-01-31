from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/',views.staff_detail, name='dashboard-staff-detail'),
    path('duty/',views.duty, name='dashboard-duty'),
    path('duty/delete/<int:pk>/',views.duty_delete, name='dashboard-duty-delete'),
    path('duty/update/<int:pk>/',views.duty_update, name='dashboard-duty-update'),
    path('order/',views.order, name='dashboard-order'),
]
