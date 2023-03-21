import random
from .backends import EmailPhoneUsernameAuthenticationBackend as EoP
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import UserLoginForm,UserCreationForm
from django.contrib.auth import login 
from django.contrib import   messages
from django.contrib.auth.decorators import login_required


class UserLoginView(View):
    form_class = UserLoginForm
    
    template_name = 'login.html'
    def dispatch(self, request, *args, **kwargs):
         if request.user.is_authenticated:
              return redirect('home')
         return super().dispatch(request, *args, **kwargs)

    def get(self, request):
      form = self.form_class
      return render(request, "login.html", {'form': form,'form1':UserCreationForm})

    def post(self, request):
      form = self.form_class(request.POST)
      if form.is_valid():
        cd = form.cleaned_data
        user = EoP.authenticate(request, username=cd['email'], password=cd['password'])
        print("auth bata")
        if user is not None:
            login(request, user)
            print("Sxxx")
            messages.success(request, 'You have successfully logged in!', 'success')
            return redirect('home')
        else:
            messages.error(request, 'Your email or password is incorrect!', 'danger')


class WelcomeView(TemplateView):
    template_name="welcome.html"
    