from django.shortcuts import render,redirect
from first.models import Comment


from .serializers import CommentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework import status

class CommentList(APIView):
    #определяет как будет рендериться класс в шаблоне
    #второй вариант JSONRenderer - но он подходит для is_ajax
    #данное решение реализую позже
    renderer_classes = (TemplateHTMLRenderer,)
    #шаблон для рендеринга
    template_name = 'test2.html'
    #метод отвечающий за обработку GET-запросов
    def get(self, request):
        form = CommentSerializers()
        allComment = sorted(Comment.objects.all().values_list('comment', flat=True),
                                 key=lambda item: len(set(item.split())), reverse=True)
        return Response({'allComment':allComment, 'form':form})

        """
        Есть лучшее решение, но оно работает только для первого варианта
        allComment = sorted(Comment.objects.all().values_list('comment', flat=True),
                                key=lambda item: len(set(item.split())), reverse=True)
        Это решение наиболее быстрое, так как вернет нам за раз все объекты из базы -values_list
        имя поля, flat=True - вернуть только значения.

        Пример с выводом результатов, для лучшего понимания
        Comment.objects.values_list('id', flat=True)
                    [1, 2, 3, 4, 5, 6]
        Comments.objects.values('id')
                    [{'id':1}, {'id':2}, {'id':3}, {'id':4}, {'id':5}, {'id':6}]
        Хотя для второго тоже)) если не испоьзовать сериализатор
                """

        # allComment = sorted(Comment.objects.all(),
        #     key=lambda item: item.quantity, reverse=True)
        # #создание набора данных для представления.
        # serializer = CommentSerializers(allComment, many=True)
        # #отправляем данные в темплейт
        # return Response({'allComment':serializer.data, 'form':form})


    #метод для обработки POST-запроса
    def post(self,request, format=None ):
        #инициализируем сеарилизатор данными пришедшими с формы
        serializer = CommentSerializers(data=request.data)
        #только после поверки они становятся нам доступными и мы можем их записать
        if serializer.is_valid():
            #записываем (под капотом дополнительно вызов метода create)
            serializer.save()
            #Результат новая страница GET-запроса
            return self.get(request) #redirect('api-test2')
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)
