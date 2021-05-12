
# this is for finding square 
def square(number):
   result = number * number
   return result

# this is for finding cube 
def cube(number):
   result = number * number * number
   return result

# this is for finding mean
def mean(numbers):
   # do not declare this variables globally
   get_sum = sum(numbers)
   length = len(numbers)

   result = get_sum / length
   return result

# this is for converting weights
# this is for pound to kilogram
def lbs_to_kg(weight):
   return weight * 0.45

# this is for kilogram to pound 
def kg_to_lbs(weight):
   return weight / 0.45
