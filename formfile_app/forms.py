# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Person

from crispy_forms.layout import Layout, Submit, Row, Column

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

class PersonBasictForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'Jon'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Ivy'}))
    gender = forms.ChoiceField(label='Gender',choices=GENDER)
    age = forms.IntegerField(label='Age', widget=forms.TextInput(attrs={'placeholder': 10}))
    email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'jonivy@atos.net'}))
    phone_no = forms.IntegerField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 12345678901}))


    class Meta:
        model = Person
        fields = ('first_name','last_name','gender', 'age', 'email','phone_no')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post' # get or post
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'gender',
            'age',
            'email',
            'phone_no',
            Submit('submit', 'Save & Next')
        )
