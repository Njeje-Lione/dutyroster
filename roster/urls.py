from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/',views.staff_detail, name='dashboard-staff-detail'),
    path('duty/',views.duty, name='dashboard-duty'),
    path('leave/',views.leave, name='dashboard-leave'),
    path('leavelist/',views.leavelist, name='dashboard-leavelist'),
    path('complain/',views.complain, name='dashboard-complain'),
    path('complain/list/',views.complainlist, name='dashboard-complain-list'),
    path('duty/delete/<int:pk>/',views.duty_delete, name='dashboard-duty-delete'),
    path('duty/update/<int:pk>/',views.duty_update, name='dashboard-duty-update'),
    path('ward/', views.ward, name='dashboard-ward'),
    path('ward/delete/<int:pk>/',views.ward_delete, name='dashboard-ward-delete'),
    path('ward/update/<int:pk>/',views.ward_update, name='dashboard-ward-update'),
    path('order/',views.order, name='dashboard-order'),
]
