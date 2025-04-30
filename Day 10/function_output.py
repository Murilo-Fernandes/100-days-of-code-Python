def formated_name(name, last_name):
    """Format the name and last name to be capitalized."""
    # formated_name = name.title()
    # formated_last_name = last_name.title()
    # return f"{formated_name} {formated_last_name}"
    return f"{name.title()} {last_name.title()}"

name = formated_name(input("Say your firstname: "), input("Say your lastname: ")) 
print(name)  # Output: John Doe