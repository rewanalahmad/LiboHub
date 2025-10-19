from django import forms
from .models import Product,FeedBack,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        #widgits={'name':forms.TextInput(attrs={'placeholder':'product name'}) }
        
#(internal,and what it shows)
choices=[
    ('happy','Happy'),
    ('neutral','Neutral'),
    ('sad','Sad'),

]
class FeedbackForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    feedback=forms.CharField()
    satisfaction=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)

    def clean_email(self):
        email= self.cleaned_data['email']
        if '@gmail.com' not in email:
            raise forms.ValidationError('plase use your gmail')
        return email