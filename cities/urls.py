from django.urls import path
from . import views


urlpatterns = [
    path("", views.NewCityView.as_view()),
    path("<int:pk>/", views.NewCityDetailView.as_view()),
]
