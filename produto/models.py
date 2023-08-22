from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao_curta = models.TextField(max_length=250)
    descricao_longa  = models.TextField(max_length=250)
    imagem  = models.ImageField(upload_to='produto_imagens/Y%/%m/', blank=True, null=True)
    slug  = models.SlugField(unique=True)
    preco_marketing  = models.FloatField()
    preco_marketing_promocional  = models.FloatField(default=0)