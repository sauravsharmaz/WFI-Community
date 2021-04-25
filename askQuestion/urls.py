from django.urls import path
from askQuestion import views

urlpatterns = [
    path('',views.ask,name='ask'),
    path('Success',views.success,name='success_page'),
]
