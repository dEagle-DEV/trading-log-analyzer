
def parse_dollar_value(value: str) -> float:
    value = value.replace('$', '').replace(',', '')
    if value.startswith('(') and value.endswith(')'):
        value = '-' + value[1:-1]  # remove parentheses and prepend minus
    return float(value)