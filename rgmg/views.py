from django.shortcuts import render, redirect
from rgmg.models import  Tabla, SeleccionTipo 

import random, decimal

from bokeh.plotting import figure, gridplot 
from bokeh.embed import components
from bokeh.models import Legend, LegendItem

import numpy as np
from scipy import stats

import scipy.special

from bokeh.layouts import gridplot




class Contador(object):
    
    def __init__(self, inicial = 0,v = 0,vv = "",mmm= [],raiz = 0,c = 0,f = 0,g = 0,tp = [], m1 = [], m2 = [],m3 = [],m4 = [],m5 = [],m6 = [],m7 = []):
        self.numero = inicial
        self.control = c
        self.full = f
        self.memoria1 = m1
        self.memoria2 = m2
        self.memoria3 = m3
        self.memoria4 = m4
        self.memoria5 = m5
        self.memoria6 = m6
        self.memoria7 = m7
        self.grafica = g
        self.tipo = tp       
        self.matriz = mmm      
        self.validador = v
      
        self.vector = vv

    def siguiente(self):
        self.numero += 1
        return self.numero

    def imprimir(self):
        print(self.numero)

    def inicioPagina(self):
        Tabla.objects.all().delete()
        contador.numero = 0
        contador.control = 0
        contador.full = 0
        contador.memoria1.clear()
        contador.memoria2.clear()
        contador.memoria3.clear()
        contador.memoria4.clear()
        contador.memoria5.clear()
        contador.memoria6.clear()
        contador.memoria7.clear()
        contador.tipo.clear()
        contador.matriz.clear()
   
        contador.validador = 0
        contador.vector = ""
        SeleccionTipo.objects.all().delete()

   

contador = Contador()

def inicio(request):
    #LO QUE SALE EN ROJO ES UN ERROR VISUAL DEL VISUAL CODE STUDIO CON LOS MODELOS  
    tamaño = 1000
    if contador.numero == 0:
        contador.inicioPagina()
        for i in range(0,tamaño): 
            contador.memoria1.append(i)
            registro = Tabla(tiempo = contador.memoria1[i])
            registro.save()
            contador.control = 1             
        contador.siguiente()
        print("CONTADOR UNICO:",end= " ")
        contador.imprimir()   

    if(request.POST.get('Discreta')):       
        print("CONTADOR DISCRETA:",end= " ")     
        contador.siguiente()
        contador.imprimir()        
        if contador.numero >= 2 and contador.full == 0:            
            for i in range(0,tamaño):   
                if contador.numero == 2:                  
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0 
                        contador.tipo.append("Discreto") 
                    rnd = random.randint(0,500)
                    contador.memoria2.append(rnd)    
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i])
                    registro.save() 
                if contador.numero == 3:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1 
                        contador.tipo.append("Discreto")
                    rnd = random.randint(0,500)
                    contador.memoria3.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i])
                    registro.save() 
                if contador.numero == 4:
                    if contador.control == 1:
                        Tabla.objects.all().delete()                        
                        contador.control = 0
                        contador.tipo.append("Discreto")
                    rnd = random.randint(0,500)
                    contador.memoria4.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i])
                    registro.save() 
                if contador.numero == 5:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1 
                        contador.tipo.append("Discreto")
                    rnd = random.randint(0,500)
                    contador.memoria5.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i])
                    registro.save() 
                if contador.numero == 6:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0
                        contador.tipo.append("Discreto")
                    rnd = random.randint(0,500)
                    contador.memoria6.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i])
                    registro.save() 
                if contador.numero == 7:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1
                        contador.tipo.append("Discreto")
                    rnd = random.randint(0,500)
                    contador.memoria7.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save() 
                    if i == (tamaño-1):       
                        contador.numero = 1
                        contador.full = 1
        if contador.numero >= 2 and contador.full == 1:            
            for i in range(0,tamaño):   
                if contador.numero == 2:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0
                        contador.tipo[0] = "Discreto"                
                    rnd = random.randint(0,500)
                    contador.memoria2[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 3:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1        
                        contador.tipo[1] = "Discreto"            
                    rnd = random.randint(0,500)
                    contador.memoria3[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save() 
                if contador.numero == 4:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0  
                        contador.tipo[2] = "Discreto"                  
                    rnd = random.randint(0,500)
                    contador.memoria4[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 5:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1    
                        contador.tipo[3] = "Discreto"                
                    rnd = random.randint(0,500)
                    contador.memoria5[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 6:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0          
                        contador.tipo[4] = "Discreto"         
                    rnd = random.randint(0,500)
                    contador.memoria6[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 7:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1      
                        contador.tipo[5] = "Discreto"             
                    rnd = random.randint(0,500)
                    contador.memoria7[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                    if i == (tamaño-1):       
                        contador.numero = 1
                        contador.full = 1
    if(request.POST.get('Continua')):       
        print("CONTADOR CONTINUA:",end= " ")     
        contador.siguiente()
        contador.imprimir()        
        if contador.numero >= 2 and contador.full == 0:            
            for i in range(0,tamaño):   
                if contador.numero == 2:                  
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0 
                        contador.tipo.append("Continuo") 
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria2.append(rnd)    
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i])
                    registro.save() 
                if contador.numero == 3:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1 
                        contador.tipo.append("Continuo") 
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria3.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i])
                    registro.save() 
                if contador.numero == 4:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0
                        contador.tipo.append("Continuo") 
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria4.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i])
                    registro.save() 
                if contador.numero == 5:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1 
                        contador.tipo.append("Continuo") 
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria5.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i])
                    registro.save() 
                if contador.numero == 6:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0
                        contador.tipo.append("Continuo") 
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria6.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i])
                    registro.save() 
                if contador.numero == 7:
                    if contador.control == 0:
                        contador.tipo.append("Continuo") 
                        Tabla.objects.all().delete()
                        contador.control = 1
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria7.append(rnd) 
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save() 
                    if i == (tamaño-1):       
                        contador.numero = 1
                        contador.full = 1
        if contador.numero >= 2 and contador.full == 1:            
            for i in range(0,tamaño):   
                if contador.numero == 2:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0   
                        contador.tipo[0] = "Continuo"                  
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria2[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 3:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1    
                        contador.tipo[1] = "Continuo"                
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria3[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save() 
                if contador.numero == 4:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0       
                        contador.tipo[2] = "Continuo"             
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria4[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 5:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1    
                        contador.tipo[3] = "Continuo"                
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria5[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 6:
                    if contador.control == 1:
                        Tabla.objects.all().delete()
                        contador.control = 0  
                        contador.tipo[4] = "Continuo"                 
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria6[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                if contador.numero == 7:
                    if contador.control == 0:
                        Tabla.objects.all().delete()
                        contador.control = 1 
                        contador.tipo[5] = "Continuo"                  
                    rnd = float(decimal.Decimal(random.randrange(0, 50000)/100))
                    contador.memoria7[i] = rnd
                    registro = Tabla(tiempo = contador.memoria1[i], columnaA = contador.memoria2[i],columnaB = contador.memoria3[i],columnaC = contador.memoria4[i],columnaD = contador.memoria5[i],columnaE = contador.memoria6[i],columnaF = contador.memoria7[i])
                    registro.save()
                    if i == (tamaño-1):       
                        contador.numero = 1
                        contador.full = 1
                    

    if(request.POST.get('BorrarTodo')):              
        contador.inicioPagina()        
        print("CONTADOR BORRAR:",end= " ") 
        contador.imprimir()     

    contexto = {
        "Tabla":Tabla.objects.all()
        }
    
    return render(request, 'index.html', contexto)



def tablas(request):

    tamaño = 1000
    contexto = {
        "Tabla":Tabla.objects.all()[tamaño-10:tamaño]

        }
    return render(request, 'tables.html',contexto)

def minimos_cuadrados(vectorx, vectory):
    vectorx = np.array(vectorx)
    vectory = np.array(vectory)
    
    sumatoria_x = sum(vectorx)
    sumatoria_y = sum(vectory)
    sumatoria_xx = sum(vectorx ** 2) 
    sumatoria_xy = sum(vectorx * vectory)
    promedio_x = sumatoria_x / len(vectorx)
    promedio_y = sumatoria_y / len(vectory)

    m = (sumatoria_xy-((sumatoria_x*sumatoria_y)/len(vectorx))) / (sumatoria_xx - ((sumatoria_x**2)/(len(vectorx))))
    b = promedio_y - (m * promedio_x)
    contador.matriz[0][0] = m
    contador.matriz[0][1] = b
   
    recta_ajustada = (m * vectorx) + b
    
    
    

    return recta_ajustada


                                                             

def error_ajuste(vector_x, vector_error, columna, color_barras):

    TOOLS="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair,save"
    grafica_error = figure(
        tools=TOOLS, 
        title="Tasas de error de "+columna+" frente al "+columna+" Modelado",
        x_axis_label='Entrada',
        y_axis_label='Salida',
        toolbar_location="right",
        plot_width=700, plot_height=494) 

    grafica_error.vbar(x=vector_x, top=vector_error, width=0.5, color=color_barras)
   

    return grafica_error

def grafico_histograma(vector_x, color_barras, contorno):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    k=0

    for j in vector_x:
        if(j<=50): 
            a+=1
        elif(j>50 and j<=100): 
            b+=1
        elif(j>100 and j<=150): 
            c+=1
        elif(j>150 and j<=200): 
            d+=1
        elif(j>200 and j<=250): 
            e+=1
        elif(j>250 and j<=300): 
            f+=1
        elif(j>300 and j<=350): 
            g+=1
        elif(j>350 and j<=400): 
            h+=1
        elif(j>400 and j<=450): 
            i+=1
        elif(j>450 and j<=500):  
            k+=1

    frecuencia_rango=[0,50,100,150,200,250,300,350,400,450,500]
    ocurrecias_rango=[a,b,c,d,e,f,g,h,i,k] 

    TOOLS="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair,save"
    histograma = figure(
        tools=TOOLS, 
        title="Frecuencia de Rangos",
        x_axis_label='Entrada',
        y_axis_label='Salida',
        toolbar_location="right",
        plot_width=700, plot_height=494)
    histograma.vbar(x=frecuencia_rango, top=ocurrecias_rango, width=50, color=contorno, fill_color=color_barras)   
    print(ocurrecias_rango)
    return histograma


def plotG(columna):
    TOOLS="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair,save"
    plot = figure(
        tools=TOOLS, 
        title="Grafico y Ajuste de la "+columna,
        x_axis_label='Entrada',
        y_axis_label='Salida',
        toolbar_location="right",
        plot_width=700, plot_height=453)
        
    return plot

def plotGraph(columna):
    
    TOOLS="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair,save"
    plot = figure(
        tools=TOOLS, 
        title="Grafico del "+columna,
        x_axis_label='Entrada',
        y_axis_label='Salida',
        toolbar_location="right",
        plot_width=1100, 
        plot_height=600)
        
    return plot


def make_plot(title, vector, hist, edges, x, color):
  
    TOOLS="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair,save"
    p = figure(
        tools=TOOLS, 
        title= title+" "+vector,
        x_axis_label='Conjuntos de numeros (rango 50)',
        y_axis_label='Cantidad',
        toolbar_location="right",
    
        plot_width=700, plot_height=453)
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color=color, line_color="white", alpha=0.5
           )


    p.y_range.start = 0
 
   
    #HACE QUE NO SE VEA LA CUADRICULA DE FONDO
    #p.grid.grid_line_color="white"
    return p
    
def modelo(request):
    tamaño = 1000
    entrada = []
    salida1 = []
    salida2 = []
    salida3 = []
    salida4 = []
    salida5 = []
    salida6 = []
    titulo = 0  
    
    for i in Tabla.objects.all():
        entrada = np.append(entrada, i.tiempo)      
        salida1 = np.append(salida1, i.columnaA)
       
        salida2 = np.append(salida2, i.columnaB)
        salida3 = np.append(salida3, i.columnaC)
        salida4 = np.append(salida4, i.columnaD)
        salida5 = np.append(salida5, i.columnaE)
        salida6 = np.append(salida6, i.columnaF)

    if contador.validador == 0:
        contador.matriz.append([-10,-10])        
        
        contador.validador = 1

     
        
    
    TOOLS="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair,save"
    plot = plotG("Vector A")
    plot2 = plotG("Vector B")
    plot3 = plotG("Vector C")
    plot4 = plotG("Vector D")
    plot5 = plotG("Vector E")
    plot6 = plotG("Vector F")


    #plot.line(entrada, salida1, line_width=2,legend="Columna A",line_color="red")
    plot.circle(entrada, salida1, legend="Columna A", size = 6, color = 'red')
    recta_ajustada = [-10]
    script, div = components(plot)
    numeroRMSE = 0
    matrizfit = []
    matrizerr = []
    scriptError, divError = components(error_ajuste(entrada,recta_ajustada,"Vector A", "red"))


    if(request.POST.get('columnaA')): 
        plot.circle(entrada, salida1, legend="Columna A", size = 6, color = 'red')
        #plot.line(entrada, salida1, line_width=2,legend="Columna A",line_color="red")        
        recta_ajustada = minimos_cuadrados(entrada,salida1) 
        plot.line(entrada, recta_ajustada, legend_label="Ajuste", line_width=3, line_color="black")
        script, div = components(plot)      
        titulo = 1
        #Indice de erros nube de puntos vs. recta
        errores = abs(salida1-recta_ajustada)
        scriptError, divError = components(error_ajuste(entrada,errores,"Vector A", "red"))
        
      
        numeroRMSE = ((sum(errores**2)) / (len(entrada)))**0.5  
        for i in range(1000):
            matrizfit.append([i,recta_ajustada[i]])
        for i in range(1000):
            matrizerr.append([i,errores[i]])


    if(request.POST.get('columnaB')):                        
        #plot2.line(entrada, salida2, line_width=2,legend="Columna B",line_color="blue")
        plot2.circle(entrada, salida2, legend="Columna B", size = 6, color = 'blue')
        recta_ajustada = minimos_cuadrados(entrada,salida2)   
        plot2.line(entrada, recta_ajustada, legend_label="Ajuste", line_width=3, line_color="black")
        script, div = components(plot2)
     
      
        titulo = 2

        #Indice de erros nube de puntos vs. recta
        errores = abs(salida2-recta_ajustada)
        scriptError, divError = components(error_ajuste(entrada,errores,"Vector B", "blue"))      

        numeroRMSE = ((sum(errores**2)) / (len(entrada)))**0.5       
        for i in range(1000):
            matrizfit.append([i,recta_ajustada[i]])
        for i in range(1000):
            matrizerr.append([i,errores[i]])
     
    if(request.POST.get('columnaC')):                        
        #plot3.line(entrada, salida3, line_width=2,legend="Columna C",line_color="yellow")
        plot3.circle(entrada, salida3, legend="Columna C", size = 6, color = 'yellow')
        recta_ajustada = minimos_cuadrados(entrada,salida3)   
        plot3.line(entrada, recta_ajustada, legend_label="Ajuste", line_width=3, line_color="black")
        script, div = components(plot3) 

       

        titulo = 3

        #Indice de erros nube de puntos vs. recta
        errores = abs(salida3-recta_ajustada)
        scriptError, divError = components(error_ajuste(entrada,errores,"Vector C", "yellow"))        
    
        numeroRMSE = ((sum(errores**2)) / (len(entrada)))**0.5 
        for i in range(1000):
            matrizfit.append([i,recta_ajustada[i]])
        for i in range(1000):
            matrizerr.append([i,errores[i]])

    if(request.POST.get('columnaD')):                        
        #plot4.line(entrada, salida4, line_width=2,legend="Columna D",line_color="orange")
        plot4.circle(entrada, salida4, legend="Columna D", size = 6, color = 'orange')
        recta_ajustada = minimos_cuadrados(entrada,salida4)   
        plot4.line(entrada, recta_ajustada, legend_label="Ajuste", line_width=3, line_color="black")
        script, div = components(plot4)

   
    
        titulo = 4

        #Indice de erros nube de puntos vs. recta
        errores = abs(salida4-recta_ajustada)
        scriptError, divError = components(error_ajuste(entrada,errores,"Vector D", "orange"))
        
     
        numeroRMSE = ((sum(errores**2)) / (len(entrada)))**0.5 
        for i in range(1000):
            matrizfit.append([i,recta_ajustada[i]])
        for i in range(1000):
            matrizerr.append([i,errores[i]])
    
    if(request.POST.get('columnaE')):                        
        #plot5.line(entrada, salida5, line_width=2,legend="Columna E",line_color="green")
        plot5.circle(entrada, salida5, legend="Columna E", size = 6, color = 'green')
        recta_ajustada = minimos_cuadrados(entrada,salida5)   
        plot5.line(entrada, recta_ajustada, legend_label="Ajuste", line_width=3, line_color="black")
        script, div = components(plot5)

      
  
        titulo = 5

        #Indice de erros nube de puntos vs. recta
        errores = abs(salida5-recta_ajustada)
        scriptError, divError = components(error_ajuste(entrada,errores,"Vector E", "green"))
        
 
        numeroRMSE = ((sum(errores**2)) / (len(entrada)))**0.5
        for i in range(1000):
            matrizfit.append([i,recta_ajustada[i]])
        for i in range(1000):
            matrizerr.append([i,errores[i]]) 
       
    if(request.POST.get('columnaF')):                        
        #plot6.line(entrada, salida6, line_width=2,legend="Columna F",line_color="brown")
        plot6.circle(entrada, salida6, legend="Columna F", size = 6, color = 'brown')
        recta_ajustada = minimos_cuadrados(entrada,salida6)   
        plot6.line(entrada, recta_ajustada, legend_label="Ajuste", line_width=3, line_color="black")
        script, div = components(plot6) 

    
    
        titulo = 6

        #Indice de erros nube de puntos vs. recta
        errores = abs(salida6-recta_ajustada)
        scriptError, divError = components(error_ajuste(entrada,errores,"Vector F", "brown"))
        
      
        numeroRMSE = ((sum(errores**2)) / (len(entrada)))**0.5 
        for i in range(1000):
            matrizfit.append([i,recta_ajustada[i]])
        for i in range(1000):
            matrizerr.append([i,errores[i]])
    
    

    diccionario = {
        "script": script, 
        'div':div,
        "scriptError": scriptError, 
        "divError":divError, 
        "matrizError": matrizerr[tamaño-10:tamaño],
        "rmse": numeroRMSE,

        "columna":matrizfit[tamaño-10:tamaño],
        "Titulo": titulo, 
        "salida":salida1, 
        "M": contador.matriz[0][0], 
        "B":contador.matriz[0][1]
    }
    return render(request, 'buttons.html' , diccionario)

  


def grafico(request):

    entrada = []
    salida1 = []
    salida2 = []
    salida3 = []
    salida4 = []
    salida5 = []
    salida6 = []
   
    for i in Tabla.objects.all():
        entrada.append(i.tiempo)
        salida1.append(i.columnaA)
        salida2.append(i.columnaB)
        salida3.append(i.columnaC)
        salida4.append(i.columnaD)
        salida5.append(i.columnaE)
        salida6.append(i.columnaF) 

    
    
    plot = plotGraph("Vector A")
    plot2 = plotGraph("Vector B")
    plot3 = plotGraph("Vector C")
    plot4 = plotGraph("Vector D")
    plot5 = plotGraph("Vector E")
    plot6 = plotGraph("Vector F")
    
    
    titulo = 0
    plot.line([], [], line_width=2,legend="Columna A",line_color="red")
    script, div = components(plot)
        

      
    if(request.POST.get('columnaA')):    
        if salida1[0] != -10:    
            titulo = 1                                  
            plot.line(entrada, salida1, line_width=2,legend="Columna A",line_color="red")
            script, div = components(plot)               
        

    if(request.POST.get('columnaB')): 
        if salida2[0] != -10:       
            titulo = 2                              
            plot2.line(entrada, salida2, line_width=2,legend="Columna B",line_color="blue")
            script, div = components(plot2)
                               
        
     
    if(request.POST.get('columnaC')):  
      
        if salida3[0] != -10:   
            titulo = 3                                   
            plot3.line(entrada, salida3, line_width=2,legend="Columna C",line_color="yellow")
            script, div = components(plot3)                     
        

    if(request.POST.get('columnaD')):
        
        if salida4[0] != -10: 
            titulo = 4                                        
            plot4.line(entrada, salida4, line_width=2,legend="Columna D",line_color="orange")
            script, div = components(plot4)                   
        
    
    if(request.POST.get('columnaE')):
           
        if salida5[0] != -10:  
            titulo = 5                                  
            plot5.line(entrada, salida5, line_width=2,legend="Columna E",line_color="green")
            script, div = components(plot5)                    
        
       
    if(request.POST.get('columnaF')):
        
        if salida6[0] != -10:     
            titulo = 6                                   
            plot6.line(entrada, salida6, line_width=2,legend="Columna F",line_color="brown")
            script, div = components(plot6)   

    
    
    return render(request, 'charts.html' , {'script': script, 'div':div, 'Titulo':titulo})
 


def analisis(request):
    tamaño = 1000

    entrada = []
    salida1 = []
    salida2 = []
    salida3 = []
    salida4 = []
    salida5 = []
    salida6 = []
   
    
    for i in Tabla.objects.all():
        entrada = np.append(entrada, i.tiempo)      
        salida1 = np.append(salida1, i.columnaA)
       
        salida2 = np.append(salida2, i.columnaB)
        salida3 = np.append(salida3, i.columnaC)
        salida4 = np.append(salida4, i.columnaD)
        salida5 = np.append(salida5, i.columnaE)
        salida6 = np.append(salida6, i.columnaF)

    promedio = -10
    moda = -10
    mediana = -10 
    varianza = -10
    desviacionEstandar = -10
    maximo = -10
    minimo = -10
    tipo = " "
    titulo = -10

    if(request.POST.get('columnaA')):
        tipo = contador.tipo[0]
        promedio = np.around((np.mean(salida1)), decimals= 4)
        moda = stats.mode(salida1)[0][0]        
        mediana = np.around((np.median(salida1)), decimals= 4)        
        varianza = np.around((np.var(salida1)), decimals= 4)
        desviacionEstandar = np.around((np.std(salida1)), decimals= 4)
        maximo = max(salida1)        
        minimo = min(salida1)
        titulo = 1   
        

    if(request.POST.get('columnaB')): 
        tipo = contador.tipo[1]
        promedio = np.mean(salida2)
        moda = stats.mode(salida2)[0][0]
        mediana = np.around((np.median(salida2)), decimals= 4)        
        varianza = np.around((np.var(salida2)), decimals= 4)
        desviacionEstandar = np.around((np.std(salida2)), decimals= 4)
        maximo = max(salida2)
        minimo = min(salida2)
        titulo = 2 

    if(request.POST.get('columnaC')): 
        tipo = contador.tipo[2]
        promedio = np.mean(salida3)
        moda = stats.mode(salida3)[0][0]
        mediana = np.around((np.median(salida3)), decimals= 4)        
        varianza = np.around((np.var(salida3)), decimals= 4)
        desviacionEstandar = np.around((np.std(salida3)), decimals= 4)
        maximo = max(salida3)
        minimo = min(salida3)
        titulo = 3

    if(request.POST.get('columnaD')): 
        tipo = contador.tipo[3]
        promedio = np.mean(salida4)
        moda = stats.mode(salida4)[0][0]
        mediana = np.around((np.median(salida4)), decimals= 5)        
        varianza = np.around((np.var(salida4)), decimals= 5)
        desviacionEstandar = np.around((np.std(salida4)), decimals= 5)
        maximo = max(salida4)
        minimo = min(salida4)
        titulo = 4

    if(request.POST.get('columnaE')): 
        tipo = contador.tipo[4]
        promedio = np.mean(salida5)
        moda = stats.mode(salida5)[0][0]
        mediana = np.around((np.median(salida5)), decimals= 4)        
        varianza = np.around((np.var(salida5)), decimals= 4)
        desviacionEstandar = np.around((np.std(salida5)), decimals= 4)
        maximo = max(salida5)
        minimo = min(salida5)
        titulo = 5

    if(request.POST.get('columnaF')): 
        tipo = contador.tipo[5]
        promedio = np.mean(salida6)
        moda = stats.mode(salida6)[0][0]
        mediana = np.around((np.median(salida6)), decimals= 4)        
        varianza = np.around((np.var(salida6)), decimals= 4)
        desviacionEstandar = np.around((np.std(salida6)), decimals= 4)
        maximo = max(salida6)
        minimo = min(salida6)
        titulo = 6


    

   

    matriz = [salida1,salida2,salida3,salida4,salida5,salida6]
    
    correlacion = np.around((np.corrcoef(matriz)), decimals= 5)
    #correlacion = stats.pearsonr(salida1, salida2)[0]
    #print(correlacion[5])
    print(type(correlacion[0][1]))
    contexto = {
        "Tabla":Tabla.objects.all()[tamaño-10:tamaño],
        "Promedio": promedio,
        "Moda": moda,
        "Mediana": mediana,
        "Varianza": varianza,
        "DesviacionEstandar": desviacionEstandar,
        "Maximo": maximo,
        "Minimo": minimo,
        "Titulo": titulo,
        "Tipo": tipo,
        "Correlacion1": correlacion[0],
        "Correlacion2": correlacion[1],
        "Correlacion3": correlacion[2],
        "Correlacion4": correlacion[3],
        "Correlacion5": correlacion[4],
        "Correlacion6": correlacion[5]
        
        }
    return render(request, 'form-elements.html',contexto)


def histograma(request):
    tamaño = 1000

    entrada = []
    salida1 = []
    salida2 = []
    salida3 = []
    salida4 = []
    salida5 = []
    salida6 = []   
    
    for i in Tabla.objects.all():
        entrada = np.append(entrada, i.tiempo)      
        salida1 = np.append(salida1, i.columnaA)       
        salida2 = np.append(salida2, i.columnaB)
        salida3 = np.append(salida3, i.columnaC)
        salida4 = np.append(salida4, i.columnaD)
        salida5 = np.append(salida5, i.columnaE)
        salida6 = np.append(salida6, i.columnaF)

    titulo = 0
    eleccion = 0
    plot_histograma = grafico_histograma([], "white", "white")
    scriptHisto , divHisto = components(plot_histograma)

    if(request.POST.get('columnaA')):
        contador.vector = "Vector A"       
        measured = salida1
        hist, edges = np.histogram(measured, bins=10)
        x = np.linspace(-2, 2, 1000)        
        p = make_plot("Histograma del ",contador.vector, hist, edges,x,"red")
        scriptHisto , divHisto = components(p)
        titulo = 1   
        
        

    if(request.POST.get('columnaB')): 
        contador.vector = "Vector B"  
        measured = salida2
        hist, edges = np.histogram(measured, bins=10)
        x = np.linspace(-2, 2, 1000)        
        p = make_plot("Histograma del ",contador.vector, hist, edges,x,"blue")
        scriptHisto , divHisto = components(p)
        titulo = 2 

    if(request.POST.get('columnaC')): 
        contador.vector = "Vector C"  
        measured = salida3
        hist, edges = np.histogram(measured, bins=10)
        x = np.linspace(-2, 2, 1000)        
        p = make_plot("Histograma del ",contador.vector, hist, edges,x,"yellow")
        scriptHisto , divHisto = components(p)
        titulo = 3

    if(request.POST.get('columnaD')): 
        contador.vector = "Vector D" 
        measured = salida4
        hist, edges = np.histogram(measured, bins=10)
        x = np.linspace(-2, 2, 1000)        
        p = make_plot("Histograma del ",contador.vector, hist, edges,x,"orange")
        scriptHisto , divHisto = components(p)
        titulo = 4

    if(request.POST.get('columnaE')): 
        contador.vector = "Vector E"  
        measured = salida5
        hist, edges = np.histogram(measured, bins=10)
        x = np.linspace(-2, 2, 1000)        
        p = make_plot("Histograma del ",contador.vector, hist, edges,x,"green")
        scriptHisto , divHisto = components(p)
        titulo = 5

    if(request.POST.get('columnaF')): 
        contador.vector = "Vector F"  
        measured = salida6
        hist, edges = np.histogram(measured, bins=10)
        x = np.linspace(-2, 2, 1000)        
        p = make_plot("Histograma del ",contador.vector, hist, edges,x,"brown")
        scriptHisto , divHisto = components(p)
        titulo = 6

    if(request.POST.get('tipo1')):        
        eleccion = 1    
        registro = SeleccionTipo(letraVector = contador.vector, tipoVector = "Binomial")
        registro.save()  
        

    if(request.POST.get('tipo2')):
        eleccion = 1
        registro = SeleccionTipo(letraVector = contador.vector, tipoVector = "Normal")
        registro.save() 
        

    if(request.POST.get('tipo3')): 
        eleccion = 1
        registro = SeleccionTipo(letraVector = contador.vector, tipoVector = "Poisson")
        registro.save()

    
      

    contexto = {
        'scriptHisto': scriptHisto, 
        'divHisto':divHisto,
        'Tabla':Tabla.objects.all()[tamaño-10:tamaño],       
        'Titulo': titulo ,
        'salida': salida1,
        'eleccion':eleccion 
        
        }
 
    return render(request, 'typography.html',contexto)