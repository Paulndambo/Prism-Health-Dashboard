from django.urls import path
#from . views import UserRegisterView, CreateProfile, EditProfilePageView, ShowProfilePageView, UserEditView, PasswordsChangeView, password_success
from django.contrib.auth import views as auth_views
from . views import PasswordsChangeView, UserAccountView
from . import views
urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("password/", PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path("edit_account/", UserAccountView.as_view(), name="edit_account"),
]
