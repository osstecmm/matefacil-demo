from django.shortcuts import render
from django.http import HttpResponse
import subprocess, os
from sys import stdout, stdin, stderr

# Create your views here.
def funcionStart(request):
    return render(request, "index.html")

    

def resSimp(request):
    output = subprocess.run(["cat", "matefacil_demo/Programs/data.txt"], capture_output=True)
    return HttpResponse(output)

def resSimpCpp(request):
    p = subprocess.Popen(["./matefacil_demo/Programs/out1"],stdout=subprocess.PIPE, shell = True)
    m = p.communicate()[0].decode('utf-8')
    return HttpResponse(m)

def resCpp(request):
    p = subprocess.Popen(["./matefacil_demo/Programs/hello_input"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell = True)
    m = "%r" %request.GET["cppRes"]
    a = m.replace("'", "")
    p.stdin.write(f'{a}\n'.encode('utf-8'))
    s = p.communicate()[0].decode('utf-8')
    return HttpResponse(s)

def resJav(request):
    m1 = "%r" %request.GET["javaRes1"]
    m2 = "%r" %request.GET["javaRes2"]
    a1 = m1.replace("'", "")
    a2 = m2.replace("'", "")
    msj = f'{a1}{a2}\n'.encode('utf-8')
    p = subprocess.Popen([f'java -cp matefacil_demo/Programs HelloWorld {a1} {a2}'], stdout=subprocess.PIPE, shell = True)
    s = p.communicate(msj)[0].decode('utf-8')
    return HttpResponse(s)

def resC(request):
    p = subprocess.Popen(["./matefacil_demo/Programs/out3"], stdout=subprocess.PIPE, shell = True)
    s = p.communicate()[0].decode('utf-8')
    return HttpResponse(s)