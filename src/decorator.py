import functools


def trace(f) -> callable:
    """

    :param f: decorated function
    :return: wrapper function
    >>> fn = lambda : print("hello")
    >>> lg = trace(fn)
    >>> type(lg)
    <class 'function'>
    >>> lg.__name__
    '<lambda>'
    """

    @functools.wraps(f)
    def tracer(*args, **kwargs) -> None:
        """
        tracer function for f
        :param args: args for the function f
        :param kwargs:kwargs for the function f
        :return:
        """
        print(f"Start - {f.__name__}")
        # print(s)   # for raise exception
        r = f(*args, **kwargs)
        print(f"End - {f.__name__}")
        return r

    return tracer


def exept(f) -> callable:
    """

    :param f: decorated function
    :return: wrapper function
    """

    @functools.wraps(f)
    def exceptor(*args, **kwargs) -> None:
        try:
            f(*args, **kwargs)
        except Exception as e:
            import traceback as tb
            code = e.__traceback__.tb_frame.f_code
            lineno = e.__traceback__.tb_lineno
            print(f"Caught Exception: {e} / {e.__doc__} at {code}:{lineno}")
        return

    return exceptor


@exept
@trace
def run(msg) -> str:
    """
    run function
    :rtype: None
    >>> run('message')
    Start - run
    run - message
    End - run
    'run - message'
    """
    s = f"run - {msg}"
    print(s)
    s += 3 / 0
    return s


def three() -> None:
    """
    three function for test the testdoc module
    :rtype: None
    >>> three()
    3
    """
    return 3


if __name__ == "__main__":
    run("hello")
