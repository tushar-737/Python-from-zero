def http_status(status):
    match status:
        case 100:
            return "Error"
        case 200:
            return "OK"
        case _:
            return "Unknown Error"
print(http_status(100))
print(http_status(3563))            

        
