#!/usr/bin/env python3                                              # выбираем версию питона (вдруг, используемые модули есть не во всех версиях)
# -*- coding: utf-8 -*-                                             # объясняем интерпретатору кодировку скрипта

import math                                                         # импортируем модули (т.е. теперь мы можем использовать всё, что содержится в импортированном модуле)
import numpy                                                        # аналогично
import matplotlib.pyplot as mpp                                     # чтобы не переписывать название модуля при обращении к нему, переназовем его

if __name__=='__main__':                                            # если кто-то захочет импортировать эту программу, то условие неверно
    arguments = numpy.r_[0:200:0.1]                                 # создает одномерный массив от [0 до 200) с шагом 0.1
    mpp.plot(                                                       # вызов функции для создания графика
        arguments,                                                  # определяем точки по оси х или иначе - аргументы функции
        [math.sin(a) * math.sin(a/20.0) for a in arguments]         # каждой точке в соответствие ставим другую f(x), для создания графика
    )                                                               # завершаем вызов функции
    mpp.show()                                                      # отображает окно с графиком
