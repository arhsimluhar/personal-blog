from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    from_email = forms.EmailField()
    to_email = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
