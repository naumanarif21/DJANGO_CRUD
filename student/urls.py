from django.urls import path

from .views import *

urlpatterns = [
    path('', StudentListView.as_view(), name="student-list"),
    path('add/', StudentAddView.as_view(), name="student-add"),
    path('student/<int:pk>/', StudentDetailView.as_view(), name="student-detail"),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name="student-update"),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name="student-delete"),
    path('student/<int:pk>/age/', StudentActionView.as_view(), name="student-age")
]
