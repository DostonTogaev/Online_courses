from django.urls import path
from courses.views import CourseListView, CourseDetailView, AddCommentView
urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses'),
    path('course/<int:course_id>', CourseDetailView.as_view(),
         name='courses_detail'),

    path('detail/<int:course_id>/comment', AddCommentView.as_view(), name='add_comment'),

]