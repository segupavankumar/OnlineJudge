import subprocess
import os

def run_python(code,problem_id):

    # Create a file with the code
    file_name = 'code.py'
    file = open(file_name, 'w')
    file.write(code)
    file.close()

    # Run the code
    process = subprocess.Popen(['python', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    os.remove(file_name)

    # print(stdout.decode('utf-8'))
    if stdout:
        return stdout.decode('utf-8')
    else:
        return stderr.decode('utf-8')


def run_c(code, problem_id):
    # Create a file with the code
    file_name = 'code.c'
    file = open(file_name, 'w')
    file.write(code)
    file.close()


    # Run the code
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
    process = subprocess.Popen(['g++', file_name, '-o', 'code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    os.remove(file_name)

    # print(stdout.decode('utf-8'))
    return stdout.decode('utf-8')

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

def run_code(code, language, problem_id,user_id):
    if language == 'c':
        return run_c(code, problem_id)
    elif language == 'c++':
        return run_cpp(code, problem_id)
    elif language == 'python':
        return run_python(code, problem_id)
    elif language == 'javascript':
        return run_javascript(code, problem_id)

