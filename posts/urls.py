from django.urls import path
from . import views
urlpatterns = [
    path('helloworld/',views.helloWorld),
    path("<int:id>/",views.post)
]