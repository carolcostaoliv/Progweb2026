from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from loja.models.Categoria import Categoria

@login_required
def list_categoria_view(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, template_name='categoria/categoria.html', context=context, status=200)

@login_required
def create_categoria_view(request):
    if request.method == 'POST':
        nome_categoria = request.POST.get('categoria_nome')
        if nome_categoria:
            Categoria.objects.create(Categoria=nome_categoria)
            return redirect('categoria')
            
    return render(request, template_name='categoria/categoria-create.html', status=200)

@login_required
def edit_categoria_view(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        nome_categoria = request.POST.get('categoria_nome')
        if nome_categoria:
            categoria.Categoria = nome_categoria
            categoria.save()
            return redirect('categoria')
            
    context = {
        'categoria': categoria
    }
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)

@login_required
def delete_categoria_view(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria')
        
    context = {
        'categoria': categoria
    }
    return render(request, template_name='categoria/categoria-delete.html', context=context, status=200)