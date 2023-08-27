
def decorator_apply(lambda_func):
    def actual_decorator(func):
        def wrapper(x):
            result = lambda_func(x)
            return func(result)
        return wrapper
    return actual_decorator
    pass


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num