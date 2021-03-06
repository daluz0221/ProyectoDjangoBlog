from django.urls import path
from .views import post_detail,  post_share, post_list

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    # path('', PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:posti>/', post_detail, name='post_detail'),    
    path('<int:post_id>/share/', post_share, name='post_share')
]