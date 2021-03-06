from django.conf.urls import url, include
from rest_framework import routers

from TestAuth import views

router = routers.DefaultRouter()
router.register(r'user', views.UserProfileViewSet)
router.register(r'group', views.GroupViewSet)


urlpatterns = [
    # /user/
    url(r'^test/', include(router.urls)),

    url(r'^test/api-auth/', include('rest_framework.urls',  namespace='rest_framework'))
]

