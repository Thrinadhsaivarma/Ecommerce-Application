from django.shortcuts import redirect, render

from app.models import Product

# Create your views here.
def index(request):
    data=Product.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        model=request.POST.get('model')
        ram=request.POST.get('ram')
        price=request.POST.get('price')
        query=Product(name=name,model=model,ram=ram,price=price)
        query.save()
    return render(request,"index.html")
def updateData(request,id):
    d=Product.objects.get(id=id)
    context={"d":d}

    if request.method=="POST":
        name=request.POST.get('name')
        model=request.POST.get('model')
        ram=request.POST.get('ram')
        price=request.POST.get('price')

        edit=Product.objects.get(id=id)
        edit.name=name
        edit.model=model
        edit.ram=ram
        edit.price=price
        edit.save()
        
        return redirect("/")
    return render(request,"edit.html",context)
     
def deleteData(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    return redirect("/")