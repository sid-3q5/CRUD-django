from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic.edit import UpdateView
from .models import List
from .forms import Student

# Create your views here.
def home(request):
    dataset = List.objects.order_by('id')
    p1 = 'Siddhant'
    p2 = 'Chauhan'
    p3 = 'India'
    p4 = 'Gittikhadan'
    p5 = 'Unmarried'
    p6 = 'IT'
    p7 = '63'
    context ={
        'dataset' : dataset,
        'p1':p1,
        'p2':p2,
        'p3':p3,
        'p4':p4,
        'p5':p5,
        'p6':p6,
        'p7':p7,
    }
 
    # add the dictionary during initialization
    # context["dataset"] = List.objects.all()

    return render(request, 'main/index.html', context)

def create(request):
    context ={}
 
    # add the dictionary during initialization
    form = Student(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form']= form
    return render(request, 'main/create.html', context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(List, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "main/delete.html", context)

def update(request, id):
    # emp = List.objects.get(id =id)
    # profile = List.objects.get(pk=emp)
    # dataset = List.objects.all()
    # form = Student(request.POST or None)
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(List, id = id)
 
    # pass the object as instance in form
    form = Student(request.POST or None, instance = obj)
    # context = {
    #     'emp' : emp,
    #     'dataset' : dataset,
    # }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request, 'main/update.html', context)