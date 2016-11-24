from django.shortcuts import render,HttpResponseRedirect,render_to_response


# Create your views here.

from models import *
def data(request):
    listAppend=[]
    for i in myCourses:
        listAppend.append(i)
    #return HttpResponseRedirect('/blog/entries/')

    return render_to_response('printData.html',{'listAppend':listAppend})

