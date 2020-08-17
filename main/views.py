from django.shortcuts import render
import pandas as pd


def home(request):
    df = pd.read_csv('/home/dmytro_b/Jupyter Files/udemy/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/Ecommerce Customers')

    labels = ['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership', 'Yearly Amount Spent']
    data = [df['Avg. Session Length'].max(), df['Time on App'].max(), df['Time on Website'].max(),
            df['Length of Membership'].max(), df['Yearly Amount Spent'].max()]

    context = {
        'labels': labels,
        'data': data
    }
    return render(request, 'index.html', context=context)
