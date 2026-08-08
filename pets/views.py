from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Pet
from .serializer import PetSerializer


@api_view(["GET", "POST"])
def all_pet(request):

    if request.method == "GET":
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"pet added successfully",
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
