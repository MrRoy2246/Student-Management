
from django.urls import path
from .views import RegisterView,LoginView,ProtectedTestView,ProfileView,AdminCreationView
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register' ),
    path('create-admin/', AdminCreationView.as_view(), name='create_admin'),
    path('login/',LoginView.as_view(),name='login' ),
    path('protected/', ProtectedTestView.as_view(), name='protected_test'),
    path('profile/',ProfileView.as_view(),name='profile' ),

]
