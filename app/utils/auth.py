from flask import session, redirect
from functools import wraps

def login_required(func):
  @wraps(func)
  # The keywords *args and **kwargs ensure that no matter how many 
  # arguments are given (if any), the wrapped_function() captures them all
  def wrapped_function(*args, **kwargs):
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)
    return redirect('/login')
  
  return wrapped_function