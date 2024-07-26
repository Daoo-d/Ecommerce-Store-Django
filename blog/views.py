from typing import Any
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Post,Comments
from django.views import View
from django.views.generic import ListView,DetailView
from .forms import commentForm

# Create your views here.   
class PostList(ListView):
    model = Post
    template_name = "blog/allPosts.html"
    ordering = ['-date']
    context_object_name = "allPost"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()  # Get the filtered queryset
        context["newPost"] = queryset[:2]  # Add newPost to context
        return context
    
class IndividualPost(View):
    def get(self,request,slug):
        form = commentForm()
        try:   
            post = Post.objects.get(slug=slug)
        except:
            return HttpResponse("failure")    
        try:
            next_post = post.get_next_by_date(author=post.author)
        except:
            next_post = {}  
        try:
            prev_post = post.get_previous_by_date(author=post.author)  # Get the previous post
        except:
            prev_post = {}   

        return render(request,"blog/postDetails.html",{
            "post":post,
            "post_tag":post.tag.all(),
            "comment_form": form,
            "post_comments":post.com_ments.all(),
            "next_post":next_post,
            "prev_post":prev_post
        })
    
    def post(self,request,slug):
        form = commentForm(request.POST)
        
        try:   
            post = Post.objects.get(slug=slug)
        except:
            return HttpResponse("failure")    
        try:
            next_post = post.get_next_by_date(author=post.author)
        except:
            next_post = {}  
        try:
            prev_post = post.get_previous_by_date(author=post.author)  # Get the previous post
        except:
            prev_post = {}    
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details" ,args=[slug]))
        return render(request,"blog/postDetails.html",{
            "post":post,
            "post_tag":post.tag.all(),
            "comment_form": form,
            "next_post":next_post,
            "prev_post":prev_post
        })    
    
def search_blog(request):
        query = request.GET.get('search_query') 
        print(query)
        return redirect("posts-page")