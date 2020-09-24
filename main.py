# Author: Haorong Xu hxx5086@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 12
# Breakout: 

def num_of_divisors(n):
  d = 0
  i=1
  while i in range (1,n+1):
    if n%i == 0:
      d += 1
    i+=1 
  return d

def num_of_primes(n):
  p = 0
  for i in range (1,n+1):
    x = num_of_divisors(i)
    if x == 0:
      p+=1
    i += 1
  return p

def sum_n(n):
  i = 0
  s = 0
  while i<= n:
    s += i
    i += 1
  return s

def print_n(s, n):
  for i in range(1,1+n):
    print(s)
  return None

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  print(f"{num} has {num_of_divisors(num)} divisors.")
  print(f"There are {num_of_primes(num)} primes <= {num}.")
  line = input("Enter a string: ")
  print_n(line, num)



if __name__ == "__main__":
  run()