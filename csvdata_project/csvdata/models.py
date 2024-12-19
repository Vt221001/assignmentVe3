from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='csv_files/')  # FileField to store CSV files
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Track the upload time

    def __str__(self):
        return self.file.name
