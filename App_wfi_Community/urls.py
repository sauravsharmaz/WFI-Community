from django.urls import path,include
from App_wfi_Community import views

urlpatterns = [
    path('',views.index),
    path('detail/<int:questionID>', views.detail), 
    path('writeAns/<int:questionID>',views.writeAns), 
    path('saveComment/<int:ansID>/<int:questionID>',views.saveComment), 
    path('update/<int:ansID>',views.update), 
    path('delete/<int:ansID>',views.deleteAns),
    path('search/', views.search), 
]
