from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def article(request):

    keyword=request.GET.get("keyword")

    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def index(request):
    context={
        "numbers":[1,2,3,4,5,6]
        
        
    }
    return render(request,"index.html",context=context)

def about(request):
    return render(request,"about.html")
"""def detail(request,id):
    return HttpResponse("Detail:" + str(id))"""
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context=context)
@login_required(login_url="user:login")
def addArticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article=form.save(commit=False) #yazar bilgisi olmadığı için hata veriyor, kaydetme diyoruz, aşağıda yazar ekliyoruz
        article.author=request.user
        article.save()
        messages.success(request,"Başarıyla makale oluşturuldu")
        return redirect("articles:dashboard")
        
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article=Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    comments=article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)

    if form.is_valid():

        article=form.save(commit=False) #yazar bilgisi olmadığı için hata veriyor, kaydetme diyoruz, aşağıda yazar ekliyoruz
        article.author=request.user
        article.save()
        messages.success(request,"Başarıyla makale güncellendi")
        return redirect("articles:dashboard")

    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale başarıyla silindi")

    return redirect("articles:dashboard")

def addComment(request,id):
    article=get_object_or_404(Article,id=id)
      
    if request.method=="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")

        newCommment=Comment(comment_author=comment_author,comment_content=comment_content)
        newCommment.article=article
        newCommment.save()

    return redirect(reverse("articles:detail",kwargs={"id":id}))


