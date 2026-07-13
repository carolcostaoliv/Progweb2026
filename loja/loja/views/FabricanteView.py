from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from loja.models.Fabricante import Fabricante


@login_required
def list_fabricante_view(request):
    fabricantes = Fabricante.objects.all()

    context = {
        'fabricantes': fabricantes
    }

    return render(
        request,
        template_name='fabricante/fabricante.html',
        context=context,
        status=200
    )


@login_required
def create_fabricante_view(request):

    if request.method == 'POST':
        nome_fabricante = request.POST.get('fabricante_nome')

        if nome_fabricante:
            Fabricante.objects.create(Fabricante=nome_fabricante)
            return redirect('fabricante')

    return render(
        request,
        template_name='fabricante/fabricante-create.html',
        status=200
    )


@login_required
def edit_fabricante_view(request, id):

    fabricante = get_object_or_404(Fabricante, id=id)

    if request.method == 'POST':
        nome_fabricante = request.POST.get('fabricante_nome')

        if nome_fabricante:
            fabricante.Fabricante = nome_fabricante
            fabricante.save()

            return redirect('fabricante')

    context = {
        'fabricante': fabricante
    }

    return render(
        request,
        template_name='fabricante/fabricante-edit.html',
        context=context,
        status=200
    )


@login_required
def delete_fabricante_view(request, id):

    fabricante = get_object_or_404(Fabricante, id=id)

    if request.method == 'POST':
        fabricante.delete()
        return redirect('fabricante')

    context = {
        'fabricante': fabricante
    }

    return render(
        request,
        template_name='fabricante/fabricante-delete.html',
        context=context,
        status=200
    )