import preprocessed as p
abc = p.alphabeth
 
def cesar(filename, n):
  text = p.read_file(filename)
  char_index = [(abc.index(text[i]) + n%27)%27 for i in range(len(text))]
  return "".join([abc[i] for i in char_index ])

def cesar_descifrado(text, n):
  c = [abc[abc.index(t)-n%27] for t in text]
  return "".join(c)
