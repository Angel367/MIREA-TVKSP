from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')  # Получаем объект запроса из контекста
        author_id = request.data.get('author')  # Получаем ID автора из тела запроса

        # Проверяем, что автор существует
        try:
            author = User.objects.get(id=author_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid author ID.")

        # Присваиваем автора
        validated_data['author'] = author

        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        author_id = request.data.get('author')
        # Проверяем, что автор существует
        try:
            author = User.objects.get(id=author_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid author ID.")

        # Присваиваем автора
        validated_data['author'] = author

        return super().create(validated_data)
