from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def render_shop(request):
    return render(request,'shop.html',{
        'products':Product.objects.all()
    })
@staff_member_required
def render_form(request):
    form = ProductForm()
    if request.method == 'POST':
        # Створюємо об'єкт форми та передаємо у неї дані та файлі, які користувач ввів у формі
        form = ProductForm(request.POST, request.FILES)
        # Перевірка валідності форми (усі дані введені вірно)
        if form.is_valid():
            # Збереження форми у БД (у підв'язану модель)
            form.save()
    else:
        form = ProductForm()
    return render(request,'form.html',{'form':form})
