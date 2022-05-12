import preprocessed as p
abc = p.alphabeth

def vigenere(filename, key, mod):
  text = p.read_file(filename)
  v = [key[i%len(key)] for i in range(len(text))]
  cifrado = [abc[(abc.index(text[i]) + abc.index(v[i]))%mod] for i in range(len(text))]
  return ''.join(cifrado)

def vigenereAscii(filename, key, mod):
  text = p.read_file(filename)
  v = [key[i%len(key)] for i in range(len(text))]
  cifrado = [chr((ord(text[i]) + ord(v[i]))%mod) for i in range(len(text))]
  return ''.join(cifrado)
  
def getFrecuencias(text):
  dic = dict()
  for t in text:
    if t in dic.keys():
      dic[t]+= 1
    else:
      dic[t]=1
  dic=sorted(dic.items(), key=lambda x: x[1], reverse=True)
  return dic

def descifrador(text, key, mod):
  v = [key[i%len(key)] for i in range(len(text))]
  cifrado = [abc[(abc.index(text[i])- abc.index(v[i]))%mod] for i in range(len(text))]
  return "".join(cifrado)
  
  