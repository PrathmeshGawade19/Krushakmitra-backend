from django.urls import path
from .views import RegisterView, UserListView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .token_views import CustomTokenObtainPairView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # new endpoint
    path('', UserListView.as_view(), name='user-list'),
]
