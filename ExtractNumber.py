import re

repatter = re.compile('\D+(\d+)\D+')

s = 'abcde12345fghij'

result = repatter.match(s)

if result:
  num = result.group(1)
  print(num)
