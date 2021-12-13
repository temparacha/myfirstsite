from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

from django import forms
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = AddCommentForm
    # fields = ('name', 'body')

    def form_valid(self, form):
        # self.object = form.save(commit=False)
        print(self.kwargs)
        form.instance.post_id = self.kwargs['pk']
        form.instance.save()
        return super(AddCommentView, self).form_valid(form)


