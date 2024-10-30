def list_op(a: [], b: []):
    intersec = []
    intersec = set(a) & set(b)
    union = set(a) | set(b)
    a_min_b = []
    a_min_b = set(a) - set(b)
    b_min_a = []
    b_min_a = set(b) - set(a)

    return (intersec, union, a_min_b, b_min_a)

def count_chars(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def comp_dict(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if len(dict1) != len(dict2):
            return False
        return all(comp_dict(dict1.get(key), dict2.get(key)) for key in dict1.keys())

    elif isinstance(dict1, list) and isinstance(dict2, list):
        if len(dict1) != len(dict2):
            return False
        return all(comp_dict(a, b) for a, b in zip(dict1, dict2))

    elif isinstance(dict1, set) and isinstance(dict2, set):
        if len(dict1) != len(dict2):
            return False
        return all(item in dict1 for item in dict2) and all(item in dict1 for item in dict2)

    else:
        return dict1 == dict2

def build_xml_element(tag, content, **attributes):
    attributes_str = ' '.join(f'{key}="{value.strip()}"' for key, value in attributes.items())
    if attributes_str:
        opening_tag = f"<{tag} {attributes_str}>"
    else:
        opening_tag = f"<{tag}>"
    closing_tag = f"</{tag}>"

    return f"{opening_tag}{content}{closing_tag}"

def dict_rules(rules, dict):
    for key, prefix, middle, suffix in rules:
        if key not in dict:
            return False
        value = dict[key]

        if not value.startswith(prefix):
            return False
        if middle not in value[1:-1]:
            return False
        if not value.endswith(suffix):
            return False

    for key in dict:
        if key not in {rule[0] for rule in rules}:
            return False
    return True

def unique_dup(list):
    unique_list = set(list)
    a = len(unique_list)
    b = len(list) - a

    return (a, b)

def set_ops(*sets):
    dict = {}
    #set_list = [set(set) for set in sets]
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set_a = sets[i]
            set_b = sets[j]

            op_res = list_op(set_a, set_b)
            dict[f"{set_a} & {set_b}"] = op_res[0]
            dict[f"{set_a} | {set_b}"] = op_res[1]
            dict[f"{set_a} - {set_b}"] = op_res[2]
            dict[f"{set_b} - {set_a}"] = op_res[3]

    return dict

def loop(map):
    visit = []
    current = "start"

    while current not in visit:
        visit.append(current)
        current = map[current]
    return visit

def my_function(*args, **key_args):
    count = 0
    for arg in args:
        if arg in key_args.values():
            count += 1
    return count
#------------------------------------------------

print("ex. 1")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(list_op(a, b))

print("ex. 2")
string = "Ana are apples."
print(count_chars(string))

print("ex. 3")
d1 = {'1': 1, '2': 2, '3': "misu", '4': ['a', 'b', 'c'], '5':{1, 2, 3}}
d2 = {'1': 1, '2': 2, '3': "misu", '4': ['a', 'b', 'c'], '5':{1, 2, 3}}
d3 = {'1': 1, '2': 2, '3': "!misu", '4': ['a', 'b', 'c'], '5':{1, 2, 3}}
print(comp_dict(d1, d2))
print(comp_dict(d1, d3))

print("ex. 4")
print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
print(build_xml_element ("a", "Hello there"))

print("ex. 5")
s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
print(dict_rules(s, d))

print("ex. 6")
print(unique_dup([1, 1, 2, 3, 4, 4, 5, 5, 5]))

print("ex. 7")
print(set_ops({1,2}, {2,3}))

print("ex. 8")
print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
)

print("ex. 9")
print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))