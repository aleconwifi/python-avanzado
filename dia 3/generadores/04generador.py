
import sys 

def primeros_num(n):
  nums = []
  for i in range(n):
    nums.append(i)
  return nums

print('Suma con for', sum(primeros_num(100000)))
print( 'Size List', sys.getsizeof(primeros_num(1000000)))


def primeros_num_gen(n):
  num = 0
  for i in range(n):
    yield num
    num = num + 1

print('Suma con generator', sum(primeros_num_gen(100000)))
print( 'Size Generator', sys.getsizeof(primeros_num_gen(1000000)))

