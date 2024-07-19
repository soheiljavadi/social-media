from django.urls import path, include
from .views import Register_user,MyTokenObtainPairView,TokenRefreshView





app_name='account'
urlpatterns = [path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

path('register',Register_user.as_view(),name='register'),]