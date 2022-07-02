from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from OJ.models import User, Problem, TestCases, Submissions


class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id','title', 'description', 'status', 'time_limit', 'memory_limit', 'score','difficulty')

class TestCasesSerializer(ModelSerializer):
    class Meta:
        model = TestCases
        fields = ('id','problem','input', 'output', 'score')

class SubmissionsSerializer(ModelSerializer):
    class Meta:
        model = Submissions
        fields = ('id','problem','user','date_created','result','previous_submission')

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','score','solved')