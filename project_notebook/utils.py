def enforce_types(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        print(annotations)
        all_args = {**dict(zip(func.__code__.co_varnames, args)), **kwargs}
        print(all_args)
        print(all_args.items())
        # Check types
        for arg_name, arg_value in all_args.items():
            if arg_name in annotations:
                expected_type = annotations[arg_name]
                if not isinstance(arg_value, expected_type):
                    raise TypeError(
                        f"Argument '{arg_name}' must be of type {expected_type}"
                    )
        return func(*args, **kwargs)

    return wrapper
