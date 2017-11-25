import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline



flows = np.array([2.0, 4.0, 8.0, 16.0])

nox = np.array([6809.810, 6833.61, 7112.8, 5736.92])

pox = np.array([4860.380, 5156.800, 5316.000, 5305.800])

floodlight = np.array([92506.17, 164002.41, 183918.57, 140195.17])

odl = np.array([87699.75, 84614.7, 90102.41, 106786.56])

onos = np.array([175369.08, 314848.36, 505059.74, 476195.85])

ryu = np.array([8985.41, 9139.05, 9303.77, 8940.87])

openmul = np.array([147310.26, 147633.79, 147940.72, 147910.47])

beacon = np.array([93531.85, 94430.19, 101550.51, 101702.12])

maestro = np.array([104978.25, 105185.34, 104997.96, 96725.02])


flows_smooth = np.linspace(flows.min(),flows.max(),300)

nox_smooth = spline(flows,nox, flows_smooth)
pox_smooth = spline(flows,pox, flows_smooth)
floodlight_smooth = spline(flows,floodlight, flows_smooth)
odl_smooth = spline(flows,odl, flows_smooth)
onos_smooth = spline(flows,onos, flows_smooth)
ryu_smooth = spline(flows,ryu, flows_smooth)
openmul_smooth = spline(flows,openmul, flows_smooth)
beacon_smooth = spline(flows,beacon, flows_smooth)
maestro_smooth = spline(flows,maestro, flows_smooth)



plt.figure(figsize=(10,6), dpi=120)

###############################################################################################
plt.subplot(3, 1, 1)

plt.plot(flows_smooth,onos_smooth, linewidth=1.5, linestyle="-", label='onos')
plt.plot(flows_smooth,openmul_smooth, linewidth=1.5, linestyle="-", label='openmul')
plt.plot(flows_smooth,floodlight_smooth, linewidth=1.5, linestyle="-", label='floodlight')



#plt.xlabel('Number of Loops')
#plt.ylabel('Responses per Second')
plt.grid(True)
plt.legend(loc='lower right', fancybox=True, framealpha=0.3)
plt.title('Throughput per Switches')

################################################################################################

plt.subplot(3, 1, 2)

plt.plot(flows_smooth,odl_smooth, linewidth=1.5, linestyle="-", label='odl')
plt.plot(flows_smooth,maestro_smooth, linewidth=1.5, linestyle="-", label='maestro')
plt.plot(flows_smooth,beacon_smooth, linewidth=1.5, linestyle="-", label='beacon')

#plt.xlabel('Number of Loops')
plt.ylabel('Responses per Second')
plt.grid(True)
plt.legend(loc='lower right', fancybox=True, framealpha=0.3)

##################################################################################################

plt.subplot(3, 1, 3)

plt.plot(flows_smooth,pox_smooth, linewidth=1.5, linestyle="-", label='pox')
plt.plot(flows_smooth,nox_smooth, linewidth=1.5, linestyle="-", label='nox')
plt.plot(flows_smooth,ryu_smooth, linewidth=1.5, linestyle="-", label='ryu')

plt.xlabel('Number of Switches')
#plt.ylabel('Responses per Second')
plt.grid(True)
plt.legend(loc='lower right', fancybox=True, framealpha=0.3)


plt.show()
