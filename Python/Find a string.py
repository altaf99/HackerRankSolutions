import re
def count_substring(string, sub_string):
    q='(?=%s)'%(sub_string)
    return len(re.findall(q, string))