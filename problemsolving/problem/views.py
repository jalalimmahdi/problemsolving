from django.shortcuts import render

# Create your views here.
def view_problemlist(request):
    dataForHtml={
    'title':"this is the first page"
    }
    return render(request,'index.html',dataForHtml)
