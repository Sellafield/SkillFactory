# coding=1251

import numpy as np
count = 0                           # счетчик попыток
number = np.random.randint(1,101)   # загадали число
print("Загадано число от 1 до 100")
    
while True:                        # бесконечный цикл
  predict = int(input())         # предполагаемое число
  count += 1                     # плюсуем попытку
  if number == predict: break    # выход из цикла, если угадали
  elif number > predict: print(f"Угадываемое число больше {predict} ")
  elif number < predict: print(f"Угадываемое число меньше {predict} ")
            
print (f"Вы угадали число {number} за {count} попыток.")