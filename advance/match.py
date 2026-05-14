def http(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found" 
        case 800:
            return "match successfully"
        case _:
            return "Unknown status"

print(http(200))