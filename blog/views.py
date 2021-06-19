from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
#     object_list = Post.objects.filter(status='published')
#     paginator = Paginator(object_list, 3) #3 post por página
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         #si la página no es un integer reparte la primera página
#         posts = paginator.page(1)
#     except EmptyPage:
#         # si la página está fuera de rango, reparte la última página
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {
#         'page': page,
#         'posts': posts
#     })

def post_detail(request, year, month, day, posti):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    return render(request,'blog/post/detail.html',{'post': post})