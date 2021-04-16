from django.urls import path
from askQuestion import views

urlpatterns = [
    path('',views.ask),
    path('Success',views.success),
]
