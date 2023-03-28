from rest_framework.viewsets import ModelViewSet
from ads.models.ad import Ad
from ads.models.comment import Comment
from ads.serializers.comment import CommentListSerializer, CommentCreateSerializer, CommentSerializer
from ads.permissions.permissions import UserPermission


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        'retrieve': CommentListSerializer,
        'create': CommentCreateSerializer,
        'update': CommentCreateSerializer,
    }

    permission_classes = (UserPermission,)

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_pk'])
        serializer.save(author=self.request.user, ad=ad)
