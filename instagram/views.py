from django.shortcuts import render
from instagram.forms import Form, Article


# Create your views here.
def index(request):
    article_list = Article.objects.all()
    return render(request, 'instagram/index.html', {'article_list': article_list})


def upload(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            new_form = Article(name=request.POST['name'],
                               photo=request.FILES['photo'],
                               contents=request.POST['contents'])
            new_form.save()
    else:
        form = Form()

    return render(request, 'instagram/upload.html', {'form': form})
