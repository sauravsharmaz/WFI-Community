from django.urls import path,include
from App_wfi_Community import views

urlpatterns = [
    path('',views.index,name='Home_page'),
    path('detail/<int:questionID>', views.detail,name='detail_page'), 
    path('writeAns/<int:questionID>',views.writeAns,name='writeAns_page'), 
    path('saveComment/<int:ansID>/<int:questionID>',views.saveComment,name='saveComment'), 
    path('update/<int:ansID>',views.update,name='update'), 
    path('delete/<int:ansID>',views.deleteAns,name='deleteAns'),
    path('search/', views.search,name='search'), 
]
