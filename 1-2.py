#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
1. Створіть три списки: int list, float_list i str_list. Користуючись пакетами
рандомізації, заповніть словник іпі. Іїзї випадковими цілочисельними
значеннями, у кількості 5000 елементів, в діапазоні від 0 до 1000.
Заповніть словник Досі /їзг випадковими значеннями, у кількості 5000
елементів, в діапазоні від 0.1 до 100.0. Також заповніть словник str_list
випадковими словами, теж у кількості 5000 елементів.

2. Додайте до попередньої програми код, будь-якого алгоритму
сортування. Додайте функцію, яка б обраховувала середній час роботи
алгоритму сортування. Функція повинна приймати список і кількість
ітерацій циклів сортування, а повертати середній час роботи алгоритму
сортування.
'''
import time
import random
from random_word import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    #str_list.append(w.get_random_word())

def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
               data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
               swapped = True
        if not swapped:
            break
    print("Bubble Sort: ", data)

time_checker = []
    
def avarage_time(lst, times):
    for i in range(times):
        cur_time = time.time()
        bubble_sort(lst)
        timer = time.time() - cur_time
        print(f"Duration time: {timer}")
        time_checker.append(timer)
        
    avar_time = sum(time_checker)/len(time_checker)
    print(f"Avarage bubble sort time: {avar_time}")
    
avarage_time(int_list, 5)
#avarage_time(float_list, 5)
#avarage_time(str_list, 5)

