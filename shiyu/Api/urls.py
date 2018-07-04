from rest_framework.routers import DefaultRouter

from .views import ShiYuViewSets,KeyViewSet,UserViewsets
from Notes.models import ShiYu

router = DefaultRouter()

router.register('note', ShiYuViewSets)
router.register('key', KeyViewSet)
router.register('register', UserViewsets,base_name='users')



