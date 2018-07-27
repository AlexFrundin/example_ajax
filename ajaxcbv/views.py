from django.shortcuts import render

from apiajax.views import CommentForm
from django.http import JsonResponse, HttpResponse
from first.models import Comment
from django.views.generic.edit import CreateView

from pprint import pprint

class AjaxMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
    def form_valid(self, form):
        if self.request.is_ajax():
            #это модель))
            form =form.save()
            data = {
                'text':form.comment
            }
            return JsonResponse(data)

class CommentViews(AjaxMixin, CreateView):
    form_class = CommentForm
    template_name = 'test3.html'
    def get(self, request, *args, **kwargs):
        context = {
            'allComents':Comment.objects.all(),
            'form':CommentForm()
        }
        return render (request, self.template_name, context)


    # def post(self, request):
    #     postForm = CommentForm(request.POST)
    #     if postForm.is_valid():
    #         postForm.save()
    #         response_data = {}
    #         response_data['text']=postForm.cleaned_data['comment']
    #     return JsonResponse(response_data, content_type='application/json')
