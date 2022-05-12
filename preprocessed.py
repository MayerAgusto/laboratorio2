alphabeth = 'abcdefghijklmnñopqrstuvwxyz'

def eliminar_tildes(texto):
  tildes = dict(zip("áÁéÉíÍóÓúÚ","aAeEiIoOuU"))
  poema = [t if t not in tildes.keys() else tildes[t] for t in texto]
  return ''.join(poema)

def eliminar_signos(texto):
  signos =" .,;:¡!¿?()[]\"\'_/*¨"
  poema =  [ t for t in texto if t not in signos]
  return "".join(poema)
  
def read_file(name_file):
  file = open(name_file, 'r')
  text = file.readlines()
  file.close()
  pre_text = [t.replace('\n'," ") for t in text]
  str_pre_text = "".join(pre_text)
  str_pre_text = eliminar_signos(str_pre_text)
  str_pre_text = eliminar_tildes(str_pre_text)
  return str_pre_text.lower()