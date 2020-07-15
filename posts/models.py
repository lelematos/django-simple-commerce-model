from django.db import models
from django.urls import reverse

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from posts.signals import item_criado, item_deletado

TAMANHOS_CHOICES = [
    ('p', 'P'),
    ('m', 'M'),
    ('g', 'G'),
]


class Item(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=2000)
    data_publicacao = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    categoria = models.CharField(max_length=100, default='Descategorizado')
    publicado = models.BooleanField(default=True)

    # opicionais
    preco = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)
    preco_com_desconto = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)
    variacoes = models.BooleanField(default=False)

    # imagens (adicionar quantas quiser)
    img1 = models.ImageField(upload_to="static/uploaded_images",
                             height_field=None, width_field=None, max_length=None,
                             null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} | R$ {self.preco}'

    @property
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    @property
    def get_delete_url(self):
        return reverse("post_delete", kwargs={"pk": self.pk})

    @property
    def get_img_url(self):
        return f'/{self.img1}'


def f_item_criado(sender, **kwargs):
    item_criado.send(sender=sender)
    print('Sinal enviado')


def f_item_deletado(sender, **kwargs):
    item_deletado.send(sender=sender)
    print('Sinal enviado')


post_save.connect(f_item_criado, sender=Item)
post_delete.connect(f_item_deletado, sender=Item)

TIPOS_VARIACOES = [
    ("tamanho", "Tamanho"),
    ("sabor", "Sabor"),
    ("cor", "Cor"),
]


class VariacaoManager(models.Manager):
    def all(self):
        return super(VariacaoManager, self).filter(ativo=True)

    def disponiveis(self):
        return all().filter(disponivel=True)


class Variacao(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPOS_VARIACOES)
    preco = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    # pode ser controlada pela disponibilidade em estoque, continua aparecendo, mas como esgotada
    disponivel = models.BooleanField(default=True)

    ativo = models.BooleanField(default=False)

    objects = VariacaoManager()

    def __str__(self):
        return f'{self.item.titulo} | {self.nome}'
