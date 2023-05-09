from loja.models import Item, Carrinho_Item
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

class ItemSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Item
        fields = '__all__'


class Carrinho_ItemSerializer(ModelSerializer):
    class Meta:
        model = Carrinho_Item
        fields = '__all__'

class Carrinho_Item_DetailSerializer(ModelSerializer):
    class Meta:
        model = Carrinho_Item
        fields = '__all__'
        depth = 1