from django.shortcuts import get_object_or_404, redirect, render
from .forms import PageForm
from .models import Page

# Create your views here.


def index(request):
    object_list = Page.objects.all()
    return render(request, 'Blog/home.html', {'object_list': object_list})


def read(request, page_id):
    object_detail = get_object_or_404(Page, id=page_id)
    return render(request, 'Blog/page_detail.html', {'object_detail': object_detail})


def create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-read', page_id=form.id)
    else:
        form = PageForm()
        return render(request, 'Blog/page_create.html', {'form': form})


def update(request, page_id):
    update_content = get_object_or_404(Page, id=page_id)

    if request.method == 'POST':
        form = PageForm(request.POST, instance=update_content)
        if form.is_valid():
            form.save()
            return redirect('page-read', page_id=update_content.id)
    else:
        form = PageForm(instance=update_content)
    return render(request, 'Blog/page_create.html', {'form': form})


def delete(request, page_id):
    object = get_object_or_404(Page, id=page_id)

    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'Blog/page_confirm.html', {'object': object})