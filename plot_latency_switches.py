import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline



flows = np.array([2.0, 4.0, 8.0, 16.0])

nox = np.array([4065.48, 4022.32, 4177.84, 4161.81])

pox = np.array([1262.09, 2017.97, 2931.82, 3745.14])

floodlight = np.array([50238.8, 69339.3, 67548.39, 89125.13])

odl = np.array([14784.65, 24907.08, 32013.89, 33319.65])

onos = np.array([40017.31, 61511.5, 76191.99, 84004.96])

ryu = np.array([5339.74, 5547.86, 5876.22, 6055.96])

openmul = np.array([18312.97, 27925.67, 28243.72, 31526.1])

beacon = np.array([60949.66, 74319.42, 75640.05, 76893.87])

maestro = np.array([15893.59, 21302.06, 22734.11, 22868.69])


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

plt.plot(flows_smooth,floodlight_smooth, linewidth=1.5, linestyle="-", label='floodlight')
plt.plot(flows_smooth,onos_smooth, linewidth=1.5, linestyle="-", label='onos')
plt.plot(flows_smooth,beacon_smooth, linewidth=1.5, linestyle="-", label='beacon')

#plt.xlabel('Number of Loops')
#plt.ylabel('Responses per Second')
plt.grid(True)
plt.legend(loc='lower right', fancybox=True, framealpha=0.3)
plt.title('Latency per Switches')

################################################################################################

plt.subplot(3, 1, 2)

plt.plot(flows_smooth,odl_smooth, linewidth=1.5, linestyle="-", label='odl')
plt.plot(flows_smooth,openmul_smooth, linewidth=1.5, linestyle="-", label='openmul')
plt.plot(flows_smooth,maestro_smooth, linewidth=1.5, linestyle="-", label='maestro')

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
