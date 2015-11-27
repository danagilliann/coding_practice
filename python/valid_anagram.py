def valid_anagram(s,t):
        s_dict = {}
        t_dict = {}
        if (len(s) != len(t)):
                return False
        for i in s:
                if (i in s_dict.keys()):
                        s_dict[i] += 1
                else:
                        s_dict[i] = 1
        for x in t:
                if (x in t_dict.keys()):
                        t_dict[x] += 1
                else:
                        t_dict[x] = 1
        for tk in t_dict.keys():
                if (tk not in s_dict.keys()):
                        return False
                elif (t_dict.get(tk) != s_dict.get(tk)):
                        return False
        return True

def valid_anagram_unicode(s,t):
        s = s.split("\u")
        t = t.split("\u")
        s_dict = {}
        t_dict = {}

        if (len(s) != len(t)):
                return False

        for i in s:
                if (i in s_dict.keys()):
                        s_dict[i] += 1
                else:
                        s_dict[i] = 1

        for x in t:
                if (x in t_dict.keys()):
                        t_dict[x] += 1
                else:
                        t_dict[x] = 1

        for tk in t_dict.keys():
                if (tk not in s_dict.keys()):
                        return False
                elif (t_dict.get(tk) != s_dict.get(tk)):
                        return False

        return True

print valid_anagram_unicode("\u0420\u043e\u0441\u0441\u0438\u044f","\u0441\u0441\u0438\u044f\u0420\u043e")
