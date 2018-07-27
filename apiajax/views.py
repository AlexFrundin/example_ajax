from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from first.models import Comment
from .forms import CommentForm
import json

def comment(request):
    context = {
        'allComents':Comment.objects.all(),
        'form':CommentForm()
    }
    if request.method == 'POST' and request.is_ajax():
        postForm = CommentForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            response_data = {}
            response_data['text']=postForm.cleaned_data['comment']
        return JsonResponse(response_data, content_type='application/json')
        #return HttpResponse(json.dumps(response_data),content_type='application/json')
    return render (request, 'test3.html', context)
