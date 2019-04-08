from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CategoriaList
from django.urls import path


router = DefaultRouter()
router.register('items', ItemViewSet)

urlpatterns = [
    path('categories', CategoriaList.as_view()),
]

urlpatterns += router.urls
