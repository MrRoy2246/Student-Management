from django.urls import path
from .views import DepartmentListView,DepartmentListCreateApiView,DepartmentDetailApiView
urlpatterns = [
    path('', DepartmentListView.as_view(),name='department-list'),
    path('create/', DepartmentListCreateApiView.as_view(),name='department-create'),
    path('<int:pk>/', DepartmentDetailApiView.as_view(),name='department-detail'),
]


