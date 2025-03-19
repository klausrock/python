"""
   
### TCP/UDP Payload Random Generator

"""

import random

def random_payload(n: int) -> [str]:
    payload=[]

    for i in range(n):             
        payload.append(chr(random.randrange(33,125))) 

    return payload

