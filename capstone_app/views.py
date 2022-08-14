from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    
)
from .models import Post1
from django.urls import reverse
from django.http import HttpResponseRedirect
from users.models import Movies, Profile2


# Create your views here.


def index(request):
    context = {
        'posts': Post1.objects.all(),

    }
    n = context.get(id=1)

    return render(request, 'index.html', context, n)


def about(request):
    return render(request, 'info.html')
def search(request):
    if request.method=='POST':
        searched =request.POST['searched']
        movies=Post1.objects.filter(title__contains=searched)
        return render(request, 'search.html',{'searched':searched,'movies':movies})
    else:
        return render(request, 'search.html')



"""def login(request):
    return render(request,'login.html')"""


class PostListView(ListView):
    model = Post1
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post1
    template_name = 'post1_detail.html'
    context_object_name = 'posts'
    def get_context_data(self,*args, **kwargs):
        context=super(DetailView,self).get_context_data()
        stuff=get_object_or_404(Post1, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        context['total_likes']=total_likes
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post1
    fields = ['title', 'content', 'movie_director', 'movie_actor', 'movie_length','movie_gne', 'image', 'movie_url']
    template_name = 'post1_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post1
    fields = ['title', 'content']
    template_name = 'post1_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def LikesView(request,pk):
    post=get_object_or_404(Post1,id=request.POST.get('movie_id'))
    post.movie_likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))