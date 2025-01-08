from django.shortcuts import render
# import django models
from .models import blog
from .forms import BlogForm , UserRegistrationForm
from django.shortcuts import get_list_or_404 ,redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')


def blog_list(request):
    blogs = blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})
  
  
@login_required  
def blog_create(request ):   
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})
  
from django.shortcuts import get_object_or_404, redirect

@login_required
def blog_edit(request, blog_id):
    blog_post = get_object_or_404(blog, pk=blog_id, user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog_post)
    return render(request, 'blog_form.html', {'form': form})
      
@login_required
def blog_delete(request,blog_id):
  blog_post = get_object_or_404(blog, pk=blog_id,user=request.user)
  if request.method == 'POST':
    blog_post.delete()
    return redirect('blog_list')
  
  return render(request, 'blog_confirm_delete.html', {'blog': blog})



def register (request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request, user)  # Log in the user and redirect to home page.
      return redirect('blog_list')
  else:
    form = UserRegistrationForm()
  return render(request, 'registration/register.html', {'form': form})
  
  
   