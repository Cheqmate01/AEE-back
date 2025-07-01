from django.urls import path
from .views import LatestUpdatesView

urlpatterns = [
    path('latest/', LatestUpdatesView.as_view(), name='latest-updates'),
]