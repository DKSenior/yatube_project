from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    """
    Вывести на экран главную страницу.

    :param request: HttpRequest
    :return: страница с шаблоном index.html
    """
    posts = Post.objects.order_by('-pub_date')[:10]

    templates = 'posts/index.html'

    context = {
        'posts': posts,
        'title': 'Главная страница',
    }
    return render(request, templates, context)


def groups_list(request):
    """
    Вывести на экран список созданных групп.

    :param request: HttpRequest
    :return: страница с шаблоном group_list.html
    """
    groups = Group.objects.order_by('title')[:10]

    templates = 'posts/group_list.html'

    context = {
        'groups': groups,
        'title': 'Группы'
    }
    return render(request, templates, context)


def group_posts(request, slug):
    """
    Вывести страницу с постами группы.

    :param request: HttpRequest
    :param slug: значение передается пользователем
    :return: страница с шаблоном index.html со списком постов группы
    """

    group = get_object_or_404(Group, slug=slug)

    templates = 'posts/index.html'

    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': group.title
    }
    return render(request, templates, context)
