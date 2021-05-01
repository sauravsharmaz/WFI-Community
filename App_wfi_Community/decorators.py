from django.http import request
from django.shortcuts import redirect

def authentication_required(func_arg):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func_arg(request, *args, **kwargs)
        else:
            return redirect('login_page')
    return wrapper_func

def welcome_user_auth(func_arg):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func_arg(request, *args, **kwargs)
        else:
            return redirect('login_page')
    return wrapper_func
