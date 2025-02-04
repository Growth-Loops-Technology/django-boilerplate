from django.urls import path
from django_template.user.views import SignupView, LoginView, GetAllUsersView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', GetAllUsersView.as_view(), name='get_all_users'),

]
