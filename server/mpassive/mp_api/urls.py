from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, DeviceViewSet, SensorViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'sensors', SensorViewSet)

rootUrl = 'api/'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(rootUrl, include(router.urls)),
    path(rootUrl + 'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]