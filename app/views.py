from django.shortcuts import render

# Create your views here.
def foo(request):
  return render(request, 'app/hello.html', {})

def test(request):
  x = 42
  return render(request, 'app/test.html', {'x': x})
