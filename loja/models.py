from django.db import models
from django.core.exceptions import ValidationError
from uploader.models import Image

class Item(models.Model):
    nome_item = models.CharField(max_length=255, default='')
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return f'{self.nome_item} - {self.quantidade} - R${self.valor}'
    
def validar_quantidade(quantia, item_id):
    item = Item.objects.get(id=item_id)
    if quantia <= 0:
        raise ValidationError("A quantidade tem que ser maior que 0!")
    elif quantia > item.quantidade:
        raise ValidationError("A quantia no carrinho não pode exceder a quantia do item disponível no estoque!")

class Carrinho_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default='')
    quantidade = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Carrinho_Itens"

    def __str__(self):
        return f"{self.item.nome_item} - {self.quantidade}"
    
    def clean(self):
        validar_quantidade(self.quantidade, self.item.id)
