from django.urls import path
from teachers.views import TeacherListView, TeacherDetailView
urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teacher_details/<int:teacher_id>/', TeacherDetailView.as_view(), name='teacher_details'),

]