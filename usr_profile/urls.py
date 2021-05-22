from django.urls import path
from usr_profile import views
urlpatterns = [
    path('<str:usr_name>/',views.usrProfile,name='usr_profile'),
]
