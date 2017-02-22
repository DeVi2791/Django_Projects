from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	nombre="Denisse Villamar"
	return HttpResponse('<h1>Hola Mundo, los saluda '+nombre+'</h1>')

