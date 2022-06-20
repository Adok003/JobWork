from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'employees', views.EmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
