from django.urls import path
from .views import CommentViews
urlpatterns=[
    path('', CommentViews.as_view()),
]
