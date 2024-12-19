from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()  # This will handle the file upload
