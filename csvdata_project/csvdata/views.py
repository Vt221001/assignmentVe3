from django.shortcuts import render
from .forms import CSVUploadForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            # Read CSV using pandas
            df = pd.read_csv(csv_file)

            # Perform basic data analysis
            summary = df.describe()  # Summary statistics
            missing_data = df.isnull().sum()  # Missing values

            # Generate visualizations
            plots = generate_visualizations(df)  # Generate and save the plots

            # Return the data along with plots
            return render(request, 'csvdata/result.html', {
                'data': df.head(),
                'summary': summary,
                'missing_data': missing_data,
                'plots': plots  # Pass the plot file paths to the template
            })
    else:
        form = CSVUploadForm()
    return render(request, 'csvdata/upload.html', {'form': form})





def generate_visualizations(data):
    # Create a folder for saving the images (if it doesn't exist)
    if not os.path.exists('static/plots'):
        os.makedirs('static/plots')

    plots = []

    # Create a histogram for each numerical column
    for col in data.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(data[col], kde=True, bins=10, color='blue')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

        # Save the plot as an image
        plot_path = f'static/plots/{col}_histogram.png'
        plt.savefig(plot_path)
        plt.close()  # Prevent overlapping plots
        plots.append(f'plots/{col}_histogram.png')  # Save the relative path for rendering

    return plots
