import re
def valid_email(s):
    try:
        if not  re.search('^[a-z0-9]+[@][a-z.]+[a-z]{2,3}$',s):
            raise Exception
    except Exception:
        print("Email is not valid")
    else:
         print("Email is valid")
