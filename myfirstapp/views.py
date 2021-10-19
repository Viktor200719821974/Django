from django.shortcuts import render

def calkulator(request, a, b, c):
    print(a, b, c)
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '*':
        x = a * b
    elif c == ':':
        x = a / b

    return render(request, 'calkulator.html', {'a': a, 'b': b, 'c': c, 'x':x})

