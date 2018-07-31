from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from instagram.forms import Form, Article


# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-cdate')
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        print('PageNotAnInteger')
        articles = paginator.page(1)
    except EmptyPage:
        print('EmptyPage')
        articles = paginator.page(paginator.num_pages)

    return render(request, 'instagram/index.html', {'articles': articles})


def upload(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            new_form = Article(name=request.POST['name'],
                               photo=request.FILES['photo'],
                               contents=request.POST['contents'])
            new_form.save()

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

    return render(request, 'instagram/update.html', {'form': form})


def remove(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/instagram/')
