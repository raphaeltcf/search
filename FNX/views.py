from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters

from .models import Question, Choice
from .serializer import QuestionSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class QuestionAPIView(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Create your views here.
