from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Entry
from .forms import EntryForm


# Create your views here.
		
def index(request):
	entrys = Entry.objects.all()
	entry_total=len(entrys)
	return render(request,"index.html",{'entrys':entrys,'entry_total':entry_total})

def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
	return redirect('index')
    else:
        form = EntryForm()

    return render(request, 'entry_form.html',{'form': form})

def edit_entry(request, id_entry):
    entry = Entry.objects.get(id = id_entry)
    if request.method == 'GET':
        form  = EntryForm(instance=entry)
    else:
        form  = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'entry_form.html', {'form':form})

def del_entry(request, id_entry):
    entry = Entry.objects.get(id = id_entry)
    if request.method=="POST":
        entry.delete()
        return redirect('index')
    return render(request,'entry_delete.html',{'entry':entry})
