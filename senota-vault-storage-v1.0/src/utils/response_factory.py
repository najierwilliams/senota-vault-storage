def success(message:str,data:dict|None=None):
    return {"success":True,"message":message,"data":data or {}}

def error(message:str):
    return {"success":False,"message":message}
