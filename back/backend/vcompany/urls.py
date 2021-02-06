from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('categorylist/',
         views.CategoryListView.as_view(),
         name='category_list'),
    path('category/<pk>/',
         views.CategoryDetailView.as_view(),
         name='category_detail'),
    path('products/',
         views.ProductListView.as_view(),
         name='product_list'),
    path('products/<pk>/',
         views.ProductDetailView.as_view(),
         name='product_detail'),
    path('news/',
         views.NewsListView.as_view(),
         name='news_list'),
    path('news/<pk>/',
         views.NewsDetailView.as_view(),
         name='product_detail'),
    path('page/<pk>/',
         views.PageView.as_view(),
         name='product_detail'),
    path('sliders/',
         views.SliderListView.as_view(),
         name='slider_list'),
    path('index/',
         views.IndexListView.as_view(),
         name='index_list')
]