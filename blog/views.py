from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from .forms import EmailPostForm, CommentForm
from .models import Post, Comment

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
    post = get_object_or_404(Post, slug=posti,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    # Lista de comentarios activos para este post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # un comentario ha sido posteado
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # crea un objeto comentario pero no lo guarda en la base de datos aun
            new_comment = comment_form.save(commit=False)
            #Asigna el post actual al comentario
            new_comment.post = post
            # Guarda el comentario en la bas de datos
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,'blog/post/detail.html',{
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
        })


def post_share(request, post_id):
    #recupera el post por el id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False


    if request.method == 'POST':
        #el form fue recibido
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # el form pasó las validaciones
            cd  = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} te recomienda que leas {post.title}"
            message = f"Leer {post.title} en {post_url}\n\n" \
                       f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'daluz0221@gmail.com', [cd['to']])
            sent = True
            #...se envía el email
    else:
        form = EmailPostForm()
        
    return render(request, 'blog/post/share.html', {
            'post':post, 
            'form': form,
            'sent':sent
            }) 