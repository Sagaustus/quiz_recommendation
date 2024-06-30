# quiz/models.py

from django.db import models

class QuizQuestion(models.Model):
    question_text = models.TextField()
    topic_id = models.IntegerField()
    difficulty = models.CharField(max_length=50)
    choice_a = models.TextField()
    choice_b = models.TextField()
    choice_c = models.TextField()
    choice_d = models.TextField()
    correct_answer = models.TextField()
    explanation = models.TextField()
