from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver, Signal

item_criado = Signal()
item_deletado = Signal()
