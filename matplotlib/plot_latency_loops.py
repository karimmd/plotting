import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline



flows = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

nox = np.array([4930.4, 4121.1, 4126.2, 4382.6, 4367.4, 4090.2, 3925.4, 4133.5, 4035, 4125.3, 4438.6, 4020.8, 4023.6, 4090.7, 4475.9, 4036.8, 4027.5, 4289.5, 4277.19, 4023.6])


pox = np.array([2691.3, 3760.2, 3733.6, 3770.2, 3738, 3767.4, 3747.6, 3715, 3723.3, 3763.3, 3751.3, 3748.4, 3761.8, 3770.3, 3702.8, 3707.6, 3767.6, 3754, 3759.6, 3750.8])


floodlight = np.array([70267.86, 87887.23, 88313.62, 87981.36, 88836.76, 89193.84, 91292.16, 89225.98, 89809.46, 91848.18, 89415.63, 87345.12, 88879.91, 87742.86, 89215.78, 88361.18, 89311.59, 89228.7, 90361.91, 89683.43])


odl = np.array([37104.29, 34932.3, 38227.12, 38692.1, 38042.55, 38604.85, 38358.7, 38260.84, 38458.85, 38666.19, 38127.5, 38471.8, 35847.4, 38357.8, 36731.89, 37127, 36860.95, 35523.9, 37582.9, 37996.05])


onos = np.array([62887.35, 82547.76, 83639.27, 85031.87, 85110.41, 83252.7, 83561.97, 83053.76, 83284.28, 84636.61, 83703.22, 84132.3, 84002.01, 84294.81, 82746.56, 84793.63, 83769.63, 85066.28, 83026.72, 83361.48])


ryu = np.array([5965.5, 6072, 6057.6, 6072, 6088.9, 6076.8, 6072.3, 6051.7, 6048, 6078.7, 6032.3, 6048, 6048.2, 6025, 6033.6, 6048.3, 6054.6, 6059.4, 6027.2, 6060.8])


openmul = np.array([28824.4, 31941.69, 31762.4, 30969, 31778.6, 32031.8, 31281, 32205.5, 31590.1, 30266.4, 30151.5, 32067.2, 32078.5, 31745.5, 30987.3, 30697.3, 32252.9, 31913.7, 31479.5, 31796.1])


beacon = np.array([77011.79, 77470.92, 77611.99, 77765.18, 77731.35, 78030.25, 77883.98, 77426.79, 77399.16, 77108.67, 77613.18, 77832.88, 75637.65, 76025.42, 75969.55, 76387.35, 74237.29, 75641.25, 77809.45, 77021.38])

maestro = np.array([16923.2, 20818.8, 19158, 19696, 22282.4, 22576, 23290.8, 23958.8, 23874, 23882.8, 23901.2, 23557.6, 23342.4, 23494, 23141.8, 23193.2, 23213.6, 23336.4, 23241.2, 23202])


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

plt.xlabel('Number of Loops')
#plt.ylabel('Responses per Second')
plt.grid(True)
plt.legend(loc='lower right', fancybox=True, framealpha=0.3)

#plt.title('Latency per 16 CBench Loops')

plt.show()
