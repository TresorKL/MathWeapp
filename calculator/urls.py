import imp
from django.urls import path
from . import views


urlpatterns = [
    path('',views.getInputs,name='calculator'),
    path('result/',views.determineResult,name='result')
    
]
