import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline



flows = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

nox = np.array([1924.152, 2767.622, 3006.054, 7847.9, 9192.234, 6731.615, 6636.57, 5887.648, 4374.736, 5695.686, 4350.909, 5099.461, 4879.178, 5104.795, 4331.004, 5267.209, 6381.204, 7004.488, 6960.476, 6306.304])


pox = np.array([4668.647, 5123.896, 5123.896, 5025.784, 4906.798, 5107.068, 5210.583, 5178.938, 5322.502, 5440.137, 5261.091, 5530.649, 5602.543, 5597.090, 5616.487, 5264.528, 5429.232, 5332.687, 5596.257, 5581.556])


floodlight = np.array([99554.597, 140678.933, 138994.964, 137537.417, 137454.759, 141676.572, 139165.036, 140608.53, 143096.957, 140029.304, 140671.203, 138815.517, 140037.521, 138558.089, 139756.674, 141885.031, 143927.55, 140907.658, 138320.986, 142082.015])


odl = np.array([82097.097, 108253.051, 107764.981, 109572.789, 106054.424, 106887.055, 109975.821, 106374.083, 103919.895, 105701.527, 106674.369, 108325.987, 107827.33, 108935.958, 95835.346, 107552.841, 110117.879, 107064.714, 106512.218, 105838.403])


onos = np.array([159427.368, 383020.325, 478959.559, 474293.384, 477635.908, 475508.446, 473705.783, 471969.595, 477775.57, 474508.731, 472827.207, 478076.72, 484083.801, 475583.533, 475742.867, 480959.127, 471671.918, 475831.491, 481849.593, 477780.106])


ryu = np.array([8885.217, 9028.417, 9065.397, 8902.77, 8956.441, 8809.991, 8871.305, 9043.033, 9073.631, 9029.314, 8912.473, 8903.981, 8969.618, 9034.208, 8841.623, 8874.549, 8882.355, 8883.255, 8926.679, 9047.887])


openmul = np.array([119274.393, 148070.186, 148014.049, 147969.34, 147806.88, 147948.995, 147930.91, 147827.922, 147837.409, 147869.739, 147953.261, 147929.671, 147908.219, 147957.47, 147824.069, 147922.997, 147905.404, 147801.403, 147877.792, 147927.288])


beacon = np.array([99343.34, 101009.021, 101045.579, 101160.78, 102406.736, 102457.457, 101653.329, 100975.78, 102280.187, 101163.808, 101720.58, 101556.77, 100945.379, 101322.98, 101261.67, 102077.78, 102506.138, 102699.025, 101507.403, 100461.76])

maestro = np.array([83235.212, 100691.964, 97456.693, 97807.394, 95378.934, 94660.262, 96895.305, 93239.301, 97733.28, 98443.189, 98124.754, 98977.785, 101602.39, 92906.313, 93453.886, 94569.85, 93684.347, 102666.587, 91916.776, 94775.945])


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
plt.plot(flows_smooth,openmul_smooth, linewidth=1.5, linestyle="-", label='openmul')

#plt.xlabel('Number of Loops')
#plt.ylabel('Responses per Second')
plt.grid(True)
plt.legend(loc='lower right', fancybox=True, framealpha=0.3)



################################################################################################

plt.subplot(3, 1, 2)

plt.plot(flows_smooth,odl_smooth, linewidth=1.5, linestyle="-", label='odl')
plt.plot(flows_smooth,beacon_smooth, linewidth=1.5, linestyle="-", label='beacon')
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
