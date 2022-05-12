import cesar as c
import vigenere as v
import autokey as a
import preprocessed as p

"""ejercicio 01"""
encrypted = c.cesar('file.txt',3)

"""ejercicio 05"""
des_ecrypted = c.cesar_descifrado(encrypted,3)

"""ejercicio 06"""
vigenere = v.vigenere('file.txt', 'mezclador',27)

"""Ejercicio 09"""
vigenere = v.vigenere('file.txt', 'maleficio',27)
dic = v.getFrecuencias(vigenere)

"""Ejercicio 10"""
text = "GYLKWQRVEBTPXDJRQDDVQNPHHGQGUWRNPPWHRGCONLJOHMÑCOXEEAVASIÑDOEQPETAPVHEOPEKRXYAEVRUHAÑVNRSIVPZBSXINLEWSMGBSHEEITVDEENSVR"
key="PEDRONAVAJA"
des_ecrypted = v.descifrador(text.lower(), key.lower(),27)

"""ejercicio 13"""
v ="XHGDQESDMPKÑDEEDKNGJZPFJSUIFZOLFCINFJCESVZTGBFXCIUDAYNUUDIZYWWZBEYNVQWIVUNKZEPHDODQUZZLBDNDRWTHQSERÑIVMLERCMGIFLSORZXTSDIGLOXQSDJHWVCIWQXQJCKMBPOKMPSKMUVIMNJDNBLCSZHXHNYYUIXDBSOXHZLXWVGDJGXHWLTDWKÑSAQIMZLNBVMLXHUOQQXIQGWGUFTWKZKMOKUDNINSIFJDUOZIJBSVVOWFAIEÑGYOWPSOAP"

k="UNODELOSMASGRANDESCRIPTOGRAFOS"
result = a.autokey(v.lower(),k.lower(),27)
