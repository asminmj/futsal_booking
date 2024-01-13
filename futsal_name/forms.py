from django import forms
from django.forms import ModelForm
from .models import Futsal, Futsalbookingdetail



#create a futsal form
class FutsalForm(ModelForm):
    class Meta:
        model = Futsal
        fields = ('name','address','zip_code','phone','web','email_address',)
        labels = {
			'name': '',
			'address': '',
			'web': '',
            'zip_code': '',
			'phone': '',
            'email_address': '',
				
		}

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Futsal Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Futsal Adress'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip_code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			
        }


#create a futsalbookingdetail form
class FutsalbookingdetailForm(ModelForm):
    class Meta:
        model = Futsalbookingdetail
        fields = ('name','booking_date','futsal','incharge','phone','rate','players',)
        labels = {
			'name': '',
			'booking_date': '',
			'futsal': '',
            'incharge': '',
			'phone': '',
            'rate': '',
            'players': '',
				
		}

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'booking_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'booking_date'}),
			'futsal': forms.Select(attrs={'class':'form-control', 'placeholder':'Futsal Name'}),
            'incharge': forms.Select(attrs={'class':'form-control', 'placeholder':'Game Incharge'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'rate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'rate'}),
            'players': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'players'}),
			
        }

