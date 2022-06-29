from django.contrib import admin
from OJ.models import User, Problem, TestCases,Submissions

# Register your models here.
admin.site.register(User)
admin.site.register(Problem)
admin.site.register(TestCases)
admin.site.register(Submissions)
