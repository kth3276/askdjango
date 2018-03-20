import os
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post

# Create your views here.

# def mysum(request, x, y=0, z=0):
#     # request: HttpRequest
#     return HttpResponse(int(x)+int(y)+int(z))


post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법 1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법 2)
            # post = Post(title = form.cleaned_data['title'],
            #             content=form.cleaned_data['content'])
            # post.save()

            # 방법 3)
            # post = Post.objects.create(title = form.cleaned_data['title'],
            #             content=form.cleaned_data['content'])

            # 방법 4)
            # post = Post.objects.create(**form.cleaned_data)

            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')  # namespace:name 형식도 가능
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')  # namespace:name 형식도 가능
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })


# 함수 기반 뷰 먼저 공부하고 클래스 기반 뷰로 넘어가기
def mysum(request, numbers):
    # numvers = "1/2/12/123"
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = '/dev/askdjango/ex.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'ex.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response




