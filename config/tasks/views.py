from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializer import TaskSerializer
@api_view(['GET', 'POST'])
def task_list_creat(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializers=TaskSerializer(tasks, many=True)
        return Response(serializers.data)
    if request.method == "POST":
        serializers=TaskSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET','PUT','PATCH','DELETE'])
def task_detail(request, pk):
    try:
        task=Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            {"error": "task not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializers=TaskSerializer(task)
        return Response(serializers.data)
    if request.method == "PUT":
        serializers=TaskSerializer(
            task,
            data=request.data
        )
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == "PATCH":
        serializers = TaskSerializer(
            task,
            data=request.data,
            partial=True
        )
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == "DELETE":
        task.delete()
        return Response(
            {"message":"deleted sucessfull"},
            status=status.HTTP_200_OK
        )
    
            
        

            
    



