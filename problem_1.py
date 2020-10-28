def sqrt(number):
  target_num = number
  if is_number(number) == False:
    return 'please input int'
  if number < 1:
    return 0
  if number == 1:
    return 1
  return recursive_sqrt(number // 2, target_num, number)

def recursive_sqrt(number, target_num, prev_num):
  if number == 1:
    return 1
  elif number ** 2 == target_num or (number ** 2 < target_num and (number + 1) ** 2 > target_num):
    return number
  else:
    if number ** 2 > target_num:
      number = recursive_sqrt(number // 2, target_num, number)
    elif number ** 2 < target_num:
      next_num = (prev_num + number) // 2

      if prev_num > next_num:
        next_num = (prev_num + next_num) // 2
        number = prev_num

      number = recursive_sqrt(next_num, target_num, number)
    return number

def is_number(element):
  return isinstance(element, int)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# # Pass
print ("Pass" if  (5 == sqrt(None)) else "Fail")
# # Fail
print ("Pass" if  (33 == sqrt(1112)) else "Fail")
# Pass
print ("Pass" if  (3335151 == sqrt(11123234567890)) else "Fail")
# Pass
# 値を半分にしていき2乗と同じまたは隣り合う数の二乗の範囲内に収まるならそれをrootのnumberとしている