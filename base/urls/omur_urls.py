from django.urls import path
from base.views import omur_views as views


urlpatterns = [
    path('initials/', views.get_initials, name="get_initials"),
    path('createinitial/', views.create_initial, name="create_initial"),
]
