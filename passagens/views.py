from django.shortcuts import render
from passagens.forms import PassagemForms   

def passagens(request):
    form = PassagemForms()
    context = { 'form':form }
    return render(request,'index.html',context )

def revisao_consulta(request):
    if request.method == "POST":
        form = PassagemForms(request.POST)
        context = { 'form':form }
        return render(request,'consulta.html',context )