from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ads.models.ad import Ad
from ads.permissions.ad_permissions import AdPermission
from ads.serializers.ad import AdListSerializer, AdDetailSerializer, AdCreateUpdateSerializer
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from ads.filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(ModelViewSet):

    queryset = Ad.objects.all().order_by("-created_at")
    serializer_class = AdListSerializer
    pagination_class = AdPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdFilter
    permission_classes = (AdPermission,)

    serializer_action_classes = {
        'list': AdListSerializer,
        'retrieve': AdDetailSerializer,
        'create': AdCreateUpdateSerializer,
        'update': AdCreateUpdateSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    @action(detail=False, methods=['get'], url_path='me', serializer_class=AdListSerializer)
    def ads_me(self, request, *args, **kwargs):
        ads_user = Ad.objects.filter(author=self.request.user).order_by("-created_at")
        page = self.paginate_queryset(ads_user)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset=Ad.objects.all(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
