from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def calkulator(request, a, b, c):
    print(a,b,c)
    # if c == '+':
    #   x = a + b
    # elif c == '-':
    #   x = a - b
    # elif c == '*':
    #  x = a * b
    # elif c == '/':
    #  x = a / b

    return render(request, 'calkulator.html',{'a':a,'b':b,'c':c})

# def users(request,name):
#     print(name)
#     return render(request, 'calkulator.html', {'user':name})