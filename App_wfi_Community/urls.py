from django.urls import path
from App_wfi_Community import views

urlpatterns = [
    path('',views.index),
    path('answers/<str:qtn_title>',views.ans),
]
