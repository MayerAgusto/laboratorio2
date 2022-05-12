import preprocessed as p
abc = p.alphabeth

def autokey(text, key, mod):
  encripted = ""
  my_key = key
  for i in range(len(text)):
    c = abc.index(text[i]) - abc.index(my_key[i])
    c = c%27
    encripted += abc[c]
    my_key += abc[c]
  return encripted

