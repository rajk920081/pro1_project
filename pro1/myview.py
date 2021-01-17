
from django.shortcuts import HttpResponse

def hello1(req):
    name ="""Mohan <h1 style="color:red">Something</h1>
            <b>my name is raj</b>  <h2>my name is kuch aur</h2>
            <a href="https://www.google.com/">google</a>
            <a href="/ab/">about</a>
            
          """
    return HttpResponse(name)

def about(request):
    v ="""
    about page hai
    <a href="/s/">service</a>
    <a href="/">hello</a>
    """
    return HttpResponse(v)

def service(request):
    return HttpResponse("service page")



# HttpResponse always gives string to brower