from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import Debate, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from politics.forms import CommentForm
from django.urls import reverse_lazy
from inspect import getcomments
from test.test_importlib.namespace_pkgs.project1 import parent

class IndexView(generic.ListView):
    template_name = 'politics/index.html'
    
    def get_queryset(self):
        return Debate.objects.all()
    
class DetailView(generic.DetailView):
    model = Debate
    template_name = 'politics/detail.html'
    

    
class DebateCreate(CreateView):
    model = Debate
    fields = ['username','title', 'description']
    
    
    

    
    
    
class ReplyCreate(CreateView):
    model = Comment
    fields = ['user', 'content', 'post','parent']
    success_url = reverse_lazy('politics:index')
    

class CommentCreate(CreateView):
    model = Comment 
    form_class = CommentForm
    
    success_url = reverse_lazy('politics:index')
    
    def add_comments(self, request, slug):
        post = get_object_or_404(Debate, slug=slug)
        if request.method == 'POST':
            form= CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post= post
                comment.save()
                return redirect('politics:detail', slug=post.slug)
            else:
                form = CommentForm() 
        
                template = 'politics/templates/politics/comment_form.html'
                context ={'form': form}
                return render(request, template, context)
