def display(num):
    message=""
    if num % 3==0:
        message="Zip"
    elif num % 5==0:
        message="Zap"
    else :
        message="Invalid"
    if num%3==0 and num% 5 ==0 :
        message="Zoom"
    
    return message

message=display(9)
print(message)