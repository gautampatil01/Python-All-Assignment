#Check whether a string is a pangram.

def pangram(input):
  input = input.lower()
  input = set(input)

  ip1 = [ch for ch in input if ord(ch) in range(ord('a'), ord('z') + 1)]

  if len(ip1) == 26:
    return 'True'
  else:
    return 'False'

input = 'The quick brown fox jumps over the lazy dog'
print(pangram(input))
