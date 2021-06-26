def function_decor(func):
  print("In decorator")
 
  def step_two(*args, **kwargs):
    print("Inside")
    print("Decorated the function")
    
    func()
     
  return step_two
 
@function_decor
def funct():
    print("Inside actual function")
 
funct()
