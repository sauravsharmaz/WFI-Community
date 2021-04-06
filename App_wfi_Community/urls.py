from django.urls import path, re_path
from App_wfi_Community import views

urlpatterns = [
    path('',views.index),
    # path('/answers/<slug:qtn_title>',views.ans),
    path('detail/<int:questionID>', views.detail),
]
