from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for LearningLog"""
    return render(request, 'learning_logs/index.html')
