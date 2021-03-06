# # -*- coding: utf-8 -*-
# """
# Created on Wed Dec  4 14:31:48 2019
#
# @author: majie
# """
#
# import numpy as np;
# np.random.seed(0)
# import seaborn as sns;
# sns.set()
# import matplotlib.pyplot as plt
#
# img_to_img = [[2.50000000e-01, 4.64288506e-28, 3.38559431e-34, 1.24999985e-01,
#                7.40811361e-28, 1.21071935e-08, 2.50000000e-01, 1.25000000e-01,
#                0.00000000e+00, 7.72665294e-33, 2.19590367e-23, 5.19231548e-32,
#                0.00000000e+00, 1.25000000e-01],
#               [4.99998003e-01, 1.24999911e-01, 0.00000000e+00, 1.25000000e-01,
#                9.28927103e-24, 3.93361472e-17, 2.21353316e-28, 0.00000000e+00,
#                3.08650650e-37, 2.42937281e-36, 1.25002086e-01, 2.77457096e-43,
#                0.00000000e+00, 1.25000000e-01],
#               [2.49987319e-01, 1.40129846e-45, 6.28797557e-23, 1.84116646e-29,
#                1.79586104e-15, 2.15202595e-35, 2.50000000e-01, 1.56258764e-20,
#                3.83008512e-12, 0.00000000e+00, 1.25000000e-01, 1.27315598e-33,
#                0.00000000e+00, 2.49998331e-01],
#               [5.00000000e-01, 3.70554087e-15, 0.00000000e+00, 1.25000000e-01,
#                0.00000000e+00, 8.49289009e-13, 0.00000000e+00, 0.00000000e+00,
#                0.00000000e+00, 4.69501716e-13, 2.50000000e-01, 0.00000000e+00,
#                0.00000000e+00, 1.25000000e-01],
#               [2.49999836e-01, 0.00000000e+00, 1.34037914e-21, 2.80560972e-40,
#                2.00832635e-20, 1.40129846e-44, 2.50000000e-01, 1.25000000e-01,
#                1.98098416e-29, 4.71295354e-36, 1.65483712e-07, 1.83151409e-32,
#                0.00000000e+00, 2.50000000e-01],
#               [5.00000000e-01, 2.47110554e-09, 0.00000000e+00, 1.25000000e-01,
#                5.09512122e-42, 4.39721696e-15, 2.28442647e-21, 0.00000000e+00,
#                0.00000000e+00, 6.22416971e-32, 2.50000000e-01, 3.41916825e-43,
#                0.00000000e+00, 1.25000000e-01],
#               [1.05423078e-01, 2.01592445e-01, 1.79851475e-28, 3.54482353e-07,
#                1.25000000e-01, 2.92353576e-12, 1.25000000e-01, 1.04054794e-34,
#                1.49943111e-02, 3.54240609e-26, 1.77989781e-01, 6.82536689e-36,
#                9.79062342e-09, 2.50000000e-01],
#               [1.25000000e-01, 5.42353228e-12, 7.20925954e-18, 2.82016055e-12,
#                2.63373376e-08, 4.60475116e-28, 1.25000000e-01, 1.53291581e-34,
#                3.68440935e-14, 2.81716807e-23, 2.49999970e-01, 1.52115831e-27,
#                1.24882482e-01, 2.50000000e-01],
#               [3.75000000e-01, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
#                1.16987656e-22, 0.00000000e+00, 2.50000000e-01, 1.25000000e-01,
#                3.40215887e-15, 0.00000000e+00, 1.30180627e-42, 3.75525894e-31,
#                0.00000000e+00, 1.25000045e-01],
#               [6.11169696e-01, 2.12221921e-17, 0.00000000e+00, 6.91723230e-08,
#                3.85967486e-35, 1.51204938e-12, 0.00000000e+00, 0.00000000e+00,
#                6.11497458e-22, 1.24999925e-01, 1.25000000e-01, 0.00000000e+00,
#                0.00000000e+00, 1.25000000e-01],
#               [2.49998808e-01, 2.24910293e-17, 6.87324928e-07, 3.95717397e-02,
#                9.39421081e-17, 8.54282603e-02, 1.25000179e-01, 5.31141908e-10,
#                1.21072187e-42, 8.05190523e-25, 1.25000000e-01, 1.12255576e-22,
#                0.00000000e+00, 1.25000000e-01],
#               [2.52182931e-01, 8.87179436e-13, 5.28800995e-40, 1.00344468e-33,
#                1.22817069e-01, 1.03074500e-20, 2.50000000e-01, 0.00000000e+00,
#                1.41397588e-28, 0.00000000e+00, 1.25000000e-01, 1.43131920e-22,
#                0.00000000e+00, 2.50000000e-01],
#               [2.75490999e-01, 1.22216995e-26, 0.00000000e+00, 1.25000000e-01,
#                8.27537502e-32, 3.53835320e-12, 1.25000000e-01, 1.11054349e-24,
#                0.00000000e+00, 8.40779079e-45, 1.25000000e-01, 5.02756398e-24,
#                0.00000000e+00, 1.25000000e-01],
#               [3.75000000e-01, 2.88489778e-23, 0.00000000e+00, 0.00000000e+00,
#                6.19552239e-12, 3.70210443e-39, 2.50000000e-01, 1.25000000e-01,
#                1.24272361e-01, 0.00000000e+00, 0.00000000e+00, 5.97874377e-25,
#                0.00000000e+00, 1.25243858e-01]]
#
# img_to_ques = [[0.17243944, 0.11383596, 0.2763755, 0.2496493, 0.1876998],
#                [0.20537847, 0.11077999, 0.2486122, 0.32798395, 0.10724542],
#                [0.15631968, 0.10285641, 0.3175846, 0.27061024, 0.1526291],
#                [0.22875626, 0.12324862, 0.23305064, 0.3229933, 0.09195115],
#                [0.17091578, 0.11308139, 0.2794897, 0.23939577, 0.19711734],
#                [0.20974836, 0.11312319, 0.24218428, 0.33595115, 0.09899307],
#                [0.28771493, 0.20174114, 0.29560262, 0.13380657, 0.08113472],
#                [0.3226854, 0.22605318, 0.2430469, 0.10765542, 0.10055913],
#                [0.16272706, 0.11721832, 0.31334037, 0.23898695, 0.16772726],
#                [0.20960878, 0.11357054, 0.23937684, 0.32333156, 0.11411229],
#                [0.27597696, 0.18625547, 0.22891703, 0.16515198, 0.14369859],
#                [0.24267754, 0.17693126, 0.32172585, 0.16663817, 0.0920272],
#                [0.20006591, 0.14145614, 0.26515093, 0.25555107, 0.13777593],
#                [0.16200007, 0.11175721, 0.26626536, 0.3304194, 0.12955797]]
#
# ques_to_img = [[0.01996823, 0.01853671, 0.02175271, 0.03380387, 0.1029, 0.03820533,
#                 0.07306205, 0.09747708, 0.02842714, 0.02278875, 0.03949055, 0.03704789, 0.04696754, 0.06089079],
#                [0.02120521, 0.02004461, 0.02205413, 0.03548722, 0.10317884, 0.03755744,
#                 0.07315425, 0.09339094, 0.03124494, 0.02273483, 0.03334457, 0.03775161, 0.04925591, 0.05538353],
#                [0.07023686, 0.02063289, 0.02975435, 0.02168505, 0.10342558, 0.0205133,
#                 0.02746727, 0.03112916, 0.05437697, 0.03419766, 0.00964225, 0.04686771, 0.00781624, 0.10181677],
#                [0.05265766, 0.03085848, 0.03918853, 0.0365004, 0.08260331, 0.0284658,
#                 0.02490009, 0.04478282, 0.05493039, 0.04039419, 0.01280532, 0.0387696, 0.0380981, 0.12236947],
#                [0.05864368, 0.03173285, 0.04372377, 0.02746271, 0.09324255, 0.02666025,
#                 0.03672605, 0.05957265, 0.06904224, 0.03264423, 0.0158533, 0.05659829, 0.02487095, 0.07467097]]
#
# ques_to_ques = [[0.12325358, 0.20996873, 0.1646173, 0.12385616, 0.3783042],
#                 [0.14089167, 0.1913202, 0.1891438, 0.14916715, 0.3294772],
#                 [0.20132962, 0.20499194, 0.13775419, 0.13402845, 0.32189584],
#                 [0.24361092, 0.18541586, 0.14768064, 0.11200446, 0.31128812],
#                 [0.27020746, 0.21306331, 0.1595145, 0.08972488, 0.26748982]
#                 ]
#
# ax0 = plt.subplot(2, 2, 1)
# ax0 = sns.heatmap(ques_to_ques, robust=True, cmap='Oranges', square=False, linewidths=.5)
# ax0.tick_params(axis='x', labeltop=True, labelbottom=False)
#
# # ax.xaxis.tick_top()
# ax0.spines['right'].set_color('red')
# plt.xticks(np.array(range(5)) + 0.5, ('Is', 'this', 'rice', 'noodle', 'soup'), rotation=45)
# plt.yticks(np.array(range(5))+0.5, ('Is', 'this', 'rice', 'noodle', 'soup'),rotation=-360)
#
# ax1 = plt.subplot(2, 2, 3)
# ax1 = sns.heatmap(img_to_img, robust=True, cmap='Oranges', square=False, linewidths=.5)
# ax1.tick_params(axis='x', labeltop=True, labelbottom=False)
#
# ax2 = plt.subplot(2, 2, 2)
# ax2 = sns.heatmap(ques_to_img, robust=True, cmap='Oranges', square=False, linewidths=.5)
# plt.yticks(np.array(range(5))+0.5, ('Is', 'this', 'rice', 'noodle', 'soup'),rotation=-360)
# ax2.tick_params(axis='x', labeltop=True, labelbottom=False)
#
# ax3 = plt.subplot(2, 2, 4)
# ax3 = sns.heatmap(img_to_ques, robust=True, cmap='Oranges', square=False, linewidths=.5)
# plt.xticks(np.array(range(5)) + 0.5, ('Is', 'this', 'rice', 'noodle', 'soup'), rotation=45)
# ax3.tick_params(axis='x', labeltop=True, labelbottom=False)
#
# plt.tight_layout()
#
# plt.savefig('intra&inter.png', dpi=600)
# plt.show()
#
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:31:48 2019

@author: majie
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:31:48 2019

@author: majie
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:31:48 2019

@author: majie
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:31:48 2019

@author: majie
"""

import numpy as np;
np.random.seed(0)
import seaborn as sns;
sns.set()
import matplotlib.pyplot as plt

img_to_img = [[2.50000000e-01, 4.64288506e-28, 3.38559431e-34, 1.24999985e-01,
               7.40811361e-28, 1.21071935e-08, 2.50000000e-01, 1.25000000e-01,
               0.00000000e+00, 7.72665294e-33, 2.19590367e-23, 5.19231548e-32,
               0.00000000e+00, 1.25000000e-01],
              [4.99998003e-01, 1.24999911e-01, 0.00000000e+00, 1.25000000e-01,
               9.28927103e-24, 3.93361472e-17, 2.21353316e-28, 0.00000000e+00,
               3.08650650e-37, 2.42937281e-36, 1.25002086e-01, 2.77457096e-43,
               0.00000000e+00, 1.25000000e-01],
              [2.49987319e-01, 1.40129846e-45, 6.28797557e-23, 1.84116646e-29,
               1.79586104e-15, 2.15202595e-35, 2.50000000e-01, 1.56258764e-20,
               3.83008512e-12, 0.00000000e+00, 1.25000000e-01, 1.27315598e-33,
               0.00000000e+00, 2.49998331e-01],
              [5.00000000e-01, 3.70554087e-15, 0.00000000e+00, 1.25000000e-01,
               0.00000000e+00, 8.49289009e-13, 0.00000000e+00, 0.00000000e+00,
               0.00000000e+00, 4.69501716e-13, 2.50000000e-01, 0.00000000e+00,
               0.00000000e+00, 1.25000000e-01],
              [2.49999836e-01, 0.00000000e+00, 1.34037914e-21, 2.80560972e-40,
               2.00832635e-20, 1.40129846e-44, 2.50000000e-01, 1.25000000e-01,
               1.98098416e-29, 4.71295354e-36, 1.65483712e-07, 1.83151409e-32,
               0.00000000e+00, 2.50000000e-01],
              [5.00000000e-01, 2.47110554e-09, 0.00000000e+00, 1.25000000e-01,
               5.09512122e-42, 4.39721696e-15, 2.28442647e-21, 0.00000000e+00,
               0.00000000e+00, 6.22416971e-32, 2.50000000e-01, 3.41916825e-43,
               0.00000000e+00, 1.25000000e-01],
              [1.05423078e-01, 2.01592445e-01, 1.79851475e-28, 3.54482353e-07,
               1.25000000e-01, 2.92353576e-12, 1.25000000e-01, 1.04054794e-34,
               1.49943111e-02, 3.54240609e-26, 1.77989781e-01, 6.82536689e-36,
               9.79062342e-09, 2.50000000e-01],
              [1.25000000e-01, 5.42353228e-12, 7.20925954e-18, 2.82016055e-12,
               2.63373376e-08, 4.60475116e-28, 1.25000000e-01, 1.53291581e-34,
               3.68440935e-14, 2.81716807e-23, 2.49999970e-01, 1.52115831e-27,
               1.24882482e-01, 2.50000000e-01],
              [3.75000000e-01, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
               1.16987656e-22, 0.00000000e+00, 2.50000000e-01, 1.25000000e-01,
               3.40215887e-15, 0.00000000e+00, 1.30180627e-42, 3.75525894e-31,
               0.00000000e+00, 1.25000045e-01],
              [6.11169696e-01, 2.12221921e-17, 0.00000000e+00, 6.91723230e-08,
               3.85967486e-35, 1.51204938e-12, 0.00000000e+00, 0.00000000e+00,
               6.11497458e-22, 1.24999925e-01, 1.25000000e-01, 0.00000000e+00,
               0.00000000e+00, 1.25000000e-01],
              [2.49998808e-01, 2.24910293e-17, 6.87324928e-07, 3.95717397e-02,
               9.39421081e-17, 8.54282603e-02, 1.25000179e-01, 5.31141908e-10,
               1.21072187e-42, 8.05190523e-25, 1.25000000e-01, 1.12255576e-22,
               0.00000000e+00, 1.25000000e-01],
              [2.52182931e-01, 8.87179436e-13, 5.28800995e-40, 1.00344468e-33,
               1.22817069e-01, 1.03074500e-20, 2.50000000e-01, 0.00000000e+00,
               1.41397588e-28, 0.00000000e+00, 1.25000000e-01, 1.43131920e-22,
               0.00000000e+00, 2.50000000e-01],
              [2.75490999e-01, 1.22216995e-26, 0.00000000e+00, 1.25000000e-01,
               8.27537502e-32, 3.53835320e-12, 1.25000000e-01, 1.11054349e-24,
               0.00000000e+00, 8.40779079e-45, 1.25000000e-01, 5.02756398e-24,
               0.00000000e+00, 1.25000000e-01],
              [3.75000000e-01, 2.88489778e-23, 0.00000000e+00, 0.00000000e+00,
               6.19552239e-12, 3.70210443e-39, 2.50000000e-01, 1.25000000e-01,
               1.24272361e-01, 0.00000000e+00, 0.00000000e+00, 5.97874377e-25,
               0.00000000e+00, 1.25243858e-01]]

img_to_ques = [[0.17243944, 0.11383596, 0.2763755, 0.2496493, 0.1876998],
               [0.20537847, 0.11077999, 0.2486122, 0.32798395, 0.10724542],
               [0.15631968, 0.10285641, 0.3175846, 0.27061024, 0.1526291],
               [0.22875626, 0.12324862, 0.23305064, 0.3229933, 0.09195115],
               [0.17091578, 0.11308139, 0.2794897, 0.23939577, 0.19711734],
               [0.20974836, 0.11312319, 0.24218428, 0.33595115, 0.09899307],
               [0.28771493, 0.20174114, 0.29560262, 0.13380657, 0.08113472],
               [0.3226854, 0.22605318, 0.2430469, 0.10765542, 0.10055913],
               [0.16272706, 0.11721832, 0.31334037, 0.23898695, 0.16772726],
               [0.20960878, 0.11357054, 0.23937684, 0.32333156, 0.11411229],
               [0.27597696, 0.18625547, 0.22891703, 0.16515198, 0.14369859],
               [0.24267754, 0.17693126, 0.32172585, 0.16663817, 0.0920272],
               [0.20006591, 0.14145614, 0.26515093, 0.25555107, 0.13777593],
               [0.16200007, 0.11175721, 0.26626536, 0.3304194, 0.12955797]]

ques_to_img = [[0.01996823, 0.01853671, 0.02175271, 0.03380387, 0.1029, 0.03820533,
                0.07306205, 0.09747708, 0.02842714, 0.02278875, 0.03949055, 0.03704789, 0.04696754, 0.06089079],
               [0.02120521, 0.02004461, 0.02205413, 0.03548722, 0.10317884, 0.03755744,
                0.07315425, 0.09339094, 0.03124494, 0.02273483, 0.03334457, 0.03775161, 0.04925591, 0.05538353],
               [0.07023686, 0.02063289, 0.02975435, 0.02168505, 0.10342558, 0.0205133,
                0.02746727, 0.03112916, 0.05437697, 0.03419766, 0.00964225, 0.04686771, 0.00781624, 0.10181677],
               [0.05265766, 0.03085848, 0.03918853, 0.0365004, 0.08260331, 0.0284658,
                0.02490009, 0.04478282, 0.05493039, 0.04039419, 0.01280532, 0.0387696, 0.0380981, 0.12236947],
               [0.05864368, 0.03173285, 0.04372377, 0.02746271, 0.09324255, 0.02666025,
                0.03672605, 0.05957265, 0.06904224, 0.03264423, 0.0158533, 0.05659829, 0.02487095, 0.07467097]]

ques_to_ques = [[0.12325358, 0.20996873, 0.1646173, 0.12385616, 0.3783042],
                [0.14089167, 0.1913202, 0.1891438, 0.14916715, 0.3294772],
                [0.20132962, 0.20499194, 0.13775419, 0.13402845, 0.32189584],
                [0.24361092, 0.18541586, 0.14768064, 0.11200446, 0.31128812],
                [0.27020746, 0.21306331, 0.1595145, 0.08972488, 0.26748982]
                ]



"""ques_to_img*=10
font1 = {'weight' : 'bold',
'size'   : 15,
}
"""

fig=plt.figure(figsize=(16,6),dpi=600)
#fig=plt.figure()



img = plt.imread('/data/kf/majie/codehub/mlvqa/noodle.png')
#ax1 = plt.subplot(2, 3, 1)
ax1 = fig.add_axes([0.05,0.55,0.2,0.3])
ax1 = plt.imshow(img)
plt.xticks([])
plt.yticks([])
#plt.axis('off')
plt.xlabel("image",labelpad=5.5,size=15)
#plt.subplots_adjust(left=0.01,right=0.8,bottom=0.5)
#ax1 = plt.subplot(2, 6, 2)
"""ax2=fig.add_axes([0.2,0.5,0.1,0.4])
ax2.arrow(0, 0.5, 0.5, 0, width=0.05,head_starts_at_zero=True)
plt.axis('off')
"""
#plt.tight_layout()

#plt.subplots_adjust(hspace=0.1,wspace=0.1)

#ax2 = plt.subplot(2, 3, 2)
ax2=fig.add_axes([0.27,0.55,0.25,0.3])
ax2 = sns.heatmap(img_to_img, robust=True, cmap='Oranges', square=False, linewidths=0,cbar=True)
ax2.tick_params(axis='x', labeltop=True, labelbottom=False)
plt.xlabel("region to region",size=15)

#ax3 = plt.subplot(2, 3, 3)
ax3=fig.add_axes([0.55,0.55,0.25,0.3])
ax3 = sns.heatmap(img_to_ques,robust=True, cmap='Oranges', square=False, linewidths=0,cbar=True)
plt.xticks(np.array(range(5)) + 0.5, ('Is', 'this', 'rice', 'noodle', 'soup'), rotation=0)
ax3.tick_params(axis='x', labeltop=True, labelbottom=False)
plt.xlabel("region to word",size=15)

#plt.tight_layout()
#ax4 = plt.subplot(2, 3, 4)
ax4=fig.add_axes([0.065,0.15,0.17,0.3])
question="Is this rice noodle soup? "
ax4=plt.text(0.5, 0.5, question, fontsize=15, alpha=0.8, ha='center', va='center')
plt.xticks([])
plt.yticks([])
#plt.axis("off")
plt.xlabel("question",size=15)

#plt.tight_layout()

#ax5 = plt.subplot(2, 3, 5)
ax5=fig.add_axes([0.27,0.15,0.25,0.3])
ax5 = sns.heatmap(ques_to_ques,robust=True, cmap='Oranges', square=False, linewidths=0,cbar=True)
ax5.tick_params(axis='x', labeltop=True, labelbottom=False)
# ax.xaxis.tick_top()
ax5.spines['right'].set_color('red')
plt.xticks(np.array(range(5)) + 0.5, ('Is', 'this', 'rice', 'noodle', 'soup'), rotation=0)
plt.yticks(np.array(range(5))+0.5, ('Is', 'this', 'rice', 'noodle', 'soup'),rotation=-360)
plt.xlabel("word to word",size=15)

#plt.tight_layout()

#ax6 = plt.subplot(2, 3, 6)
ax6=fig.add_axes([0.55,0.15,0.25,0.3])
#ax6 = sns.heatmap(ques_to_img, vmin=0.0,vmax=0.35,robust=True, cmap='Oranges', square=False, linewidths=0,cbar=True)
ax6 = sns.heatmap(ques_to_img,robust=True, cmap='Oranges', square=False, linewidths=0,cbar=True)
plt.yticks(np.array(range(5))+0.5, ('Is', 'this', 'rice', 'noodle', 'soup'),rotation=-360)
ax6.tick_params(axis='x', labeltop=True, labelbottom=False)
plt.xlabel("word to region",size=15)



#plt.tight_layout()
plt.savefig('intra&inter.png', dpi=600)
plt.show()











#ax_colorbar=fig.add_axes([0.77,0.1,0.01,0.7])cbar_ax=ax_colorbar,



"""
ax0 = plt.subplot(2, 3, 1)
ax0 = sns.heatmap(ques_to_ques, robust=True, cmap='Oranges', square=False, linewidths=.5)
ax0.tick_params(axis='x', labeltop=True, labelbottom=False)

# ax.xaxis.tick_top()
ax0.spines['right'].set_color('red')
plt.xticks(np.array(range(5)) + 0.5, ('Is', 'this', 'rice', 'noodle', 'soup'), rotation=45)
plt.yticks(np.array(range(5))+0.5, ('Is', 'this', 'rice', 'noodle', 'soup'),rotation=-360)

ax1 = plt.subplot(2, 3, 3)
ax1 = sns.heatmap(img_to_img, robust=True, cmap='Oranges', square=False, linewidths=.5)
ax1.tick_params(axis='x', labeltop=True, labelbottom=False)

ax2 = plt.subplot(2, 3, 2)
ax2 = sns.heatmap(ques_to_img, robust=True, cmap='Oranges', square=False, linewidths=.5)
plt.yticks(np.array(range(5))+0.5, ('Is', 'this', 'rice', 'noodle', 'soup'),rotation=-360)
ax2.tick_params(axis='x', labeltop=True, labelbottom=False)

ax3 = plt.subplot(2, 3, 4)
ax3 = sns.heatmap(img_to_ques, robust=True, cmap='Oranges', square=False, linewidths=.5)
plt.xticks(np.array(range(5)) + 0.5, ('Is', 'this', 'rice', 'noodle', 'soup'), rotation=45)
ax3.tick_params(axis='x', labeltop=True, labelbottom=False)


plt.tight_layout()

plt.savefig('intra&inter.png', dpi=600)
plt.show()
"""