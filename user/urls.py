from django.urls import path
from .views import UserInfoView

urlpatterns = [
    path('submit/', UserInfoView.as_view(), name='user-info'),
]