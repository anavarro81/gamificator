# YOUTUBE_VIEW   = "¿Has visto algún video de Youtbe?"
# film_view = "¿Has visto alguna película?"
# chapter_view = "¿Has visto algún capítulo?"


acumular_puntos()

from constants import *

def comprar_registro(): 
    f = open("puntos.txt", "r")

    

resp_yoututbe  = input (YOUTUBE_VIEW)
resp_film      = input (film_view)
resp_character = input (chapter_view)

print (f'Youtube {resp_yoututbe}, film {resp_film}, series {resp_character}')




