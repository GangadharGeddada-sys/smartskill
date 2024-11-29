from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'smartskill/home.html')

def result(request):
    # Dummy data for now
    recommendations = [
        {"skill": "Python", "resources": ["Learn Python", "Advanced Python"]},
        {"skill": "Data Analysis", "resources": ["Pandas Tutorial", "NumPy Guide"]},
    ]
    return render(request, 'smartskill/result.html', {"recommendations": recommendations})
