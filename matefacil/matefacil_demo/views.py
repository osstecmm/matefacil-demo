from django.shortcuts import render
from django.http import HttpResponse
import subprocess, os
from sys import stdout, stdin, stderr

# Create your views here.
def funcionStart(request):
    return render(request, "index.html")

    

def resSimp(request):
    proc = subprocess.Popen(['cat', '-'], stdout=subprocess.PIPE, )
    #proc = subprocess.Popen(['.matefacil_demo/Programs/'])
    msg = 'through stdin to stdout'.encode('utf-8')
    stdout_value = proc.communicate(msg)[0]
    h = 'pass through: ', stdout_value
    return HttpResponse(h)

def resSimpCpp(request):
    p = subprocess.Popen (["./matefacil_demo/Programs/out1"],stdout=subprocess.PIPE, shell = True)
    m = p.communicate()[0].decode('utf-8')
    return HttpResponse(m)

def resCpp(request):
    p = subprocess.Popen (["./matefacil_demo/Programs/out2"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell = True)
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
    p = subprocess.Popen ([f'java matefacil_demo/Programs/HelloWorld {a1} {a2}'], stdout=subprocess.PIPE, shell = True)
    s = p.communicate(msj)[0].decode('utf-8')
    return HttpResponse(s)

def resC(request):
    p = subprocess.Popen (["./matefacil_demo/Programs/out3"], stdout=subprocess.PIPE, shell = True)
    s = p.communicate()[0].decode('utf-8')
    return HttpResponse(s)