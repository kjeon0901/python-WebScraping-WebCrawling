import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 10, 0.01)
sin_y = np.sin(time)
cos_y = np.cos(time)

plt.figure('sin, cos 그래프')

plt.plot(time, sin_y, label='sin')  # label 인자로 범례설정
plt.plot(time, cos_y, label='cos')  # label 인자로 범례설정

plt.legend()

plt.xlabel('time') # x축
plt.ylabel('value')  # y 축
plt.title('sin, cos Graph')  # 그래프 이름

plt.grid()  # 그리드 설정
plt.show()  # 그래프 보이기
