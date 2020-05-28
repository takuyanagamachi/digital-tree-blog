from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('contact/', views.contact, name='contact'),
    path('contact/done/', views.done, name='done'),
    #コメント削除
    path('comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('like/', views.like, name='like'),

]