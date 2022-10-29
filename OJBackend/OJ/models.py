from unittest import result
from django.db import models
from django.contrib.auth.models import AbstractUser
from froala_editor.fields import FroalaField

# Create your models here.

def check(text):
        if text.upper() != 'SOLVED' and text.upper() != 'UNSOLVED':
            raise Exception('Status must be either Solved or Unsolved')

def score_check(score):
    if score < 0 :
        raise Exception('Score must be greter than 0')

class User(AbstractUser):
    email = models.EmailField(unique=True)
    score = models.FloatField(default=0, validators=[score_check])
    solved = models.IntegerField(default=0)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.username


class Problem(models.Model):
    class Meta:
        ordering = ['-date_created']
    title = models.CharField(max_length=300)
    description = FroalaField()
    status = models.CharField(max_length=10, default='Unsolved',validators=[check,])
    difficulty = models.CharField(max_length=10, default='Easy')
    time_limit = models.IntegerField(default=1)
    memory_limit = models.IntegerField(default=128)
    score = models.FloatField(default=0, validators=[score_check])
    # user = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TestCases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.problem.title + 'testcases set ' + str(self.id)

class Submissions(models.Model):
    
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=200)
    previous_submission = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=10,null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.problem.title +'---' +self.user.username + "---"+self.result[:9]

class Code(models.Model):
    code = models.TextField()
    language = models.CharField(max_length=10)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

