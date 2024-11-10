from django.shortcuts import render, redirect, get_object_or_404
from .models import Crud_Data

# Index view to display the form and existing data
def index(request):
    query = request.GET.get('search', '')  # Correct search implementation
    if query:
        all_data = Crud_Data.objects.filter(name__icontains=query)  # Use correct filter method
    else:
        all_data = Crud_Data.objects.all()
    return render(request, 'index.html', {'key': all_data})

# Insert data into the database
def inserdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        Crud_Data.objects.create(name=name, email=email)
        return redirect('index')  # Redirect after successful insertion

def data_delete(request, pk):
    if request.method == 'POST':  # Only allow delete on POST method for safety
        delete_data = get_object_or_404(Crud_Data, pk=pk)
        delete_data.delete()
    return redirect('index')

def updatePage(request, pk):
    get_data = get_object_or_404(Crud_Data, id=pk)
    return render(request, 'update.html', {'key': get_data})

def updateData(request, pk):
    if request.method == 'POST':  # Process only POST updates
        update_data = get_object_or_404(Crud_Data, id=pk)
        update_data.name = request.POST['name']
        update_data.email = request.POST['email']
        update_data.save()
    return redirect('index')
