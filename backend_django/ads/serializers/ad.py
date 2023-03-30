from rest_framework import serializers
from ads.models.ad import Ad


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.ReadOnlyField(source="author.phone")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = [
            "pk", "image", "title", "price", "phone", "description",
            "author_first_name", "author_last_name", "author_id"
        ]


class AdCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['image', 'title', 'price', 'description']
