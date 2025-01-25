

def sanitizedEval(math_string: str) -> float:
    """Returns the given string evaluated. Only evaluates math expressions and ignores every other character."""
    sanitized_string = "" 
    valid_chars = "123456789+-/*^()"
    for char in math_string:
        if (char in valid_chars):
            sanitized_string += char

    result = eval(sanitized_string)
    return result