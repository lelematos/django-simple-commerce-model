from django.shortcuts import render
from django.views.generic import ListView

from django.dispatch import receiver

from posts.models import Item
from posts.signals import item_criado, item_deletado


memoria_categorias = []
lista_items = []
memoria_queryset = Item.objects.all()
flag = 0
queryset_mudou = True


def identificaCategorias_e_Separa(queryset):
    # começa sempre vazio
    lista_items = []

    # criando uma lista para cada categoria
    for categoria in memoria_categorias:
        lista_items.append([])

    for item in queryset:
        if item.publicado:
            if str(item.categoria) not in memoria_categorias:
                memoria_categorias.append(str(item.categoria))
                lista_items.append([item])

            else:
                lista_items[memoria_categorias.index(
                    item.categoria)].append(item)

    for categoria, lista in zip(memoria_categorias, lista_items):
        if lista == []:
            memoria_categorias.remove(categoria)
            lista_items.remove(lista)

    return memoria_categorias, lista_items


def verificaQueryset(queryset):
    global memoria_queryset, queryset_mudou, memoria_categorias, lista_items

    if queryset_mudou:
        queryset_mudou = False
        # atualizado o valor da memoria do queryset
        memoria_queryset = queryset
        # executando rotina de separação do queryset
        memoria_categorias, lista_items = identificaCategorias_e_Separa(
            queryset)
        print(f'Algo esta diferente, {memoria_categorias, lista_items}\n')
    return memoria_categorias, lista_items


def listFromDict(dict):
    list_values = []
    list_keys = []
    print(dict)
    for key in dict:
        list_keys.append(key)
        list_values.append(dict[key])
    return list_keys, list_values


@receiver(item_criado)
def item_criado_receiver(sender, **kwargs):
    global queryset_mudou
    queryset_mudou = True
    print(f'Houve mudanças no queryset, {queryset_mudou}')


@receiver(item_deletado)
def item_deletado_receiver(sender, **kwargs):
    global queryset_mudou
    queryset_mudou = True
    print(f'Houve mudanças no queryset, {queryset_mudou}')


class Home(ListView):
    model = Item
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        global memoria_categorias, lista_items
        queryset = Item.objects.all()
        # if verificaQueryset(queryset) != None:
        memoria_categorias, lista_items = verificaQueryset(queryset)

        categorias_e_items = zip(memoria_categorias, lista_items)
        context['categorias_e_items'] = categorias_e_items
        return context
