from django.urls import path
from .views import StudentOwnProfileView,StudentProfileListView



urlpatterns = [
    path('profile/', StudentOwnProfileView.as_view(),name='own-profile'),
    path('all-profile/', StudentProfileListView.as_view(),name='own-profile'),
    
]


