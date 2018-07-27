from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CommentForm
from .models import Comment
from django.db.models import F, Value,ExpressionWrapper
# Create your views here.

def test(request):
    allComment = sorted(Comment.objects.all(),
                        key=lambda item: item.quantity, reverse=True)

    context = {'form':CommentForm(),
               'allComment':allComment}

    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.save()
        return redirect('test')#так называется функция в урлах

    return render(request, "test.html", context)
