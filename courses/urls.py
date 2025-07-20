from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CourseViewSet,SectionViewset

router=DefaultRouter()
router.register('courses',CourseViewSet,basename='courses')
router.register('section',SectionViewset,basename='section')
urlpatterns = [
    path('',include(router.urls)),
    
]
