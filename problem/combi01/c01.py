from itertools import permutations
def test(s):
    return  s.find('A') < s.rfind('B') and \
            s.find('B') < s.rfind('C') and \
            s.find('C') < s.rfind('D')
perms = set(permutations("AAABBBCCDD"))
count = sum([1 for p in perms if test("".join(p))])
print(count)