
from django import forms
from .models import Package, Category,ServiceProvider


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = [
            "package",
            "price"
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "category"
        ]



class ServiceForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = ServiceProvider

        # specify fields to be used
        fields = [
            "user_id",
            "company_name",
            "location",
            "contact_no",
            "desc",
            "package",
            "category",
            "image",
        ]
