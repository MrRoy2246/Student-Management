# from django.urls import path
# from .views import DepartmentListView,DepartmentListCreateApiView,DepartmentDetailApiView
# urlpatterns = [
#     path('', DepartmentListView.as_view(),name='department-list'),
#     path('create/', DepartmentListCreateApiView.as_view(),name='department-create'),
#     path('<int:pk>/', DepartmentDetailApiView.as_view(),name='department-detail'),
# ]


from django.urls import path
from .views import DepartmentListCreateView, DepartmentDetailView

urlpatterns = [
    path('', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
]