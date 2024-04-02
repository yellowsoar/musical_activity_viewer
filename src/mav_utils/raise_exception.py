def raise_exception_if_not_truth(
    input_variable,
    exception_message: str,
):
    """Raise exception if not passing truth value testing

    Parameters
    ----------
    input_variable : TYPE
        The variable for truth value testing
    exception_message : TYPE
        The return message if not passing the truth value testing
    """
    if not input_variable:
        raise Exception(exception_message)
