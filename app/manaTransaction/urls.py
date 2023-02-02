from django.urls import path
from . import views


urlpatterns = [
    path('index', view=views.index, name="index"),
    path('', view=views.Dashboard, name="dashboard"),
]