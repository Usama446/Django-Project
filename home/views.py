from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is Home Page")

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<2 or len(phone)<2 or len(phone)<2:
            messages.error(request, 'Please fill the Form correctly')
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent')
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found.") 
    params = {'allPosts' : allPosts, 'query' : query}
    return render(request, 'home/search.html', params)
    # return HttpResponse("This is search")

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        #chech for error inputs
        if len(username) > 20:
            messages.error(request, "User name must be 20 characters.")
            return redirect('home')
        # if not username.isalnum():
        #     messages.error(request, "Username should contain alphabets and numbers.")
        #     return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Password do not match.")
            return redirect('home')
        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been successfully created.")
        return redirect('home')
    else:
        return HttpResponse("404 Error")

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In ")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try again.")
            return redirect('home')
    
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect('home')
    # return HttpResponse('404 - NotZXZXZX Found')