from django.urls import path

from . import views

urlpatterns = [
    path('',views.vendor_index,name='vendor_index'),
    path('create/',views.vendor_create_view),
]