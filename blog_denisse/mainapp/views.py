from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def index(request):
	title="Primer Post"
	body="Estamos aprendiendo a enviar datos dinamicos a los templates :D"
	context={
		'entry_title': title,
		'entry_body': body,
	}
	return render (request,"index.html",context)
	'''
class Entry (): # declaro el objeto
	def __init__(self,title,body,img_url):
		self.title=title
		self.body=body
		self.img_url=img_url
		
def index(request):
	entrys=[
		Entry("Primer Post","Aprendiendo a enviar datos dinamicos","https://k60.kn3.net/taringa/4/A/3/9/8/A/Valeryc/686.jpg"),
		Entry("Segundo Post","wuuu","http://static.notinerd.com/wp-content/uploads/2015/12/11121.jpg"),
	]
	entry_total=len(entrys)
	return render(request,"index.html",{'entrys':entrys,'entry_total':entry_total})
