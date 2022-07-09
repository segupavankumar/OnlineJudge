import subprocess
import os
from OJ.models import User,Problem,Submissions,TestCases,Submissions
from django.http import HttpResponse

import time
def run_python(code,input_):

    file_name = 'code.py'
    file = open(file_name, 'w+')
    file.write(code)
    file.close()

    process = subprocess.run(['python', file_name], input = input_,encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.stdout, process.stderr

    os.remove(file_name)
    
    # print(stdout)
    if stdout:
        return stdout[:-1]
    else:
        return stderr


def run_c(code,input_):
    # Create a file with the code
    file_name = 'code.c'
    file = open(file_name, 'w')
    file.write(code)
    file.close()

    subprocess.run(["gcc", file_name])
    # f = open('a.txt','w')
    f = subprocess.run("a",input = input_,encoding="utf-8",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # print(f)
    # f.close()
    # f = open('a.txt', 'r')
    # output = f.stdout
    # f.close()
    # os.remove('a.txt') 
    os.remove(file_name)
    os.remove('a.exe')

    # print(stdout.decode('utf-8'))
    if f.stdout:
        return f.stdout
    else:
        return f.stderr

def run_cpp(code,input_):
    # Create a file with the code
    file_name = 'code.cpp'
    file = open(file_name, 'w')
    file.write(code)
    file.close()

    # Run the code
    process = subprocess.run(['g++', file_name] )
    # f = open('a.txt','w')
    f = subprocess.run("a",input = input_,encoding="utf-8",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # f.close()
    # f = open('a.txt', 'r')
    # output = f.read()
    # f.close()
    # os.remove('a.txt') 
    os.remove(file_name)
    os.remove('a.exe')

    # print(stdout.decode('utf-8'))
    if f.stdout:
        return f.stdout
    else:
        return f.stderr
def run_javascript(code,input_):
    file_name = 'code.js'
    file = open(file_name, 'w+')
    file.write(code)
    file.close()

    process = subprocess.run(['node', file_name], input = input_,encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.stdout, process.stderr

    os.remove(file_name)
    

    if stdout:
        s = stdout[:-1]
        # s.replace('\n','<br>')
        return s
    else:
        return stderr

def run_code(code, language,input_):
    if language == 'c':
        return run_c(code, input_)
    elif language == 'cpp':
        return run_cpp(code, input_)
    elif language == 'python':
        return run_python(code, input_)
    elif language == 'javascript':
        return run_javascript(code, input_)



def Run_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result_code = func(*args,**kwargs)
        end = time.time()
        run_time = end-start
        result = {'result':result_code,'run_time':run_time}
        return result
    return wrapper


def evaluation(code,language,problem_id,user_id):
    try:
        problem = Problem.objects.get(id=problem_id)
        user = User.objects.get(id=user_id)
    except Problem.DoesNotExist:
        return HttpResponse(status=404)

    test_cases = TestCases.objects.filter(problem=problem,many = True)

    for test in test_cases:
        result = run_code(code, language,test)



@Run_time
def Run(code,language,input_):
    return run_code(code,language,input_)


def Submit(code,language,problem_id,user_id):
    try:
        problem = Problem.objects.get(id=problem_id)
        user = User.objects.get(id=user_id)
    except Problem.DoesNotExist:
        return HttpResponse(status=404)

    test_cases = TestCases.objects.filter(problem=problem)

    length_test_cases = len(test_cases)
    
    for input_ in test_cases:
        Result = Run(code, language,input_.input)
        # print(input_.output.encode('utf-8'))
        input_.output = input_.output.encode('utf-8')
        # print(Result['result'][:].encode('utf-8'))
        result_ = Result['result']
        Result['result'] = Result['result'][:].encode('utf-8')
        if 'Error' in result_:
            out = 'Runtime Error in test case ' + str(len(test_cases) - length_test_cases) + '\n' + result_
        elif Result['result'] == input_.output and Result['run_time'] <= problem.time_limit:
            length_test_cases -= 1
        elif Result['result'] == input_.output and Result['run_time'] > problem.time_limit:
            out = 'Time Limit Exceeded on test case ' + str(len(test_cases) - length_test_cases)
        else:
            out = 'Wrong Answer on test case ' + str(len(test_cases) - length_test_cases) 
            break
    if length_test_cases == 0:
        out = 'Accepted'
        solved = user.solved +1
        score = user.score + problem.score
        user.solved = solved
        user.score = score
        user.save()


    submission = Submissions.objects.create(user=user,problem=problem,language=language,result=out,previous_submission=code)
    submission.save()

    return out
    
