from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import sys


#FRONTERA ABIERTA
#frontera abierta t=0
abierta_0=np.genfromtxt("Abierta.txt",skip_footer=2500*10000-100)
figAbierta=plt.figure()
ax=figAbierta.gca(projection='3d')
x0=abierta_0[:,1]
y0=abierta_0[:,2]
x0,y0=np.meshgrid(x0,y0)
z0=abierta_0[:,3]

surf=ax.plot_surface(x0,y0,z0,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figAbierta.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera abierta en t=0")
plt.savefig("abierta_0.png")

#frontera abierta t=100
abierta_100=np.genfromtxt("Abierta.txt",skip_header=2500*10000-99*1000,skip_footer=2500*10000-101*10000)
figAbierta=plt.figure()
ax=figAbierta.gca(projection='3d')
x100=abierta_100[:,1]
y100=abierta_100[:,2]
x100,y100=np.meshgrid(x100,y100)
z100=abierta_0[:,3]

surf=ax.plot_surface(x100,y100,z100,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figAbierta.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera abierta en t=0")
plt.savefig("abierta_100.png")


#frontera abierta t=2500
abierta_2500=np.genfromtxt("Abierta.txt",skip_header=2500*1000-2499*1000)
figAbierta=plt.figure()
ax=figAbierta.gca(projection='3d')
x2500=abierta_2500[:,1]
y2500=abierta_2500[:,2]
x2500,y2500=np.meshgrid(x2500,y2500)
z2500=abierta_0[:,3]

surf=ax.plot_surface(x2500,y2500,z2500,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figAbierta.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera abierta en t=2500")
plt.savefig("abierta_2500.png")




#FRONTERA FIJA
#frontera fija t=0
fija_0=np.genfromtxt("Fija.txt",skip_footer=2500*10000-100)
figFija=plt.figure()
ax=figFija.gca(projection='3d')
x0=fija_0[:,1]
y0=fija_0[:,2]
x0,y0=np.meshgrid(x0,y0)
z0=fija_0[:,3]

surf=ax.plot_surface(x0,y0,z0,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figFija.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera fija en t=0")
plt.savefig("fija_0.png")

#frontera fija t=100
fija_100=np.genfromtxt("Abierta.txt",skip_header=2500*10000-99*1000,skip_footer=2500*10000-101*10000)
figFija=plt.figure()
ax=figFija.gca(projection='3d')
x100=fija_100[:,1]
y100=fija_100[:,2]
x100,y100=np.meshgrid(x100,y100)
z100=fija_0[:,3]

surf=ax.plot_surface(x100,y100,z100,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figFija.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera fija en t=0")
plt.savefig("fija_100.png")


#frontera fija t=2500
abierta_2500=np.genfromtxt("Abierta.txt",skip_header=2500*1000-2499*1000)
FigFija=plt.figure()
ax=figFija.gca(projection='3d')
x2500=abierta_2500[:,1]
y2500=abierta_2500[:,2]
x2500,y2500=np.meshgrid(x2500,y2500)
z2500=abierta_0[:,3]

surf=ax.plot_surface(x2500,y2500,z2500,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figFija.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera fija en t=2500")
plt.savefig("fija_2500.png")


#FRONTERA PERIODICA
#frontera fija t=0
period_0=np.genfromtxt("Periodica.txt",skip_footer=2500*10000-100)
figPer=plt.figure()
ax=figPer.gca(projection='3d')
x0=period_0[:,1]
y0=period_0[:,2]
x0,y0=np.meshgrid(x0,y0)
z0=period_0[:,3]

surf=ax.plot_surface(x0,y0,z0,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figPer.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera periodica en t=0")
plt.savefig("periodica_0.png")

#frontera periodica t=100
period_100=np.genfromtxt("Periodica.txt",skip_header=2500*10000-99*1000,skip_footer=2500*10000-101*10000)
figPer=plt.figure()
ax=figPer.gca(projection='3d')
x100=period_100[:,1]
y100=period_100[:,2]
x100,y100=np.meshgrid(x100,y100)
z100=period_0[:,3]

surf=ax.plot_surface(x100,y100,z100,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figPer.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera periodica en t=0")
plt.savefig("periodica_100.png")


#frontera periodica t=2500
period_2500=np.genfromtxt("Periodica.txt",skip_header=2500*1000-2499*1000)
FigPer=plt.figure()
ax=figPer.gca(projection='3d')
x2500=period_2500[:,1]
y2500=period_2500[:,2]
x2500,period=np.meshgrid(x2500,y2500)
z2500=period_0[:,3]

surf=ax.plot_surface(x2500,y2500,z2500,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figPer.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Frontera periodica en t=2500")
plt.savefig("fija_2500.png")



#TEMPERATURA PROMEDIO
abierta=np.loadtxt("Abierta.txt")
figAbierta=plt.figure()
x=abierta[:,1]
y0=abierta[:,2]
x0,y0=np.meshgrid(x0,y0)
z0=abierta[:,4]

surf=ax.plot_surface(x0,y0,z0,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figAbierta.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Abierta promedio")
plt.savefig("abierta_promedio.png")



fija=np.LOADTXT("Fija.txt")
figFija=plt.figure()
ax=figFija.gca(projection='3d')
x0=fija[:,1]
y0=fija[:,2]
x0,y0=np.meshgrid(x0,y0)
z0=fija[:,4]

surf=ax.plot_surface(x0,y0,z0,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figFija.colorbar(surf, shrink=0.5, aspect=5)

plt.title("FIJA PROMEDIO")
plt.savefig("fija_promedio.png")



period=np.loadtxt("Periodica.txt")
FigPer=plt.figure()
ax=figPer.gca(projection='3d')
x2500=period[:,1]
y2500=period[:,2]
x2500,period=np.meshgrid(x2500,y2500)
z2500=period[:,4]

surf=ax.plot_surface(x2500,y2500,z2500,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_zlim(0,100)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
figPer.colorbar(surf, shrink=0.5, aspect=5)

plt.title("Periodica promedio")
plt.savefig("fija_promedio.png")
