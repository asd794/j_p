from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("year<int:year>/",views.year_archive),
    path("month/<year>/<month>/",views.month_archive),

]