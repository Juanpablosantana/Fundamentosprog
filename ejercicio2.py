# decil = 10
# la Academia school of talent
 #requiere realizar una aplicacion en python que le permita establecer el rango socioeconomico de cada uno de sus estuadiante , para poder proporcionar los distintos beneficios economicos
#sabiendo que cada uno de los deciles establecidos cuenta con una diferencia de 10%
# decil n°1 beneficia al estrato mas bajo con calificaciones de 7 100%
# decil n°2 beneficia al estrato bajo con calificaciones de 7 40%
# decil n°3 beneficia al estrato mas medio con calificaciones de 7 30%
# decil n°4 beneficia al estrato mas bajo con calificaciones de 6  30%
# decil n°5 beneficia al estrato mas bajo con calificaciones de 6  25%
# decil n°6 beneficia al estrato mas bajo con calificaciones de 5  20%
# decil n°7 al 10 no beneficia al estrato alto

#precio del curso es de $300.000 por 6 meses

def decil_estrato(calificacion):
    if calificacion >= 7:
        return "Decil 1"
    elif calificacion >= 6.5:
        return "Decil 2"
    elif calificacion >= 6:
        return "Decil 3"
    elif calificacion >= 5.5:
        return "Decil 4"
    elif calificacion >= 5:
        return "Decil 5"
    elif calificacion >= 4.5:
        return "Decil 6"
    else:
        return "No aplica"
    
