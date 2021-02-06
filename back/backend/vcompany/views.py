from rest_framework import generics
from .models import SliderModel, Product, Category, News, SinglePage, IndexModel
from .serializers import ProductSerializer, CategorySerializer, NewsSerializer, SlideSerializer, PageSerializer, IndexSerializer
from rest_framework.pagination import PageNumberPagination


class SmallPagesPagination(PageNumberPagination):
    page_size = 10


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related('category').filter(status='published').order_by('created').all()
    serializer_class = ProductSerializer
    pagination_class = SmallPagesPagination

    def get_queryset(self):
        filter_qs = self.request.GET.getlist('category')
        queryset = super().get_queryset()
        if 'category' in self.request.query_params:
            queryset = queryset.filter(category__in=filter_qs)
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        filter_qs = self.request.GET.getlist('category')
        queryset = super().get_queryset()
        if 'category' in self.request.query_params:
            queryset = queryset.filter(category__in=filter_qs)
        return queryset


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class SliderListView(generics.ListAPIView):
    queryset = SliderModel.objects.filter(status='published').all()
    serializer_class = SlideSerializer


class IndexListView(generics.ListAPIView):
    queryset = IndexModel.objects.filter(status='published').all()
    serializer_class = IndexSerializer


class PageView(generics.RetrieveAPIView):
    queryset = SinglePage.objects.all()
    serializer_class = PageSerializer


