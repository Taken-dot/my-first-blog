from django.shortcuts import render
from .models import Post, Profile, Project, Skill, Experience
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html')

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render ( request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete ( request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST": # using post to avoid deleting via link
     post.delete()
     return redirect ('post_list') #after deleting post sending user back to post list page
    return render ( request, 'blog/post_delete.html', {'post' : post} )

def portfolio(request):
    profile = Profile.objects.first()
    projects = Project.objects.filter(is_featured=True)
    experiences = Experience.objects.all().order_by('-start_date')

    context = {
        'profile': profile,
        'projects': projects,
        'skills': Skill.objects.all().order_by('category', 'order'),
        'experiences': experiences
    }
    return render(request, 'blog/portfolio.html', context)



