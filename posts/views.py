from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.views.generic import DetailView
from .models import Item


class PostDetail(DetailView):
    model = Item
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def post_delete(request, pk):
    if request.user.is_superuser:
        post = get_object_or_404(Item, id=pk)
        post.delete()

        messages.add_message(request, messages.SUCCESS,
                             f'Item {pk} deletado com sucesso!')
        return HttpResponseRedirect(reverse('home'))
    else:
        return redirect('/')
