from django.shortcuts import render

def index(request):
    return render(request, "appf/caltax.html")  # Render the HTML template

def anynumber(request,number):
    number=int(number)
    tax=number*0.15
    total=number+tax
    return render(request, "appf/result.html", {"total": total})

def taxrate(request):
    taxrate=15
    return render(request,"appf/taxrate.html",{"taxrate":taxrate})
