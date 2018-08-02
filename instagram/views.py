import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from instagram.forms import Form, Article
from django.http import HttpResponse


# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-cdate')
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        print('PageNotAnInteger')
        items = paginator.page(1)
    except EmptyPage:
        print('EmptyPage')
        items = paginator.page(paginator.num_pages)

    return render(request, 'instagram/index.html', {'items': items, 'paginator': paginator})


def upload(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.name = request.POST['name']
            article.photo = request.FILES['photo']
            article.contents = request.POST['contents']
            article.save()

            return redirect('/instagram/')
    else:
        form = Form()

    return render(request, 'instagram/upload.html', {'form': form})


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'instagram/detail.html', {'article': article})


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = Form(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.name = request.POST['name']
            article.photo = request.FILES['photo']
            article.contents = request.POST['contents']
            article.save()

            return redirect('/instagram/')
    else:
        form = Form(instance=article)

    return render(request, 'instagram/upload.html', {'form': form})


def remove(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/instagram/')


def like(request):
    pk = request.POST.get('pk', None)
    article = Article.objects.get(pk=pk)
    article.like += 1
    article.save()

    context = {'pk': pk, 'like_count': article.like}

    return HttpResponse(json.dumps(context), content_type='application/json')
