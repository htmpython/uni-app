
from django.urls import path
from . import views

urlpatterns = [
    path("carousels",views.CarouselView.as_view()),
    path("vajras",views.VajraView.as_view()),
    path("user",views.UserView.as_view()),
    path("update",views.updateView.as_view()),
]
