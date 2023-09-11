from django.shortcuts import render
from groups.models import group
from groups.forms import group_form
from django.shortcuts import redirect

# Create your views here.

def create_group(request):
    if request.method == 'POST':
        form = group_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups:show_groups')
    else:
        form = group_form()
    return render(request,'groups/create_groups.html',{'form':form})

def show_group(request):
    values = group.objects.all()
    return render(request,'groups/show_groups.html',{'values':values})
