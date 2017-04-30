#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
//------------------ Declaracion de variables
int i;
int j;
int t;
double v = 0.00001;
double longitud=1;
double dx=0.01;
double Thot=100;
double Tcold=50;
int linea=longitud/dx;  //Tamano de la fila
FILE *Abierta;
Abierta=fopen("Abierta.txt","w");
FILE *Periodica;
Periodica=fopen("Periodica.txt","w");
FILE *Fija;
Fija=fopen("Fija.txt","w");

//------------------ punteros 
double *x;                                 // lista que ordena la matriz de puntos en x
x= malloc((linea*linea) * sizeof(double)); 
double *y;                                 // lista que ordena la matriz de puntos en y
y= malloc((linea*linea) * sizeof(double)); 
double *T;                                 // lista que asigna las temperaturas a cada punto
T=malloc((linea*linea) * sizeof(double));  
double *Tfuturo;                           // Lista para las temperaturas con t=t+1
Tfuturo=malloc((linea*linea)*sizeof(double));
double *Time;                              // Asignacion lista de tiempo(s)
Time=malloc(2500*sizeof(int));
double *Tmean;
Tmean=malloc(2500*sizeof(double));


//----------------- asignacion de matrices
//valores x y y
for(i=0; i<linea; i++)
{
	for(j=0; j<linea; j++)
	{
		x[i*linea + j] = j* dx;
		y[i*linea + j] = i* dx;	
		//printf(" %f ---%f  \n ", x[i*n + j], y[i*n + j]);
	}
}

//Asignar las temperaturas a cada punto 
 for(i=0; i<linea*linea; i++)
 {
	T[i]=Tcold;
	if(y[i]>= 0.45 && y[i]<= 0.55)
	{
		if(x[i]>= 0.20 && x[i]<= 0.40)
		{
			T[i]=Thot;
		}
	}
	//printf("%f %f %f \n ", T[i], x[i],y[i]);
}

// ----------------- Condiciones de frontera ------------------------- //
//--frontera periodica
// i es la posicion sobre la linea de la lamina, N es el tamaño de la matriz de puntos (linea*linea), y linea la longitud de cada fila
for(t=0; t<2500; t++)
{
	Time[t]=t;
	for(i=0; i<linea*linea; i++)
	{
		if(Time[t]==0.0 && i<linea*linea)
		{
			Tfuturo[i]=T[i];			  // Tiempo 0
		}
		else if(i<(linea*linea)-linea)          // Arriba
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i+linea]+T[i-linea]+T[i-1]+T[i-linea+1]);
		}
		else if(i<linea)                       // Abajo
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i+linea]+T[linea*linea-linea+i]+T[i+1]+T[i-1]);
		}
		else if(x[i]==0.0)                    //Izquierda
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i+linea]+T[i-linea]+T[i+linea-1]+T[i+1]);
		}
		else if(x[i]==0.9)                    // Derecha
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i+linea]+T[i-linea]+T[i-1]+T[i-linea+1]);
		}
		else                            //Centro
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i-1]+T[i+1]+T[i+linea]+T[i-linea]);
		}
		Tmean[t]=Tfuturo[i]/linea*linea;
		fprintf(Periodica,"%f %f %f %f %f \n ", Time[t],x[i],y[i],Tfuturo[i],Tmean[t]);
	}
}

//--- Frontera abierta
for(t=0; t<2500; t++)
{
	Time[t]=t;
	for(i=0; i<linea*linea; i++)
	{
		if(Time[t]==0.0 && i<linea*linea)
		{
			Tfuturo[i]=T[i];			  // Tiempo 0
		}
		else if(i<(linea*linea)-linea)         // Arriba
		{
			Tfuturo[i]=T[i-linea];
		}
		else if(i<linea)                      // Abajo
		{
			Tfuturo[i]=T[i+linea];
		}
		else if(x[i]==0.0)                     // Izquierda
		{
			Tfuturo[i]=T[i+1];
		}
		else if(x[i]==0.9)                   // Derecha
		{
			Tfuturo[i]=T[i-linea];
		}
		else                           //Centro
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i-1]+T[i+1]+T[i+linea]+T[i-linea]);
		}
		Tmean[t]=Tfuturo[i]/linea*linea;
		fprintf(Abierta,"%f %f %f %f %f \n ", Time[t],x[i],y[i],Tfuturo[i],Tmean[t]);
	}

}

//--- Frontera fija
for(t=0; t<2500; t++)
{
	Time[t]=t;
	for(i=0; i<linea*linea; i++)
	{
		if(Time[t]==0.0 && i<linea*linea)
		{
			Tfuturo[i]=T[i];			  // Tiempo 0
		}
		else if(i<(linea*linea)-linea)         // Arriba
		{
			Tfuturo[i]=T[i];
		}
		else if(i<linea)                      // Abajo
		{
			Tfuturo[i]=T[i];
		}
		else if(x[i]==0.0)                     // Izquierda
		{
			Tfuturo[i]=T[i];
		}
		else if(x[i]==0.9)                   // Derecha
		{
			Tfuturo[i]=T[i];
		}
		else                           //Centro
		{
			Tfuturo[i]=T[i]+v*((-4*T[i])+T[i-1]+T[i+1]+T[i+linea]+T[i-linea]);
		}
		Tmean[t]=Tfuturo[i]/linea*linea;
		fprintf(Fija,"%f %f %f %f %f \n ", Time[t],x[i],y[i],Tfuturo[i],Tmean[t]);
	}

}

fclose(Periodica);
fclose(Abierta);
fclose(Fija);

return (0);
}