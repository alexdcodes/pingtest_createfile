# templates.py

import fileinput, re

# Matches fields enclosed in square brackets:
field_pat = re.compile(r'\[(.+?)\]')


# We'll collect variables in this:
scope = {}

# This is used in re.sub:


def replacement(match):
    code = match.group(1)
    try:
        # If the field can be evaluated, return it:
        return str(eval(code, scope))
    except SyntaxError:
        # Otherwise execute teha ssignment in the same scope....
        exec code in scope
        # ...and return an empty string:
        return ''

# Get all the text as a single string:
