from django.urls import path, include
from rest_framework import routers

from . import views
from .api.view_sets import UserViewSet, StudentViewSet, TeacherViewSet, ClaseViewSet, DisponibleViewSet, PaymentViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'clases', ClaseViewSet)
router.register(r'disponibles', DisponibleViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("arrange", views.arrange, name="arrange"),
    path("packs", views.packs, name="packs"),
    path("payments", views.payments, name="payments"),
    path("profile", views.profile, name="profile"),
    path("teacher/<int:teacher_id>", views.teacher, name="teacher"),
    path("home", views.home, name="home"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]