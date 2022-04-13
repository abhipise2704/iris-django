from unicodedata import name
from django.urls import path 
from . import views 

app_name='prediction'

urlpatterns=[
    path('',views.predict,name='predict'),
    path('predict/',views.predict_chances,name='submit_prediction'),
    path('results/', views.view_results, name='results'),
]