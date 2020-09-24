# Author: Haorong Xu hxx5086@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 12
# Breakout: 

def num_of_divisors(n):
  """
  given a positive int n, return number of divisors for n between 1-n inclusive
  You must use a while cond: style loop for this function.
  """
  divnum = 0
  i=1
  while i in range (1,n+1):
    if n%i == 0:
      divnum += 1
    i+=1 
  return divnum

def num_of_primes(n):
  """
  given a positive int n, return number of primes that is <= n.
  You must use num_of_divisors() function to help determine if a number is prime:
  a number is a prime if its number of divisors is 2.
  You must use a for... in range(...): style loop for this function.
  """
  numprime = 0
  for i in range (1,n+1):
    x = num_of_divisors(i)
    if x == 0:
      numprime+=1
    i += 1
  return numprime

def sum_n(n):
  """
  given a non-negative int n, return the sum 0+1+2+...+n
  You must use a while cond: style loop for this function.
  """
  i = 0
  sumnum = 0
  while i<= n:
    sumnum += i
    i += 1
  return sumnum

def print_n(s, n):
  """
  given a string s and a non-negative int n, print s n times
  you must use for ... in range(...): style loop for this function
  """
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