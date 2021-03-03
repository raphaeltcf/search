from django.urls import path
from . import views
from .views import QuestionAPIView

urlpatterns = [
    path('questions/',  views.QuestionAPIView.as_view()),
]