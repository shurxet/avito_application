from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from ads.views.ad import AdViewSet
from ads.views.comment import CommentViewSet

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet)

comments_router = routers.NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls))
]
