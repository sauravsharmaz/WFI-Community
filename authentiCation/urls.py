from django.urls import path
from authentiCation import views
 
urlpatterns = [
	path('register/',views.register_Page,name='register_Page'),
	path('login/',views.login_page,name='login_page'),
	path('logout/',views.log_out,name='logout_page'),
]