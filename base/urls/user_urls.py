from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name="login"),
    path('profile/', views.get_user_profile, name="user-profile"),
    path('profile/update/', views.update_user_profile, name="user-profile-update"),
    path('allusers/', views.get_all_users, name="users"),
    path('get/<str:id>/', views.get_user, name="user-get"),
    # path('deneme/', views.deneme, name="deneme"),
    path('update/<str:id>/', views.update_user, name="user-update"),
]
