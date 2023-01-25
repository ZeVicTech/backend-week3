from django.shortcuts import render
from rest_framework import status

from .models import ToDo
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ToDoSerializer

# Create your views here.


class ToDoSimple(APIView):
    def get(self, request):
        all_todolist = ToDo.objects.all()
        serializer = ToDoSerializer(all_todolist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetail(APIView):
    def get_object(self, id):
        return ToDo.objects.get(id=id)

    def get(self,request, id):
        todo = self.get_object(id)
        print(type(todo))
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, id):
        todo = self.get_object(id)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




