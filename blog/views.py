from django.shortcuts import render, HttpResponse
import time
# Create your views here.




def show_time(requset):

    # return HttpResponse("Hello")
    t = time.ctime()

    return render(requset,"index.html",{"t":t}) #locals()