def filter_data(data, **rules):
    result=[]
    
    for x in data:
        ok= True
        if "gt" in rules and not (x> rules["gt"]):
            ok=False
        if "lt" in rules and not (x<rules["lt"]):
            ok=False
        if "eq" in rules and not (x==rules["eq"]):
            ok=False
        if "divisible_by" in rules and not (x% rules["divisible_by"]==0):
            ok=False
        if ok:
            result.append(x)
        
    return result
print(filter_data([1, 5, 6, 9, 10], gt=5, divisible_by=5))
