from django.urls import path
from . import views
from .views import student_view, update_student, delete_student, create_student, query_student

urlpatterns = [
    path('student/', student_view, name='student'),
    path('student/update', update_student, name='update_student'),
    path('student/delete', delete_student, name='delete_student'),
    path('student/create', create_student, name='create_student'),
    path('student/query', query_student, name='query_student'),
]