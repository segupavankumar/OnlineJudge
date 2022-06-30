from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from OJ.models import User, Problem, TestCases, Submissions


class ProblemSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id','title', 'description', 'status', 'time_limit', 'memory_limit', 'score','difficulty')