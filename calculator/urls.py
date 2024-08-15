from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('button/<int:pk>/', views.button, name='button'),
    path('delete', views.delete_button, name='delete'),
    path('stringbutton/<str:my_string>/', views.string_button, name='stringbutton'),
    path('solve', views.solve, name='solve'),



]
