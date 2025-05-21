from functools import wraps
import time

def time_performance(_func=None, detail_name: str = ""):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            print(f'[INFO] [{detail_name or func.__name__}] Executado em {end - start:.2f} segundos')
            
            return result
        
        return wrapper

    if _func is None:
        return decorator
    
    return decorator(_func)

