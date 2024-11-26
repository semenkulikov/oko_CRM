from django.urls import path, include
from authapp.views import UserLoginView, UserLogoutView, UserSignUpView, ProfileDetailView

app_name = 'authapp'

urlpatterns = [
    # path('forgot-password/', UserPassResetView.as_view(),
    #      name='forgot_pass'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('set-password/<uidb64>/<token>/', UserPassChangeView.as_view(),
    #      name='set_pass'),
    path('signup/', UserSignUpView.as_view(),
         name='signup'),
    path('logout/', UserLogoutView.as_view(),
         name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile')
    # path('verified/<str:email>/<str:key>/', verify_user,
    #      name='verified'
    #      ),

    #     path("login/",
    #          auth_views.LoginView.as_view(template_name="authapp/login.html"), name='login'),
]