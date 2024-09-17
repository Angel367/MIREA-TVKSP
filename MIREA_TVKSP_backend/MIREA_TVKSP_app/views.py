import json

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv
from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .zabbix_utils import get_zabbix_logs
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

import csv
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
import io

@api_view(['GET'])
def export_logs(request):
    url = "http://elasticsearch:9200/graylog_0/_search"
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "query": {
            "match_all": {}
        },
        "size": 10000
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response)
    if response.status_code != 200:
        return HttpResponse(response, status=500)
    result_csv = []
    for hit in response.json().get('hits', {}).get('hits', []):
        source = hit.get('_source', {})
        timestamp = source.get('timestamp')
        message = source.get('message')
        result_csv.append([timestamp, message])
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Timestamp', 'Message'])  # Write the header
    writer.writerows(result_csv)  # Write the data
    response_csv = HttpResponse(
        output.getvalue(),
        content_type='text/csv'
    )
    response_csv['Content-Disposition'] = 'attachment; filename="logs.csv"'

    return response_csv
