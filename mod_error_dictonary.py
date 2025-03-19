# Module mod_error_dictonary.py
#
# Dipl.-Ing.(FH) Klaus Rock
# Aalen Germany
# 11.09.2023

error_no = {
    "0": "No Error",
    "1000": "Error reading http_quss_client.json File!",
}

# Print Error Number and Message

def print_error_message(str_error_no):
    print('Error No:',str_error_no,'->',error_no[str_error_no])
    