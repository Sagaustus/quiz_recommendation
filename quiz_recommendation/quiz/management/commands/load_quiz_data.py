import csv
from django.core.management.base import BaseCommand
from quiz.models import QuizQuestion

class Command(BaseCommand):
    help = 'Load quiz data from CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'logic.csv'  # Update this path
        with open(file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                QuizQuestion.objects.create(
                    question_text=row['question_text'],
                    topic_id=row['topic_id'],
                    difficulty=row['difficulty'],
                    choice_a=row['choice_a'],
                    choice_b=row['choice_b'],
                    choice_c=row['choice_c'],
                    choice_d=row['choice_d'],
                    correct_answer=row['correct_answer'],
                    explanation=row['explanation'],
                )
