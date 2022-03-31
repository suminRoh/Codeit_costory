from django.views.generic import (
    CreateView,ListView,DetailView,UpdateView,DeleteView,RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm


class IndexRedirectView(RedirectView):
    pattern_name='post-list'
 
class PostListView(ListView):
    model=Post
    ordering=['-dt_created'] #정렬 최신순(-안붙일 경우 오래된 순)
    paginate_by=6
   

class PostDetailView(DetailView):
    model=Post
 

class PostCreateView(CreateView):
    model=Post
    form_class=PostForm 
  

    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk':self.object.id})



class PostUpdateView(UpdateView):
    model=Post
    form_class=PostForm

    def get_success_url(self) :
        return reverse('post-detail',kwargs={'pk':self.object.id})

class PostDeleteView(DeleteView):
    model=Post
 
    def get_success_url(self):
        return reverse('post-list')


