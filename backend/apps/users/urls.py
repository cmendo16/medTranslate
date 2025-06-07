from django.urls import path 
from .views import MyProfileView, SignupView

urlpatterns = [
    path("profile/", MyProfileView.as_view(), name="my-profile"),
    path('signup/', SignupView.as_view(), name='signup'),
]
