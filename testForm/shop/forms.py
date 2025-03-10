from django import forms
from .models import Product
from django.core.exceptions import ValidationError
import string

def has_only_latin_letters(name):
    char_set = string.ascii_letters
    return all((True if x in char_set else False for x in name))
class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = "__all__"
        # widgets = {
        #     "name": forms.TextInput(attrs={"placeholder":"name"}),
        #     "price": forms.TextInput(attrs={"placeholder":"price"}),
        #     'sku': forms.TextInput(attrs={'placeholder': 'sku'})
        # }
        # Вказуємо кастомні повідомлення для пвених помилок для кожного поля
        # error_messages = {
        #     "sku": {
        #         "required": "Це поле обов'язкове для заповнення",
        #         "max_length": "Введено більше, ніж 8 символів"
        #     },
        #     'price':{
        #         'required': "Введіть сумму!"
        #     }
        # }
    def clean_sku(self):
        sku = self.cleaned_data.get("sku") 
        cont = False
        for element in sku:
            print(element)
            if not has_only_latin_letters(element) and not element.isdigit():
                cont = True
        if cont:
            print('huhhuhu')
            raise ValidationError("only latin and digit for sku")
        else:
            print('okay')
            return sku