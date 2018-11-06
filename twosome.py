def deco(func):
  import time
  import functools
  import math 

  @functools.wraps(func)
  def inner(*args, **kwargs):
    start = time.time()
    res = func(*args, **kwargs)
    finish = time.time()

    delta = (finish - start)
    print(f'{func.__name__} works for {delta:2.3}')
    return res
  return  inner


@deco
def twoSumSlice( nums, target):
    result=[]
    for i in range(len(nums)):
        if target-nums[i] in nums[i+1::]:
            result.append(i)
            result.append(nums[i+1::].index((target-nums[i]))+i+1)
    return result

@deco
def twoSumDict(nums, target):
    collected = {}
    for index, val in enumerate(nums):
        diff = target - val
        if diff in collected:
            return [collected[diff], index]
        collected[val] = index
        #print(collected)  


if __name__ == "__main__":
  print(twoSumSlice((80,5,2,7,9,11), 9))     
  print(twoSumDict((80,5,2,7,9,11), 9))
  assert twoSumSlice([2, 7, 11, 15], 9) == [0, 1], 'проверка методом со слайсом'
  assert twoSumDict([2, 7, 11, 15], 9) == [0, 1], 'проверка методом со словарём'
