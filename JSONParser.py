class JSONParser:
    def __init__(self, data):
        self.data = data
        
    def pretty_print(self, mult=4, space_between_lines=0):
        def parse(data, key, level, mult):
            if not data:
                return
            if type(data)==str or type(data)==int:
                if key:
                    print(level*mult*" ", str(key) + ":", data)
                else:
                    print(level*mult*" ", data)
                if space_between_lines!=0:
                    print("\n"*(space_between_lines-1))
            elif type(data)==list:
                if key:
                    print(level*mult*" ", key + ":")
                for item in data:
                    if type(item)==dict:
                        parse(item, None, level, mult)
                    else:
                        parse(item, None, level + 1, mult)
            elif type(data)==dict:
                if key:
                    print(level*mult*" ", key + ":")
                for element in data:
                    parse(data[element], element, level + 1, mult)
        parse(self.data, None, -1, mult)








def parse_json(d, k, search_key=None, search_value=None, mult=4, op=None):
    
    printing = [not(search_key or search_value)]
    printlevel = [0]
    searching = bool(search_key or search_value)
    res = 0
    agg = []
    op_dict = {"agg": agg, "add": res}
    def parse(data, key, level, is_searching=False, search_for_key=None, search_for_value=None, operation=None):
        if (is_searching and data==search_for_value) or (is_searching and key==search_for_key):
            if operation:
                print(search_for_value)
                if (type(op_dict[operation])==int or type(op_dict[operation])==float):
                    op_dict[operation] += float(data)
                else:
                    op_dict[operation].append(data)
            printing[0]=True
            printlevel[0] = level

        if type(data)==str or type(data)==int:
            if key and printing[0]:
                print(level*mult*" ", key, data)
            elif not key and printing[0]:
                print(level*mult*" ", data)
            return

        elif type(data)==list:
            if printing[0]:
                print(level*mult*" ", key, "(list)")
            for item in data:
                parse(item, None, level + 1, is_searching, search_for_key, search_for_value, operation)

        elif type(data)==dict:
            if printing[0]:
                print(level*mult*" ", key, "(object)")
            for el in data:
                parse(data[el], el, level + 1, is_searching, search_for_key, search_for_value, operation)
            if is_searching and printlevel[0]-1 == level:
                printing[0] = False
    
    parse(d, k, 0, searching, search_for_key=search_key, search_for_value=search_value, operation=op)
    if op:
        return op_dict[op]
