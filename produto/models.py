from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao_curta = models.TextField(max_length=250)
    descricao_longa  = models.TextField()
    imagem  = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug  = models.SlugField(unique=True)
    preco_marketing  = models.FloatField()
    preco_marketing_promocional  = models.FloatField(default=0)


    @staticmethod
    def resize_image(img, new_width=800):
        print(img.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome