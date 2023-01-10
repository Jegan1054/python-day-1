def isIso(s,t):
  if len(s)!=len(t):
        return False
  for i in range(len(s)): 
    count=0
    if s.count(s[i])!=t.count(t[i]):
       return False
  return True
print(isIso("egg","add"))
print(isIso("foo","bar"))
print(isIso("paper","title"))
print(isIso("fry","sky"))
print(isIso("apples","apple"))
    
