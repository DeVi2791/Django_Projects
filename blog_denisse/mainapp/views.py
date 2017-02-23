from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	nombre="Denisse Villamar"
	return render (request,"index.html")

