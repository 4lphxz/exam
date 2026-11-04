from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from app.serializers import RecipeSerializer
from rest_framework.response import Response
from app.models import Recipe

# Create your views here.
class recipeCreate(APIView):
    def post(self,request):
        serializer_instance=RecipeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()

            return  Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class recipeList(APIView):
    def get(self,request):
        qs=Recipe.objects.all()
        serializer_instance = RecipeSerializer(qs, many=True)
        return Response(serializer_instance.data)

class recipeRetrieve(APIView):
    def get(self,request,i):
        e=get_object_or_404(Recipe,id=i)
        serializer_instance = RecipeSerializer(e)
        return Response(serializer_instance.data)
class recipeUpdate(APIView):
    def put(self,request,i):
        e=get_object_or_404(Recipe,id=i)
        serializer_instance = RecipeSerializer(instance=e,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class RecipePartialupdate(APIView):
    def patch(self, request, i):
        e = get_object_or_404(Recipe, id=i)
        serializer_instance = RecipeSerializer(instance=e, data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class RecipeDelete(APIView):
    def delete(self, request, i):
        e = get_object_or_404(Recipe,id=i)
        e.delete()
        return Response({'message':"deleted"})