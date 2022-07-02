from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from yaml import serialize
from .serializers import ProblemSerializer, TestCasesSerializer, SubmissionsSerializer, UserSerializer
from OJ.models import Problem, TestCases, Submissions, User
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

@api_view(['GET'])
def Leadership(request):
    if request.method == 'GET':
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['GET'])
def ListOfSubmissionsOfProblem(request, id):
    try:
        problem = Problem.objects.get(id=id)
    except Problem.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SubmissionsSerializer(Submissions.objects.filter(problem=problem), many=True)
        return Response(serializer.data)

def ListOfSubmissionsOfUser(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SubmissionsSerializer(Submissions.objects.filter(user=user), many=True)
        return Response(serializer.data)

