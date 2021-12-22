from django.urls import path

from .views import AboutUSView

app_name = 'landingpages'

urlpatterns = [
    path('services', AboutUSView.as_view(), name="services"),
]
