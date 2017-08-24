# !/usr/bin/env python

#
# Imports
#
try:
    import json
except ImportError:
    raise ImportError("Import failed to load in view.py.")


#
# Parse Data
#
def parse_data(data, dict_names, is_list):
    content = {}
    i = 0
    json_length = len(dict_names)
    if not is_list:
        while i < json_length:
            if dict_names[i] in data:
                content[dict_names[i]] = {}
                for key in data[dict_names[i]]:
                    content[dict_names[i]][key] = data[dict_names[i]][key]
            i += 1
    else:
        while i < json_length:
            if dict_names[i] in data:
                content[dict_names[i]] = {}
                x = 0
                list_length = len(data[dict_names[i]])
                while x < list_length:
                    content[dict_names[i]][x] = {}
                    for key in data[dict_names[i]][x]:
                        content[dict_names[i]][x][key] = data[dict_names[i]][x][key]
                    x += 1
            i += 1
    return content


#
# Print Title
#
def print_title(title, important):
    title_length = len(title)
    if important:
        print("\n\n" + "=" * title_length)
        print(title.upper())
        print("=" * title_length)
    else:
        print("\n")
        print(title.lower())
        print("-" * title_length)


#
# Print Data
#
def print_data(data, title):
    print_title(title, True)
    print(json.dumps(data, sort_keys = False, indent = 2))


#
# Print JSON
#
def print_dict(data, names, is_list):
    i = 0
    json_length = len(names)
    if not is_list:
        while i < json_length:
            if names[i] in data:
                print_title(names[i], False)
                for key, value in data[names[i]].items():
                    print(key, ":", value)
            i += 1
    else:
        while i < json_length:
            x = 0
            list_length = len(data[names[i]])
            while x < list_length:
                if names[i] in data:
                    print_title(names[i] + " " + str(x), False)
                    for key, value in data[names[i]][x].items():
                        print(key, ":", value)
                x += 1
            i += 1
