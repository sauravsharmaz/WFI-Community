from django.urls import path, re_path
from App_wfi_Community import views

urlpatterns = [
    path('',views.index),
    path('detail/<int:questionID>', views.detail), 
    path('writeAns/<int:questionID>',views.writeAns), 
]
