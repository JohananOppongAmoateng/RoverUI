from django import forms

class FileUploadForm(forms.Form):
    input_file = forms.FileField(label='Choose JSON file')
    input_format = forms.ChoiceField(
        choices=[('json', 'JSON')],
        label='Select Input Format'
    )
    sites_per_topic = forms.IntegerField(
        initial=5, min_value=1, label='Sites per Topic',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
