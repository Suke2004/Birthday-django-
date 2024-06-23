from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('Santhu/',views.birthday,name="birthday")
]
