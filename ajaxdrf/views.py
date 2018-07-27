from django.shortcuts import render
from api.serializers import CommentSerializers
from first.models import Comment
from apiajax.forms import CommentForm

from rest_framework import generics

def home(request):
    pass
