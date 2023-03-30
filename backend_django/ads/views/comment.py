from rest_framework import pagination
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from ads.models import Comment
from ads.models.ad import Ad

from ads.serializers.comment import CommentListDetailSerializer, CommentCreateUpdateSerializer
from ads.permissions.ad_permissions import AdPermission


class CommentPagination(pagination.PageNumberPagination):
    page_size = 100


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListDetailSerializer
    pagination_class = CommentPagination
    permission_classes = (AdPermission,)
    obj = Comment.objects.all()
    serializer_action_classes = {
        'list': CommentListDetailSerializer,
        'retrieve': CommentListDetailSerializer,
        'create': CommentCreateUpdateSerializer,
        'update': CommentCreateUpdateSerializer,
    }

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_id)
        return ad.comments.all().order_by("-created_at")

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_id)
        serializer.save(author=self.request.user, ad=ad)
