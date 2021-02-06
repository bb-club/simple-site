from rest_framework import serializers
from .models import SliderModel, Product, Category, News, SinglePage, IndexModel


class AbstractSerializer:
    translate_field = 'title'

    def translate(self, request, result, attr):
        if request and request.query_params['lang']:
            lang = request.query_params['lang']
            if lang != 'ru':
                result[attr] = result[f'{attr}_{lang}']
            result[f'{attr}_en'] = result[f'{attr}_ch'] = ''
        return result

    def to_representation(self, obj):
        res = self.translate(self.context.get("request"), super().to_representation(instance=obj), self.translate_field)
        return res


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IndexSerializer(AbstractSerializer, serializers.ModelSerializer):
    class Meta:
        model = IndexModel
        fields = '__all__'


class SlideSerializer(AbstractSerializer, serializers.ModelSerializer):
    class Meta:
        model = SliderModel
        fields = '__all__'


class ProductSerializer(AbstractSerializer, serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    translate_field = 'name'
    class Meta:
        model = Product
        fields = '__all__'


class NewsSerializer(AbstractSerializer, serializers.ModelSerializer):
    translate_field = 'text'
    class Meta:
        model = News
        fields = '__all__'


class PageSerializer(AbstractSerializer, serializers.ModelSerializer):
    translate_field = 'text'
    class Meta:
        model = SinglePage
        fields = '__all__'
