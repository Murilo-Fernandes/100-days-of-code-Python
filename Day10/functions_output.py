def format_name(f_name, l_name):
    formated_f_name = f_name.capitalize()
    formated_l_name = l_name.capitalize()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("CassANDRa", "cain")
print(format_name(f"BrUCE", "waynE"))
print(formated_string)