import subprocess
import os
from OJ.models import User,Problem,Submissions,TestCases
from django.http import HttpResponse

import time
def run_python(code,input_):

    file_name = 'code.py'
    file = open(file_name, 'w+')
    file.write(code)
    t = file.read()
    print(t)
    file.close()

    process = subprocess.run(['python', file_name], input = input_,encoding="utf-8",stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.stdout, process.stderr

    os.remove(file_name)
    

    if stdout:
        s = stdout
        s.replace('\n','<br>')
        # print(s)
        return s
    else:
        return stderr


def run_c(code, problem_id):
    # Create a file with the code
    file_name = 'code.c'
    file = open(file_name, 'w')
    file.write(code)
    file.close()


    # Run the cod
    # process = subprocess.Popen(['g++', file_name, '-o', 'code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()

    subprocess.run(["g++", file_name])
    f = open('a.txt','w')
    subprocess.run("a",stdout=f)
    f.close()
    f = open('a.txt', 'r')
    output = f.read()
    f.close()
    os.remove('a.txt') 
    os.remove(file_name)
    os.remove('a.exe')

    # print(stdout.decode('utf-8'))
    return output

def run_cpp(code, problem_id):
    # Create a file with the code
    file_name = 'code.cpp'
    file = open(file_name, 'w')
    file.write(code)
    file.close()

    # Run the code
    process = subprocess.run(['g++', file_name] )
    f = open('a.txt','w')
    subprocess.run("a",stdout=f)
    f.close()
    f = open('a.txt', 'r')
    output = f.read()
    f.close()
    os.remove('a.txt') 
    os.remove(file_name)
    os.remove('a.exe')

    # print(stdout.decode('utf-8'))
    return output
def run_javascript(code, problem_id):
    # Create a file with the code
    file_name = 'code.js'
    file = open(file_name, 'w')
    file.write(code)
    file.close()

    # Run the code
    process = subprocess.Popen(['node', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    os.remove(file_name)

    # print(stdout.decode('utf-8'))
    return stdout.decode('utf-8')

def run_code(code, language,input_):
    if language == 'c':
        return run_c(code, test)
    elif language == 'cpp':
        return run_cpp(code, test)
    elif language == 'python':
        return run_python(code, input_)
    elif language == 'javascript':
        return run_javascript(code, test)



def Run_time(*args,**kwargs):
    def wrapper(*args,**kwargs):
        start = time.time()
        result_code = run_code(*args,**kwargs)
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


