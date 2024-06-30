from django.urls import path
from .views import QuizQuestionList, RecommendView

urlpatterns = [
    path('questions/', QuizQuestionList.as_view(), name='question-list'),
    path('recommend/', RecommendView.as_view(), name='recommend'),
]
