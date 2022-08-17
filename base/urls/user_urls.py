from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name="login"),
    path('profile/', views.get_user_profile, name="user-profile"),
    path('profile/update/', views.update_user_profile, name="user-profile-update"),
]
