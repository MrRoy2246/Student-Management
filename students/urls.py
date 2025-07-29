from django.urls import path
from .views import StudentOwnProfileView,StudentProfileListView,StudentProfileDetailView



urlpatterns = [
    path('profile/', StudentOwnProfileView.as_view(),name='own-profile'),
    path('all-profile/', StudentProfileListView.as_view(),name='student-list'),
    path('<int:pk>/', StudentProfileDetailView.as_view(),name='student-profile-detail'),
    
]


