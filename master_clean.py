# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:36:57 2019

@author: ian_s
"""

#importando librerias
import pandas as pd
import numpy as np
import math 
from pandas.plotting import table
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from math import pi
from windrose import WindroseAxes

#------------------------------------------------------------------------------
  
#------------------------------------------------------------------------------
    
def Grafica():
    plt.plot(dfPLT) 
    plt.xlabel('TIEMPO') 
    plt.ylabel(nameColum) 
    plt.title(TitleGrafica)  
    plt.show()      
    
    
#------------------------------------------------------------------------------
#esta funcion genera la rosa de viento
def RosaDeViento():
    print('\n')
    print('¿Desea generar Rosa de Viento? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        df['velocidad_x'] = VelocidadViento * np.sin(DireccionViento * pi / 180.0)
        df['velocidad_y'] = VelocidadViento * np.cos(DireccionViento * pi / 180.0)
        fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        ax.set_aspect('equal')
        _ = df.plot(kind='scatter', x='velocidad_x', y='velocidad_y', alpha=0.35, ax=ax)
        plt.show()
        
        print('\n'*2)
        print('======================== ROSA DE VIENTO =========================')
        ax = WindroseAxes.from_ax()
        ax.bar(DireccionViento, VelocidadViento, normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.show()
#------------------------------------------------------------------------------    
                                            
#------------------------------------------------------------------------------                                           
#creando funcion para exportar df a doc PDF
def GenPDF():
    print('\n')
    print('¿Desea generar un documento PDF de la consola? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        print('\n')
        print('\n')
        print('Al ingresar el nombre del doc. agregele el punto pdf "@ejemplo Resultado##.pdf "  ')
#esta parte del codigo genera el doc PDF      
        nombrePDF = str(input('ingrese el nombre del doc:  '))
        with PdfPages(str(nombrePDF)) as pdf:
            txt='Reporte de Datos'
            firstPage=plt.figure(figsize=(6,4))
            firstPage.clf()
            firstPage.text(0.5,0.5,txt,transform=firstPage.transFigure,size=32,ha='center')
            pdf.savefig()
            plt.close()
            
            j=0
            
            for i in range(0,5):
                
                txt2='dataframe'
                fig,ax=plt.subplots(1,1)
                plt.gca().axis('off')
                plt.text(0,1.05,txt2,bbox=dict(boxstyle='square',color='yellow'))
                plt.ioff()
                
                table(ax,(dfExcel.iloc[j:j+5]), loc='center', bbox=[0,0,1,1])
                pdf.savefig()
                plt.close()
                
                j=j+6
                
            plt.plot(dfPLT) 
            plt.xlabel('TIEMPO') 
            plt.ylabel(nameColum) 
            plt.title(TitleGrafica)  
            pdf.savefig()
            plt.close()
    
        print('\n'*3)
        print('Ya se genero el documento PDF ')
        print('Este se guardo en la misma carpeta donde guardo el csv que ingresaste')
#------------------------------------------------------------------------------    

#------------------------------------------------------------------------------
#creando funcion para exportar df a doc excel
def GenEXCEL():
    print('\n')
    print('¿Desea generar un documento Excel del dataframe? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        print('\n')
        print('Al ingresar el nombre del doc. agregele el punto xlsl "@ejemplo Resultado##.xlsx "  ')
#esta parte del codigo genera el doc Excel      
        nombrexp = str(input('ingrese el nombre del doc:  '))
        grabar=pd.ExcelWriter(str(nombrexp))        
        dfExcel.to_excel(grabar,'Hoja 1')
        grabar.save()
        print('\n'*2)
        print('Ya se genero el documento Excel ')
        print('Este se guardo en la misma carpeta donde guardo el csv que ingresaste')
    else:
        print('gracias')         
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------        
#------------------------------------------------------------------------------
#leemos el doc csv con el sig codigo
print('\n'*2)
print('\n=================================================================================  ')
print('Covertir el doc Excel a CSV(delimitado  por comas)  ' )  
print('---------------------------------------------------------------------------------  ')      
st = str(input('Ingrese el doc CSV que desea leer:  '))
df=pd.read_csv( str(st) ,header=0)
print('=================================================================================  ')
print('\n'*5)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#seleccion del formato sgun el doc csv

#"df2=df.columns.tolist()" se encarga de leer el encabezado de las columnas para identificar el formato
df2=df.columns.tolist()

letra = df2

# si el encabezado de las columnas es igual a alguno de estos guardados en la variable caracter se selecciona  
caracter = ['fecha', 'RapViento', 'RapRafaga', 'DirViento', 'DirRafaga', 'TempAire',
       'HumRelativa', 'PresBarometric', 'Precipitacion', 'RadSolar']
caracter2 = ['Date', 'Time', 'Dir', 'WSMDir', 'WSK', 'WSMK', 'AvgTemp', 'AvgRh',
             'AvgBP', 'Rain', 'AvgSR', 'Batt', 'SPanel']
caracter3 = ['fecha', 'DirViento', 'DirRafaga', 'RapViento', 'RapRafaga', 'TempAire',
             'HumRelativa', 'PresBarometric', 'Precipitacion', 'RadSolar', 'nombre_estacion']




#------------------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ FORMATOS //////////////////////////////////
#------------------------------------------------------------------------------

#formato (1)
if(letra == caracter):
    
    df['RapViento'] = pd.to_numeric(df['RapViento'],errors='coerce')
    df['RapRafaga'] = pd.to_numeric(df['RapRafaga'],errors='coerce')
    df['DirViento'] = pd.to_numeric(df['DirViento'],errors='coerce')
    df['DirRafaga'] = pd.to_numeric(df['DirRafaga'],errors='coerce')
    df['TempAire'] = pd.to_numeric(df['TempAire'],errors='coerce')
    df['HumRelativa'] = pd.to_numeric(df['HumRelativa'],errors='coerce')
    df['PresBarometric'] = pd.to_numeric(df['PresBarometric'],errors='coerce')
    df['Precipitacion'] = pd.to_numeric(df['Precipitacion'],errors='coerce')
    df['RadSolar'] = pd.to_numeric(df['RadSolar'],errors='coerce')
#------------------------------------------------------------------------------    
    r=0
    FREC0=df.loc[0,'fecha']
    FREC1=df.loc[1,'fecha']
    
    XFREC0=int(FREC0[-2:])
    XFREC1=int(FREC1[-2:])
    
    q=0
#esta condicon checa los minutos y nos permite saber si esdiezminutal o no
    if (XFREC1==XFREC0+10):
        print('\n            LA FRECUENCIA DE DATOS ES DIEZMINUTAL Y SE CONVERTIRA A DATOS DIARIOS')
    elif (XFREC1==XFREC0+15):
        print('\n          LA FRECUENCIA DE DATOS ES QUINCEMINUTAL Y SE CONVERTIRA A DATOS DIARIOS')
    elif (XFREC1==XFREC0):    
        print('\n                LA FRECUENCIA DE DATOS ES HORARIA Y SE CONVERTIRA A DATOS DIARIOS')
    print('..................................................................................    ')    

    if (XFREC1==XFREC0+10) or (XFREC1==XFREC0+15) or (XFREC1==XFREC0):    
#print('yes')
        findf=len(df)
    
        for i in range(1,findf):
            FMESA=df.loc[i-1,'fecha']
            FMESAX=FMESA[1:4]
            FMESD=df.loc[i,'fecha']
            FMESDX=FMESD[1:4]
#esta condicon checa el dia        
            if(FMESDX!=FMESAX):
                ndf=df.loc[r:i-1]
#print(ndf)
                FHN=ndf.loc[i-1,'fecha']
                df.loc[q,'fecha']=FHN[0:9]
                df.loc[q,'RapViento'] = ndf.RapViento.mean()
                df.loc[q,'RapRafaga'] = ndf.RapRafaga.mean()
                df.loc[q,'DirViento'] = ndf.DirViento.mean()
                df.loc[q,'DirRafaga'] = ndf.DirRafaga.mean()
                df.loc[q,'TempAire'] = ndf.TempAire.mean()
                df.loc[q,'HumRelativa'] = ndf.HumRelativa.mean()
                df.loc[q,'PresBarometric'] = ndf.PresBarometric.mean()
                df.loc[q,'Precipitacion'] = ndf.Precipitacion.sum()
                df.loc[q,'RadSolar'] = ndf.RadSolar.mean()
            
                q=q+1
                r=i
            
        ndf=df.loc[r:i]
#print(ndf)
        FHN=ndf.loc[i-1,'fecha']
        df.loc[q,'fecha']=FHN[0:9]
        df.loc[q,'RapViento'] = ndf.RapViento.mean()
        df.loc[q,'RapRafaga'] = ndf.RapRafaga.mean()
        df.loc[q,'DirViento'] = ndf.DirViento.mean()
        df.loc[q,'DirRafaga'] = ndf.DirRafaga.mean()
        df.loc[q,'TempAire'] = ndf.TempAire.mean()
        df.loc[q,'HumRelativa'] = ndf.HumRelativa.mean()
        df.loc[q,'PresBarometric'] = ndf.PresBarometric.mean()
        df.loc[q,'Precipitacion'] = ndf.Precipitacion.sum()
        df.loc[q,'RadSolar'] = ndf.RadSolar.mean()
            
    df.drop(df.index[q+1:len(df)],inplace=True)
#eliminando NANS creados por saltos de fila    
    for i in range(0,len(df)):
        if pd.isnull(df.loc[i,'DirViento'])==True :
            if pd.isnull(df.loc[i,'DirRafaga'])==True :
                if pd.isnull(df.loc[i,'RapViento'])==True :
                    if pd.isnull(df.loc[i,'RapRafaga'])==True :
                        if pd.isnull(df.loc[i,'TempAire'])==True :
                            if pd.isnull(df.loc[i,'HumRelativa'])==True :
                                if pd.isnull(df.loc[i,'PresBarometric'])==True :
                                    if pd.isnull(df.loc[i,'Precipitacion'])==True :
                                        if pd.isnull(df.loc[i,'RadSolar'])==True :
                                            df.drop([i], inplace=True)
    
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ' )
    print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
    print(df)    
        
    print('\n'*2)
    print('------------------------ ***VALORES NaN***  ---------------------------')
    print(df.isnull().sum())
    print('\n'*2)
    print('------------------------ ***VALORES MAXIMOS***  -----------------------')
    print(df.max())
    print('\n'*2)
    print('------------------------ ***VALORES MINIMOS***  -----------------------')
    print(df.min())
    print('\n'*2)
    print('------------------------ ***VALORES MEDIOS***  ------------------------')
    print(df.mean())

#yécora mz08.csv
    
    VelocidadViento=df.RapViento
    DireccionViento=df.DirViento
    RosaDeViento()
    
    print('\n')
    print('¿Desea crear una nueva columna de velocidad del viento a 10 mts? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        print('\n\n░░░░░░░░░░░░░░TIPO DE SUPERFICIE░░░░░░░░░░░░░░░░░░░░░░░VALOR DE Zo░░░░░░' )
        print('\n◙ Superficie del agua -----------------------------------> 0.0002 ')
        print('◙ Áreas abiertas con muy poca protección ----------------> 0.03')
        print('contra el viento')
        print('◙ Terreno agrícola con algo protección contra -----------> 0.1')
        print('el viento de más de 1 km de separación')
        print('◙ Distritos urbanos y terreno agrícola con --------------> 0.4')
        print('mucha proteccion contra el viento')
        rug = float(input('Elija la rugosidad del terreno:  '))
        va3m=df['RapViento']*((10/3)**(0.24+(0.04*math.log(rug)))+(0.003*(math.log(rug)**2)))
        df=df.assign(RapViento10m=va3m.values)
        print('\n ' )
        print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░NUEVO MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
        print(df)   
        
    print('\n')
    print('¿Desea crear una nueva columna de velocidad del viento a otra altura en mts? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        alt = str(input('Elija la altura:  '))
        va3m=df['RapViento']*((float(alt)/3)**(0.24+(0.04*math.log(rug)))+(0.003*(math.log(rug)**2)))
        axm='RapViento'+alt+'m'
        df=df.assign(axm=va3m.values)
        df=df.rename(columns = {'axm':axm})
        print('\n ' )
        print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░NUEVO MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
        print(df)
#------------------------------------------------------------------------------

#mes/dia/año
    print('\n')
    print('¿Desea buscar una fecha? ')
    gen = str(input('Si desea buscar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        fhDIA = str(input('ingrese el numero de Dia:  ')) 
        fhMES = str(input('ingrese el numero de Mes:  '))
        
        FECHA = fhMES + '/' + fhDIA + '/'
        print('FECHA:',FECHA)
        df2=df.loc[df['fecha'].str.startswith(FECHA)]        
        print('\n',df2)
        
        media=df2.RadSolar.mean()    
        
        suma=0
        for i in range(0,len(df2)):
            
            suma += (df2.iloc[i,9] - media) ** 2
            
        VARIANZA = suma / (len(df2) )
        
        print('\n■ Varianza: ',VARIANZA)
        print('■ Media: ',df2.RadSolar.mean())
        print('■ Mediana: ',df2.RadSolar.median())        
#------------------------------------------------------------------------------    
    print('\n')
    print('¿Desea analizar los datos especificos de alguna columna? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'): 
        print('\n Siguientes opciones: ' )
        print('\n 1.  Analisis RapViento' )
        print('\n 2.  Analisis RapRafaga' )
        print('\n 3.  Analisis DirViento' )
        print('\n 4.  Analisis DirRafaga' )
        print('\n 5.  Analisis TempAire' )
        print('\n 6.  Analisis HumRelativa' )
        print('\n 7.  Analisis PresBarometric' )
        print('\n 8.  Analisis Precipitacion' )
        print('\n 9.  Analisis RadSolar' )
        opcion = int(input('ingresar opcion:  '))
        while(opcion !=15):
            
            if(opcion == 1 ):
                
                dfE1 = nan_rows = df[df['RapViento'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN RapViento ------------------------------')
                print('\n'*2)
                print(dfE1)
                
                nameColum='RapViento'
                TitleGrafica='Grafica RapViento'
                dfExcel=dfE1
                dfPLT=df.RapViento
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                                
            elif(opcion == 2 ):
                    
                dfE2 = nan_rows = df[df['RapRafaga'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN RapRafaga ------------------------------')
                print('\n'*2)
                print(dfE2)
                
                nameColum='RapRafaga'
                TitleGrafica='Grafica RapRafaga'
                dfExcel=dfE2
                dfPLT=df.RapRafaga
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                                
            elif(opcion == 3 ):
                
                dfE3 = nan_rows = df[df['DirViento'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN DirViento ------------------------------')
                print('\n'*2)
                print(dfE3)
                
                nameColum='DirViento'
                TitleGrafica='Grafica DirViento'
                dfExcel=dfE3
                dfPLT=df.DirViento
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                                        
            elif(opcion == 4 ):
                
                dfE4 = nan_rows = df[df['DirRafaga'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN DirRafaga ------------------------------')
                print('\n'*2)
                print(dfE4)
                
                nameColum='DirRafaga'
                TitleGrafica='Grafica DirRafaga'
                dfExcel=dfE4
                dfPLT=df.DirRafaga
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                                
            elif(opcion == 5 ):
                        
                dfE5 = nan_rows = df[df['TempAire'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN TempAire ------------------------------')
                print('\n'*2)
                print(dfE5)
                
                nameColum='TempAire'
                TitleGrafica='Grafica TempAire' 
                dfExcel=dfE5
                dfPLT=df.TempAire
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;                
                
            elif(opcion == 6 ):
                
                dfE6 = nan_rows = df[df['HumRelativa'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN HumRelativa ------------------------------')
                print('\n'*2)
                print(dfE6)
                
                nameColum='HumRelativa'
                TitleGrafica='Grafica HumRelativa'
                dfExcel=dfE6
                dfPLT=df.HumRelativa
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;         
                                
            elif(opcion == 7 ):
                    
                dfE7 = nan_rows = df[df['PresBarometric'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN PresBarometric ------------------------------')
                print('\n'*2)
                print(dfE7)
                
                nameColum='PresBarometric'
                TitleGrafica='Grafica PresBarometric'
                dfExcel=dfE7
                dfPLT=df.PresBarometric
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;    
                    
            elif(opcion == 8 ):

                dfE8= nan_rows = df[df['Precipitacion'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN Precipitacion ------------------------------')
                print('\n'*2)
                print(dfE8)
                
                nameColum='Precipitacion'
                TitleGrafica='Grafica Precipitacion'
                dfExcel=dfE8
                dfPLT=df.Precipitacion
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;

            elif(opcion == 9 ):
            
                dfE9= nan_rows = df[df['RadSolar'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN RadSolar ------------------------------')
                print('\n'*2)
                print(dfE9)
                
                nameColum='RapSolar'
                TitleGrafica='Grafica RadSolar'
                dfExcel=dfE9
                dfPLT=df.RadSolar
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;

            else:
                print('\n'*2)
                print(' XXXXXXXXXXXXXXXXXXXXXXXX  ERROR  XXXXXXXXXXXXXXXXXXXXXXXXXXX  ' )
                break;
 
#------------------------------------------------------------------------------       
#formato (2)

elif(letra == caracter2):
#eliminando NANS creados por saltos de fila    
    df['Dir'] = pd.to_numeric(df['Dir'],errors='coerce')
    df['WSMDir'] = pd.to_numeric(df['WSMDir'],errors='coerce')
    df['WSK'] = pd.to_numeric(df['WSK'],errors='coerce')
    df['WSMK'] = pd.to_numeric(df['WSMK'],errors='coerce')
    df['AvgTemp'] = pd.to_numeric(df['AvgTemp'],errors='coerce')
    df['AvgRh'] = pd.to_numeric(df['AvgRh'],errors='coerce')
    df['AvgBP'] = pd.to_numeric(df['AvgBP'],errors='coerce')
    df['Rain'] = pd.to_numeric(df['Rain'],errors='coerce')
    df['AvgSR'] = pd.to_numeric(df['AvgSR'],errors='coerce')
    df['Batt'] = pd.to_numeric(df['Batt'],errors='coerce')
    df['SPanel'] = pd.to_numeric(df['SPanel'],errors='coerce')
    
    
    for i in range(0,len(df)):
        if pd.isnull(df.loc[i,'WSMDir'])==True :
            if pd.isnull(df.loc[i,'WSK'])==True :
                if pd.isnull(df.loc[i,'WSMK'])==True :
                    if pd.isnull(df.loc[i,'AvgTemp'])==True :
                        if pd.isnull(df.loc[i,'AvgRh'])==True :
                            if pd.isnull(df.loc[i,'AvgBP'])==True :
                                if pd.isnull(df.loc[i,'Rain'])==True :
                                    if pd.isnull(df.loc[i,'AvgSR'])==True :
                                        if pd.isnull(df.loc[i,'Batt'])==True :
                                            if pd.isnull(df.loc[i,'SPanel'])==True :      
                                                df.drop([i], inplace=True)
                                            
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ' )
    print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
    print(df) 
        
    print('\n'*2)
    print('------------------------ ***VALORES NaN***  -------------------------')
    print(df.isnull().sum())
    print('\n'*2)
    print('------------------------ ***VALORES MAXIMOS***  -----------------------')
    print(df.max())
    print('\n'*2)
    print('------------------------ ***VALORES MINIMOS***  -----------------------')
    print(df.min())
    print('\n'*2)
    print('------------------------ ***VALORES MEDIOS***  ------------------------')
    print(df.mean())
    
#Yécora emz 03.csv
    VelocidadViento=df.WSK
    DireccionViento=df.WSMDir
    RosaDeViento()
    
    df['Date'] = df['Date'].str.replace(r' Ene ','/1/')
    df['Date'] = df['Date'].str.replace(r' Feb ','/2/')
    df['Date'] = df['Date'].str.replace(r' Mar ','/3/')
    df['Date'] = df['Date'].str.replace(r' Abr ','/4/')
    df['Date'] = df['Date'].str.replace(r' May ','/5/')
    df['Date'] = df['Date'].str.replace(r' Jun ','/6/')
    df['Date'] = df['Date'].str.replace(r' Jul ','/7/')
    df['Date'] = df['Date'].str.replace(r' Ago ','/8/')
    df['Date'] = df['Date'].str.replace(r' Sep ','/9/')
    df['Date'] = df['Date'].str.replace(r' Oct ','/10/')
    df['Date'] = df['Date'].str.replace(r' Nov ','/11/')
    df['Date'] = df['Date'].str.replace(r' Dic ','/12/')
    df['Date'] = df['Date'].str.replace(r' ene ','/1/')
    df['Date'] = df['Date'].str.replace(r' feb ','/2/')
    df['Date'] = df['Date'].str.replace(r' mar ','/3/')
    df['Date'] = df['Date'].str.replace(r' abr ','/4/')
    df['Date'] = df['Date'].str.replace(r' may ','/5/')
    df['Date'] = df['Date'].str.replace(r' jun ','/6/')
    df['Date'] = df['Date'].str.replace(r' jul ','/7/')
    df['Date'] = df['Date'].str.replace(r' ago ','/8/')
    df['Date'] = df['Date'].str.replace(r' sep ','/9/')
    df['Date'] = df['Date'].str.replace(r' oct ','/10/')
    df['Date'] = df['Date'].str.replace(r' nov ','/11/')
    df['Date'] = df['Date'].str.replace(r' dic ','/12/')
    
    print(df)
    print('\n')
    print('¿Desea crear una nueva columna de velocidad del viento a 10 mts? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        print('\n\n░░░░░░░░░░░░░░TIPO DE SUPERFICIE░░░░░░░░░░░░░░░░░░░░░░░VALOR DE Zo░░░░░░' )
        print('\n◙ Superficie del agua -----------------------------------> 0.0002 ')
        print('◙ Áreas abiertas con muy poca protección ----------------> 0.03')
        print('contra el viento')
        print('◙ Terreno agrícola con algo protección contra -----------> 0.1')
        print('el viento de más de 1 km de separación')
        print('◙ Distritos urbanos y terreno agrícola con --------------> 0.4')
        print('mucha proteccion contra el viento')
        rug = float(input('Elija la rugosidad del terreno:  '))
        va3m=df['WSK']*((10/3)**(0.24+(0.04*math.log(rug)))+(0.003*(math.log(rug)**2)))
        df=df.assign(RapViento10m=va3m.values)
        print('\n ' )
        print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░NUEVO MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
        print(df)   
        
    print('\n')
    print('¿Desea crear una nueva columna de velocidad del viento a otra altura en mts? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        alt = str(input('Elija la altura:  '))
        va3m=df['WSK']*((float(alt)/3)**(0.24+(0.04*math.log(rug)))+(0.003*(math.log(rug)**2)))
        axm='RapViento'+alt+'m'
        df=df.assign(axm=va3m.values)
        df=df.rename(columns = {'axm':axm})
        print('\n ' )
        print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░NUEVO MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
        print(df)
#------------------------------------------------------------------------------

#mes/dia/año
    print('\n')
    print('¿Desea buscar una fecha? ')
    gen = str(input('Si desea buscar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        
        fhDIA = str(input('ingrese el numero de Dia:  '))
        fhMES = str(input('ingrese el numero de Mes:  ')) 
                
        FECHA = '/' + fhMES + '/' + fhDIA 
        print('FECHA:',FECHA)
        df2=df.loc[df['Date'].str.endswith(FECHA)]        
        print('\n',df2)
        
        media=df2.AvgSR.mean()    
        
        suma=0
        for i in range(0,len(df2)):
            
            suma += (df2.iloc[i,10] - media) ** 2
            
        VARIANZA = suma / (len(df2) )
        
        print('\n■ Varianza: ',VARIANZA)
        print('■ Media: ',df2.AvgSR.mean())
        print('■ Mediana: ',df2.AvgSR.median())
        
#-------------------
    
    print('\n')
    print('¿Desea analizar los datos especificos de alguna columna? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'): 
        print('\n Siguientes opciones: ' )
        print('\n 1.  Analisis Dir' )
        print('\n 2.  Analisis WSMDir' )
        print('\n 3.  Analisis WSK' )
        print('\n 4.  Analisis WSMK' )
        print('\n 5.  Analisis AvgTemp' )
        print('\n 6.  Analisis AvgRh' )
        print('\n 7.  Analisis AvgBP' )
        print('\n 8.  Analisis Rain' )
        print('\n 9.  Analisis AvgSR' )
        print('\n 10. Analisis Batt')
        print('\n 11. Analisis SPanel')
        
        opcion = int(input('ingresar opcion:  '))
        while(opcion !=15):
            
            if(opcion == 1 ):
                
                df['Dir'] = pd.to_numeric(df['Dir'],errors='coerce')
                dfE1 = nan_rows = df[df['Dir'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN Dir ------------------------------')
                print('\n'*2)
                print(dfE1)
            
                nameColum='Dir'
                TitleGrafica='Grafica Dir'
                dfExcel=dfE1
                dfPLT=df.Dir
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                    
            elif(opcion == 2 ):
                        
                dfE2 = nan_rows = df[df['WSMDir'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN WSMDir ------------------------------')
                print('\n'*2)
                print(dfE2)
                df['WSMDir'] = pd.to_numeric(df['WSMDir'],errors='coerce')
                
                nameColum='WSMDir'
                TitleGrafica='Grafica WSMDir'
                dfExcel=dfE2
                dfPLT=df.WSMDir
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                    
            elif(opcion == 3 ):
            
                dfE3 = nan_rows = df[df['WSK'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN WSK ------------------------------')
                print('\n'*2)
                print(dfE3)
                df['WSK'] = pd.to_numeric(df['WSK'],errors='coerce')
                
                nameColum='WSK'
                TitleGrafica='Grafica WSK'
                dfExcel=dfE3
                dfPLT=df.WSK
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;

            elif(opcion == 4 ):
            
                dfE4 = nan_rows = df[df['WSMK'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN WSMK ------------------------------')
                print('\n'*2)
                print(dfE4)
                df['WSMK'] = pd.to_numeric(df['WSMK'],errors='coerce')
                
                nameColum='WSMK'
                TitleGrafica='Grafica WSMK'
                dfExcel=dfE4
                dfPLT=df.WSMK
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;

            elif(opcion == 5 ):
            
                dfE5 = nan_rows = df[df['AvgTemp'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN AvgTemp ------------------------------')
                print('\n'*2)
                print(dfE5)
                df['AvgTemp'] = pd.to_numeric(df['AvgTemp'],errors='coerce')
                
                nameColum='AvgTemp'
                TitleGrafica='Grafica AvgTemp'
                dfExcel=dfE5
                dfPLT=df.AvgTemp
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;                
            
            elif(opcion == 6 ):
                
                dfE6 = nan_rows = df[df['AvgRh'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN AvgRh ------------------------------')
                print('\n'*2)
                print(dfE6)
                df['AvgRh'] = pd.to_numeric(df['AvgRh'],errors='coerce')
                
                nameColum='AvgRh'
                TitleGrafica='Grafica AvgRh'
                dfExcel=dfE6
                dfPLT=df.AvgRh
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;         
                                
            elif(opcion == 7 ):
            
                dfE7 = nan_rows = df[df['AvgBP'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN AvgBP ------------------------------')
                print('\n'*2)
                print(dfE7)
                df['AvgBP'] = pd.to_numeric(df['AvgBP'],errors='coerce')
                
                nameColum='AvgBP'
                TitleGrafica='Grafica AvgBP'
                dfExcel=dfE7
                dfPLT=df.AvgBP
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;            
            
            elif(opcion == 8 ):
            
                dfE8= nan_rows = df[df['Rain'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN Rain ------------------------------')
                print('\n'*2)
                print(dfE8)
                df['Rain'] = pd.to_numeric(df['Rain'],errors='coerce')
                
                nameColum='RAIN'
                TitleGrafica='Grafica RAIN'
                dfExcel=dfE8
                dfPLT=df.Rain
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                    
            elif(opcion == 9 ):
                
                dfE9= nan_rows = df[df['AvgSR'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN AvgSR ------------------------------')
                print('\n'*2)
                print(dfE9)
                df['AvgSR'] = pd.to_numeric(df['AvgSR'],errors='coerce')
                
                nameColum='AvgSR'
                TitleGrafica='Grafica AvgSR'
                dfExcel=dfE9
                dfPLT=df.AvgSR
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                            
            elif(opcion == 10 ):
            
                dfA1= nan_rows = df[df['Batt'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN Batt ------------------------------')
                print('\n'*2)
                print(dfA1)
                df['Batt'] = pd.to_numeric(df['Batt'],errors='coerce')
                
                plt.plot(df.Batt) 
                plt.xlabel('TIEMPO') 
                plt.ylabel('Batt')  
                plt.title('GRAFICA DE BATT')  
                plt.show()
                dfExcel=dfA1
                dfPLT=df.Batt
                GenEXCEL()
                GenPDF()
                break;
                                
            elif(opcion == 11 ):
                        
                dfA2= nan_rows = df[df['SPanel'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN SPanel ------------------------------')
                print('\n'*2)
                print(dfA2)
                df['SPanel'] = pd.to_numeric(df['SPanel'],errors='coerce')
                
                nameColum='SPANEL'
                TitleGrafica='Grafica SPANEL'
                dfExcel=dfA2
                dfPLT=df.SPanel
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                
                
            else:
                print('\n'*2)
                print(' XXXXXXXXXXXXXXXXXXXXXXXX  ERROR  XXXXXXXXXXXXXXXXXXXXXXXXXXX  ' )
                break;
            
#------------------------------------------------------------------------------        
#formato(3)
            
elif(letra == caracter3):
    
    df['DirViento'] = pd.to_numeric(df['DirViento'],errors='coerce')
    df['DirRafaga'] = pd.to_numeric(df['DirRafaga'],errors='coerce')
    df['RapViento'] = pd.to_numeric(df['RapViento'],errors='coerce')
    df['RapRafaga'] = pd.to_numeric(df['RapRafaga'],errors='coerce')
    df['TempAire'] = pd.to_numeric(df['TempAire'],errors='coerce')
    df['HumRelativa'] = pd.to_numeric(df['HumRelativa'],errors='coerce')
    df['PresBarometric'] = pd.to_numeric(df['PresBarometric'],errors='coerce')
    df['Precipitacion'] = pd.to_numeric(df['Precipitacion'],errors='coerce')
    df['RadSolar'] = pd.to_numeric(df['RadSolar'],errors='coerce')
    
#-----------------------------------------------------------
    r=0
    FREC0=df.loc[0,'fecha']
    FREC1=df.loc[1,'fecha']
    
    XFREC0=int(FREC0[-2:])
    XFREC1=int(FREC1[-2:])
    
    q=0
#esta condicon checa los minutos y nos permite saber si esdiezminutal o no
    if (XFREC1==XFREC0+10):
        print('\n            LA FRECUENCIA DE DATOS ES DIEZMINUTAL Y SE CONVERTIRA A DATOS DIARIOS')
    elif (XFREC1==XFREC0+15):
        print('\n          LA FRECUENCIA DE DATOS ES QUINCEMINUTAL Y SE CONVERTIRA A DATOS DIARIOS')
    elif (XFREC1==XFREC0):    
        print('\n                LA FRECUENCIA DE DATOS ES HORARIA Y SE CONVERTIRA A DATOS DIARIOS')
    print('..................................................................................    ')    

    if (XFREC1==XFREC0+10) or (XFREC1==XFREC0+15) or (XFREC1==XFREC0):    
#print('yes')
        findf=len(df)
    
        for i in range(1,findf):
            FMESA=df.loc[i-1,'fecha']
            FMESAX=FMESA[1:4]
            FMESD=df.loc[i,'fecha']
            FMESDX=FMESD[1:4]
#esta condicon checa el dia        
            if(FMESDX!=FMESAX):
                ndf=df.loc[r:i-1]
#print(ndf)
                FHN=ndf.loc[i-1,'fecha']
                df.loc[q,'fecha']=FHN[0:9]
                df.loc[q,'RapViento'] = ndf.RapViento.mean()
                df.loc[q,'RapRafaga'] = ndf.RapRafaga.mean()
                df.loc[q,'DirViento'] = ndf.DirViento.mean()
                df.loc[q,'DirRafaga'] = ndf.DirRafaga.mean()
                df.loc[q,'TempAire'] = ndf.TempAire.mean()
                df.loc[q,'HumRelativa'] = ndf.HumRelativa.mean()
                df.loc[q,'PresBarometric'] = ndf.PresBarometric.mean()
                df.loc[q,'Precipitacion'] = ndf.Precipitacion.sum()
                df.loc[q,'RadSolar'] = ndf.RadSolar.mean()
            
                q=q+1
                r=i
            
        ndf=df.loc[r:i]
#print(ndf)
        FHN=ndf.loc[i-1,'fecha']
        df.loc[q,'fecha']=FHN[0:9]
        df.loc[q,'RapViento'] = ndf.RapViento.mean()
        df.loc[q,'RapRafaga'] = ndf.RapRafaga.mean()
        df.loc[q,'DirViento'] = ndf.DirViento.mean()
        df.loc[q,'DirRafaga'] = ndf.DirRafaga.mean()
        df.loc[q,'TempAire'] = ndf.TempAire.mean()
        df.loc[q,'HumRelativa'] = ndf.HumRelativa.mean()
        df.loc[q,'PresBarometric'] = ndf.PresBarometric.mean()
        df.loc[q,'Precipitacion'] = ndf.Precipitacion.sum()
        df.loc[q,'RadSolar'] = ndf.RadSolar.mean()
            
    df.drop(df.index[q+1:len(df)],inplace=True)
    
    #eliminando NANS creados por saltos de fila    
    for i in range(0,len(df)):
        if pd.isnull(df.loc[i,'DirViento'])==True :
            if pd.isnull(df.loc[i,'DirRafaga'])==True :
                if pd.isnull(df.loc[i,'RapViento'])==True :
                    if pd.isnull(df.loc[i,'RapRafaga'])==True :
                        if pd.isnull(df.loc[i,'TempAire'])==True :
                            if pd.isnull(df.loc[i,'HumRelativa'])==True :
                                if pd.isnull(df.loc[i,'PresBarometric'])==True :
                                    if pd.isnull(df.loc[i,'Precipitacion'])==True :
                                        if pd.isnull(df.loc[i,'RadSolar'])==True :
                                            df.drop([i], inplace=True)
    
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ' )
    print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
    print(df) 
    
    print('\n'*2)
    print('------------------------ ***VALORES NaN***  -------------------------')
    print(df.isnull().sum())
    print('\n'*2)
    print('------------------------ ***VALORES MAXIMOS***  -----------------------')
    print(df.max())
    print('\n'*2)
    print('------------------------ ***VALORES MINIMOS***  -----------------------')
    print(df.min())
    print('\n'*2)
    print('------------------------ ***VALORES MEDIOS***  ------------------------')
    print(df.mean())
    
#yécor s12.csv
    VelocidadViento=df.RapViento
    DireccionViento=df.DirViento
    RosaDeViento()
    
    print('\n')
    print('¿Desea crear una nueva columna de velocidad del viento a 10 mts? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        print('\n\n░░░░░░░░░░░░░░TIPO DE SUPERFICIE░░░░░░░░░░░░░░░░░░░░░░░VALOR DE Zo░░░░░░' )
        print('\n◙ Superficie del agua -----------------------------------> 0.0002 ')
        print('◙ Áreas abiertas con muy poca protección ----------------> 0.03')
        print('contra el viento')
        print('◙ Terreno agrícola con algo protección contra -----------> 0.1')
        print('el viento de más de 1 km de separación')
        print('◙ Distritos urbanos y terreno agrícola con --------------> 0.4')
        print('mucha proteccion contra el viento')
        rug = float(input('Elija la rugosidad del terreno:  '))
        va3m=df['RapViento']*((10/3)**(0.24+(0.04*math.log(rug)))+(0.003*(math.log(rug)**2)))
        df=df.assign(RapViento10m=va3m.values)
        print('\n ' )
        print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░NUEVO MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
        print(df)   
        
    print('\n')
    print('¿Desea crear una nueva columna de velocidad del viento a otra altura en mts? ')
    gen = str(input('Si desea generar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        alt = str(input('Elija la altura:  '))
        va3m=df['RapViento']*((float(alt)/3)**(0.24+(0.04*math.log(rug)))+(0.003*(math.log(rug)**2)))
        axm='RapViento'+alt+'m'
        df=df.assign(axm=va3m.values)
        df=df.rename(columns = {'axm':axm})
        print('\n ' )
        print('\n ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░NUEVO MARCO DE DATOS░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░' )
        print(df)
#------------------------------------------------------------------------------

#mes/dia/año
    print('\n')
    print('¿Desea buscar una fecha? ')
    gen = str(input('Si desea buscar teclee "si" de lo contrario pulse calquier tecla:  '))
    if(gen == 'si'):
        fhDIA = str(input('ingrese el numero de Dia:  ')) 
        fhMES = str(input('ingrese el numero de Mes:  '))
        
        FECHA = fhMES + '/' + fhDIA + '/'
        print('FECHA:',FECHA)
        df2=df.loc[df['fecha'].str.startswith(FECHA)]        
        print('\n',df2)
        
        media=df2.RadSolar.mean()    
        
        suma=0
        for i in range(0,len(df2)):
            
            suma += (df2.iloc[i,9] - media) ** 2
            
        VARIANZA = suma / (len(df2) )
        
        print('\n■ Varianza: ',VARIANZA)
        print('■ Media: ',df2.RadSolar.mean())
        print('■ Mediana: ',df2.RadSolar.median())        
#--------------------------------------------------------
    
    
    print('\n')
    print('¿Desea analizar los datos especificos de alguna columna? ')
    gen = str(input('Si desea generar teclee "si" si no pulse calquier tecla:  '))
    if(gen == 'si'):    
        print('\n Siguientes opciones: ' )
        print('\n 1.  Analisis DirViento' )
        print('\n 2.  Analisis DirRafaga' )
        print('\n 3.  Analisis RapViento' )
        print('\n 4.  Analisis RapRafaga' )
        print('\n 5.  Analisis TempAire' )
        print('\n 6.  Analisis HumRelativa' )
        print('\n 7.  Analisis PresBarometric' )
        print('\n 8.  Analisis Precipitacion' )
        print('\n 9.  Analisis RadSolar' )
        opcion = int(input('ingresar opcion:  '))
        while(opcion !=15):
        
            if(opcion == 1 ):
            
                dfE1 = nan_rows = df[df['DirViento'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN DirViento ------------------------------')
                print('\n'*2)
                print(dfE1)
            
                nameColum='DirViento'
                TitleGrafica='Grafica DirViento'
                dfExcel=dfE1
                dfPLT=df.DirViento
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
            
            elif(opcion == 2 ):
            
                dfE2 = nan_rows = df[df['DirRafaga'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN DirRafaga ------------------------------')
                print('\n'*2)
                print(dfE2)
                
                nameColum='DirRafaga'
                TitleGrafica='Grafica DirRafaga'
                dfExcel=dfE2
                dfPLT=df.DirRafaga
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
            
            elif(opcion == 3 ):
                
                dfE3 = nan_rows = df[df['RapViento'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN RapViento ------------------------------')
                print('\n'*2)
                print(dfE3)
                
                nameColum='RapViento'
                TitleGrafica='Grafica RapViento'
                dfExcel=dfE3
                dfPLT=df.RapViento
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                
            elif(opcion == 4 ):
                    
                dfE4 = nan_rows = df[df['RapRafaga'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN RapRafaga ------------------------------')
                print('\n'*2)
                print(dfE4)
                
                nameColum='RapRafaga'
                TitleGrafica='Grafica RapRafaga'
                dfExcel=dfE4
                dfPLT=df.RapRafaga
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                
            elif(opcion == 5 ):
                
                dfE5 = nan_rows = df[df['TempAire'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN TempAire ------------------------------')
                print('\n'*2)
                print(dfE5)
                
                nameColum='TempAire'
                TitleGrafica='Grafica TempAire'
                dfExcel=dfE5
                dfPLT=df.TempAire
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;                
                
            elif(opcion == 6 ):
                
                dfE6 = nan_rows = df[df['HumRelativa'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN HumRelativa ------------------------------')
                print('\n'*2)
                print(dfE6)
                
                nameColum='HumRelativa'
                TitleGrafica='Grafica HumRelativa'
                dfExcel=dfE6
                dfPLT=df.HumRelativa
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;         
                
            elif(opcion == 7 ):
                    
                dfE7 = nan_rows = df[df['PresBarometric'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN PresBarometric ------------------------------')
                print('\n'*2)
                print(dfE7)
                
                nameColum='PresBarometric'
                TitleGrafica='Grafica PresBarometric'
                dfExcel=dfE7
                dfPLT=df.PresBarometric
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;    
                
            elif(opcion == 8 ):
            
                dfE8= nan_rows = df[df['Precipitacion'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN Precipitacion ------------------------------')
                print('\n'*2)
                print(dfE8)
                
                nameColum='Precipitacion'
                TitleGrafica='Grafica Precipitacion'
                dfExcel=dfE8
                dfPLT=df.Precipitacion
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                
                
            elif(opcion == 9 ):
            
                dfE9= nan_rows = df[df['RadSolar'].isnull()]
                print('\n'*3)
                print('------------------------ VALOR NaN RadSolar ------------------------------')
                print('\n'*2)
                print(dfE9)
                
                nameColum='RadSolar'
                TitleGrafica='Grafica RadSolar'
                dfExcel=dfE9
                dfPLT=df.RadSolar
                
                Grafica()
                GenEXCEL()
                GenPDF()
                break;
                
            else:
                print('\n'*2)
                print(' XXXXXXXXXXXXXXXXXXXXXXXX  ERROR  XXXXXXXXXXXXXXXXXXXXXXXXXXX  ' )
                break;
        
else:
    print('XXXXXXXXXXXXXXXXXXX  NO EXISTE ESTE FORMATO  XXXXXXXXXXXXXXXXXXXXXXXXX  ' )   
    
    
