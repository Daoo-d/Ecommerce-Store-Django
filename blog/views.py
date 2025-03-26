from typing import Any
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Post,Comments
from django.views import View
from django.views.generic import ListView,DetailView
from .forms import commentForm
from django.db.models import Q

# Create your views here.   
class PostList(View):
    def  get(self,request,search_results=None):
        allPost = Post.objects.all().order_by('-date')
        newPost = allPost[:2] 
        return render(request,"blog/allPosts.html",{
            "newPost":newPost,
            "allPost":allPost,
            "search_result":search_results
        })  
    
class IndividualPost(View):
    def get(self,request,slug,search_results=None):
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
        newPost = Post.objects.all().order_by('-date')[:2]    

        return render(request,"blog/postDetails.html",{
            "newPost":newPost,
            "post":post,
            "post_tag":post.tag.all(),
            "comment_form": form,
            "post_comments":post.com_ments.all(),
            "next_post":next_post,
            "prev_post":prev_post,
            "search_result":search_results
        })
    
    def post(self,request,slug,search_results=None):
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
        newPost = Post.objects.all().order_by('-date')[:2]     
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details" ,args=[slug]))
        return render(request,"blog/postDetails.html",{
            "newPost":newPost,
            "post":post,
            "post_tag":post.tag.all(),
            "comment_form": form,
            "next_post":next_post,
            "prev_post":prev_post,
            "search_result":search_results
        })    
    
def search_blog(request,slug=None):
        query = request.GET.get('search_query') 
        if query:
            search_results = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains = query)
            )
            print(search_results)
            if slug:
                return IndividualPost.as_view()(request, slug=slug, search_results=search_results)
            else:
                return PostList.as_view()(request,search_results=search_results)
        return redirect("posts-page")