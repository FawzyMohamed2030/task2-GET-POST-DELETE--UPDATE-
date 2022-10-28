from django.urls import path
from . import views


urlpatterns = [
    path('', views.getcharacters.as_view()),
    path('2/<int:pk>', views.postcharacters.as_view())
]
