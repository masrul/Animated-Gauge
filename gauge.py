import numpy as np 
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import sys 
import matplotlib as mpl 
import math 
from matplotlib import rc,rcParams

# change rc parameter 

rc('font', family='sans-serif', serif='cm10')
rcParams["xtick.labelsize"] = 20 
rcParams['axes.linewidth'] = 2.0 
# set radius of dial and 
r=5.0
nframes=100

# create data 
thetas=np.linspace(0,180,nframes)
thetas=np.flip(thetas)
r=np.arange(nframes, dtype=np.float)
r[:]=5.0 

# set plot, labelling 
fig = plt.figure(figsize=(6,4))
ax = fig.add_axes([0.05, 0.05, 0.95, 0.95], polar=True, facecolor='cornsilk')
ax.set_xlim(0,np.pi)
ax.set_ylim(0,4.50)
ax.grid(True)
labels=[r'$\boldmath{10~s}$',r'$\boldmath{5~s}$',r'$\boldmath{0~s}$']
ax.set_thetagrids(range(0,181,90),labels=labels)
ax.set_rgrids(range(0,0,15))
for spine in ax.spines.values():
    spine.set_edgecolor('orange')

ax.set_yticklabels([])
ax.tick_params(axis='x', pad=12)

# animation 
ims=[]
nframes=len(thetas)
duration=10 #sec 
fps=nframes/duration
interval=(duration*1000)/nframes 

ax.plot(90.0/np.pi*180.0,0,marker='o',ms=30, color='navy',zorder=10)
for i in range(nframes):
    theta=thetas[i]
    arrow=ax.arrow(theta/180.*np.pi,0,0.0,.1,
            width=1.,
            head_length=4.0,
            edgecolor = 'maroon', 
            facecolor = 'maroon', 
            lw = 4, zorder = 5
            )
    endpoint,=ax.plot(theta/180.0*np.pi,4.05,marker='o',ms=7, color='navy',zorder=10)
    
    ims.append([arrow,endpoint])

ani = animation.ArtistAnimation(fig,ims,interval=interval)
ani.save('animation-gauge.mp4',fps=fps, dpi=300)
plt.show()



