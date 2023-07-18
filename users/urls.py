from django.urls import path
from users.views import SignUp
from users.views import SignIn
from users.views import ProfileView
from users.views import EditProfile
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView





urlpatterns = [
    path('api/v1/regis/', SignUp.as_view()),
    path('api/v1/login/', SignIn.as_view(), name='jwt_create'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='verify'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='verify'),
    path('api/v1/profile/', ProfileView.as_view(), name="username"),
    path('api/v1/editing_profile/<int:pk>/', EditProfile.as_view(), name="edit-profile"),
]
