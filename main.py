"""
        Two sum from https://leetcode.com/problems/two-sum
"""

# TODO

# Сделать хэш-таблицу с ключами по индексам, т.е.

# {0:7, 1:9, ... }

# Реализовать one pass решение из leetcode

# Оценить работу программы с использованием структур из
# collections


class Solution:

    def deco(func):
        import functools
        import time

        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()  # начало таймера
            result = func(*args, **kwargs)
            end_time = time.time()  # завершение таймера
            time_delta = end_time - start_time
            print(f'Время выполнения кода {func.__name__} заняло: {time_delta}')
            return result

        return inner

    @staticmethod
    @deco
    def two_sum_brute(nums, target):  # staticmethod(deco(two_sum_brute))
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """

        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[j] == target - nums[i]:
                    return [i, j]

    @staticmethod
    @deco
    def two_sum(nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        length = len(nums)
        nums_map = dict()
        for i in range(length):
            nums_map[nums[i]] = i

        for i in range(length):
            diff = target - nums[i]

            if (diff in nums_map.keys()) and (nums_map.get(diff, -1) != i):
                return [i, nums_map.get(diff)]


Solution.two_sum_brute([2, 7, 11, 15], 9)

assert Solution.two_sum_brute([2, 7, 11, 15], 9) == [0, 1], 'проверка случая с единственным сочетанием элементов'

Solution.two_sum([2, 7, 11, 15], 9)

assert Solution.two_sum([2, 7, 11, 15], 9) == [0, 1], 'проверка случая с единственным сочетанием элементов'

if __name__ == '__main__':
    import timeit

    # print(timeit.timeit("test()", setup="from __main__ import test"))

# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Шаги решения:
# 1. Решаем "влоб", оцениваем время работы.
# 2. timeit
# 2a. Декоратор
# 3. Решаем с хэш-таблицей (словарь)
# 4. Улучшение с помощью модуля collections?
# 5. Замеряем время работы
# 6. Делаем выводы
