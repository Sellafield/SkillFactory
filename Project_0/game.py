# coding=1251

import numpy as np

def game_core_v1(number):
  '''������ ��������� �� random, ����� �� ��������� ���������� � ������ ��� ������.
     ������� ��������� ���������� ����� � ���������� ����� �������'''
  count = 0
  while True:
    count += 1
    predict = np.random.randint(1, 101)  # �������������� �����
    if number == predict:
      return count  # ����� �� �����, ���� �������

def game_core_v2(number):
  '''������� ������������� ����� random �����, � ����� ��������� ��� ����������� ��� � ����������� �� ����, ������ ��� ��� ������ �������.
     ������� ��������� ���������� ����� � ���������� ����� �������'''
  count = 1

  predict = np.random.randint(1, 101)
  while number != predict:
    count += 1
    if number > predict:
      predict += 1
    elif number < predict:
      predict -= 1
  return (count)  # ����� �� �����, ���� �������

def int_r(num):
  num = int(num + (0.5 if num > 0 else -0.5))
  return num

def game_core_v3(number):
  '''������� ������������� ����� random �����, � ����� ��������� ��� ����������� ��� � ����������� �� ����, ������ ��� ��� ������ �������.
     ������� ��������� ���������� ����� � ���������� ����� �������'''
  count = 1

  predict = np.random.randint(1, 101)
  while number != predict:
    count += 1
    if number > predict:
      predict += int_r((number - predict) / 2)
    elif number < predict:
      predict -= int_r((predict - number) / 2)

  return (count)  # ����� �� �����, ���� �������

def score_game(game_core):
  '''��������� ���� 1000 ���, ����� ������, ��� ������ ���� ��������� �����'''
  count_ls = []
  np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
  random_array = np.random.randint(1, 101, size=(1000))
  for number in random_array:
    count_ls.append(game_core(number))
  score = int(np.mean(count_ls))
  print(f"��� �������� ��������� ����� � ������� �� {score} �������")
  return (score)

# ���������
score_game(game_core_v3)