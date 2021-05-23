from django.urls import path
#from . views import UserRegisterView, CreateProfile, EditProfilePageView, ShowProfilePageView, UserEditView, PasswordsChangeView, password_success
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("profile/", views.profile, name="profile"),
]
