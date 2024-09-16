from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
def export_logs(request):
    # Здесь вам нужно будет реализовать логику для получения данных из GrayLog
    # Для примера, я создаю фиктивные данные
    logs = [
        {"timestamp": "2023-10-01T12:00:00Z", "message": "Sample log message 1"},
        {"timestamp": "2023-10-01T12:05:00Z", "message": "Sample log message 2"},
    ]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="logs.csv"'

    writer = csv.writer(response)
    writer.writerow(['timestamp', 'message'])

    for log in logs:
        writer.writerow([log['timestamp'], log['message']])

    return response
