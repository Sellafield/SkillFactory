# coding=1251

import numpy as np
count = 0                           # ������� �������
number = np.random.randint(1,101)   # �������� �����
print("�������� ����� �� 1 �� 100")
    
while True:                        # ����������� ����
  predict = int(input())         # �������������� �����
  count += 1                     # ������� �������
  if number == predict: break    # ����� �� �����, ���� �������
  elif number > predict: print(f"����������� ����� ������ {predict} ")
  elif number < predict: print(f"����������� ����� ������ {predict} ")
            
print (f"�� ������� ����� {number} �� {count} �������.")