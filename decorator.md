the things like __name__ , __doc__ , __module__ etc etc are the part of fuction build in metadata atritubte 
we use it like :
               ``` def my_logger(func):
                    def wrapper(*args, **kwargs):
                        print(f"Executing {func.__name__}")
                        return func(*args, **kwargs)

                    return wrapper


                @my_logger
                def add(a: int, b: int) -> int:
                    return a + b


                print(add.__name__)  # Output: 'wrapper' (Lost 'add')
                print(add.__doc__)  # Output: 'Wrapper function docstring.' (Lost original docstring)   ```

this is mostly correct accept their is some issue with it

{1.Broken Stack Traces & Profiling: Tracebacks, error logs, and performance profilers attribute exceptions and latency to wrapper instead of add, making debugging unclear in large codebases.
2.Framework Routing & Command Registration: Web frameworks (Flask, FastAPI) and CLI parsers (Click) inspect func.__name__ and parameter annotations to map routes or commands. Decorating multiple endpoints without preserving metadata leads to duplicate route errors or failed parameter parsing.
3.Documentation Generators: Tools like Sphinx parse __doc__ and type annotations to build developer documentation. Without preservation, documentation renders wrapper text instead of actual endpoint specs.
4.Introspection & IDE Support: help(add), inspect.signature(add), and IDE autocompletion fail to display correct signatures or tooltips.}

so we use 

```  from functools import wraps
        def my_logger(func):
            @wraps(func)  
            def wrapper(*args, **kwargs):
                print(f"Executing {func.__name__}")
                return func(*args, **kwargs)
            return wrapper


        @my_logger
        def add(a: int, b: int) -> int:
            return a + b


        print(add.__name__)  # Output: 'add'
        print(add.__doc__)  # Output: 'Adds two integers together.'
        print(add.__wrapped__)  # Output: <function add at 0x...>
 ```