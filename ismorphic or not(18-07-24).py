def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_st = {}
    mapping_ts = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if char_s in mapping_st:
            if mapping_st[char_s] != char_t:
                return False
        else:
            mapping_st[char_s] = char_t
        
        if char_t in mapping_ts:
            if mapping_ts[char_t] != char_s:
                return False
        else:
            mapping_ts[char_t] = char_s
    
    return True

s1 = "egg"
t1 = "add"
print(f"Are '{s1}' and '{t1}' isomorphic? {is_isomorphic(s1, t1)}")


