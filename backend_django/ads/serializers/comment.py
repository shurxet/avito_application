from rest_framework import serializers
from ads.models.comment import Comment


class CommentListDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_image = serializers.SerializerMethodField('get_author_image_url')

    class Meta:
        model = Comment
        fields = [
            "pk", "text", "author_id", "created_at", "author_first_name", "author_last_name", "ad_id", "author_image"
        ]

    def get_author_image_url(self, obj):
        request = self.context.get("request")
        image_url = obj.author.image.url if obj.author.image else '/django_media/user_avatars/avatar_placeholder.jpg'
        return request.build_absolute_uri(image_url)


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']
