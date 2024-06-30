from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuizQuestion
from .serializers import QuizQuestionSerializer

class QuizQuestionList(APIView):
    def get(self, request):
        questions = QuizQuestion.objects.all()
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from sklearn.neighbors import NearestNeighbors
import pandas as pd

data = {
    'quiz_scores': [[80, 70, 90], [50, 60, 70], [90, 90, 80], [60, 50, 70]],
    'recommended_topics': ['Advanced Math', 'Basic Algebra', 'Statistics', 'Intermediate Algebra']
}

df = pd.DataFrame(data)
knn = NearestNeighbors(n_neighbors=1, metric='euclidean')
knn.fit(df['quiz_scores'].tolist())

class RecommendView(APIView):
    def post(self, request):
        scores = request.data.get('scores')
        distances, indices = knn.kneighbors([scores])
        index = indices[0][0]
        topic = df.iloc[index]['recommended_topics']
        return Response({'recommended_topic': topic}, status=status.HTTP_200_OK)
