# import the standard Django Forms
# from built-in library
from django import forms

FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


# creating a form
class InputForm(forms.Form):
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={"type": "date"}))
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES, required=False)
    favorite_color_one = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES
    )
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    profile_image = forms.FileField()

    agree = forms.BooleanField(label="Agree")
