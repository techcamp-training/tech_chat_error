from django.urls import path
from . import views

app_name = 'answers'

urlpatterns = [
    path('', views.AnswerCreateView.as_view(), name='answer'),
]