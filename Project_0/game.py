# coding=1251

import numpy as np
number = np.random.randint(1,101)      # �������� �����
print ("�������� ����� �� 1 �� 100")
for count in range(1,101):         # ����� ���������� ������� ��������
  if number == count: break      # ����� �� �����, ���� �������
print (f"�� ������� ����� {number} �� {count} �������.")

 