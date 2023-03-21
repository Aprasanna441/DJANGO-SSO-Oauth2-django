from django.urls import path,include
from .views import UserLoginView,WelcomeView


urlpatterns = [
    path('',UserLoginView.as_view(),name='login'),
    path('home',WelcomeView.as_view(),name="home")
]