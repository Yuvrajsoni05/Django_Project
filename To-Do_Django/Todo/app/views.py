from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from app.forms import TODOForm
from app.models import TODO




@login_required(login_url='user_login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        return render(request, 'home.html',context={'form':form , 'todos':todos})




def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('user_login')
    context = {"form": form}
    return render(request, 'signup.html', context=context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, 'login.html', context=context)


@login_required(login_url='user_login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()  # Save the todo item to the database
            return redirect("home")
        else:
            return render(request, 'home.html', context={'form': form})

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect("user_login")


def delete(request, id):
    print(id)
    TODO.objects.get(pk = id ).delete()
    return redirect('home')



def change_status(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')





