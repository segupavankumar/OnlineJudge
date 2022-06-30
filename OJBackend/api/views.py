from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ProblemSerializer
from OJ.models import Problem
from django.http import HttpResponse
# Create your views here.


@api_view(['GET'])
def Problem_post(request):
    if request.method == 'GET':
        serializer = ProblemSerializer(Problem.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['GET'])
def Problem_detail(request, id):
    try:
        problem = Problem.objects.get(id=id)
    except Problem.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)
