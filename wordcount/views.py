from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        txt = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'media/'+uploaded_file.name),'r')
        text = txt.read()
    else:
        text = request.GET['fulltext']
    words = text.split()
    word_dictionary={}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})