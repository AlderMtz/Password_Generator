from django.shortcuts import render
#from django.http import HttpResponse #pero no vamos a utilizar esta libreria sino paginas "html"
import random #importamos la funcion "random"


def home(request): #creamos la vista para la direccion 'home'
    return render(request, 'generator/home.html')

def about(request):   #creamos la vista para la direccion 'about'
    return render(request, 'generator/about.html')

def password(request): #creamos la vista para la direccion "password"
    
    characters = list('abcdefghijklmnñopqrstuvwxyz') #caracteres a utilizar para generar la contraseña
    generated_password = '' #var que va a guardar el resultado final
    length = int(request.GET.get('length')) #transformamos a "int" lo que obtenemos "GET" de la pagina y mediante la 
    #funcion "get" obtenemos el valor de 'length'

    if request.GET.get('uppercase') == 'on': #si en el "uppercase" se tiene el valor igual a "on" entonces:
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')) #extiende la lista "characters" con una lista de "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    if request.GET.get('special') == 'on': #hacemos lo mismo para las opciones de "caracteres especiales" y "numeros"
        characters.extend(list('-+/*#$%&/'))

    if request.GET.get('numbers') == 'on': #NOTA: EL NOMBRE QUE VA DENTRO DE "get('name')" ES EL VALOR DE "name"
        characters.extend(list('0123456789'))


    for x in range(length): #for con var x y limite igual a "length"
        generated_password += random.choice(characters) #random.choice() es una funcion que busca en la lista "characters" y elije uno por vuelta
    
    return render(request, 'generator/password.html', {'password': generated_password})#retornamos un diccionario con valor igual a "generated_password"
