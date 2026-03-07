# import logging 

# logging.basicConfig(level=logging.INFO)

# def sqrt(x,guess=1.0):
#     if x<0:
#         logging.error("Cannot compute square root of negative number")
#         return None
#     logging.info("Calculating square root for x",x)
#     if good_guess(guess,x):
#         logging.info("Guess you choose is Good",guess)
#         return guess
#     else:
#         new_guess = improve_guess(guess,x)
#         logging.info("Function Ended")
#         return sqrt(x,new_guess)  
# def good_guess(guess,x):
#     return abs(guess*guess - x) < 0.0001  
# def improve_guess(guess,x):
#     return (guess + x / guess) / 2
    
  
# sqrt(36)


def sum (a, b ):
    return a+b
