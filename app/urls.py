from django.urls import path
from . import views

urlpatterns = [
  path('', views.foo, name='hello'),
  path('test/', views.test, name="")
]
