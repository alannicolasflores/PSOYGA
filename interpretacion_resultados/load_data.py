import os


def cargar_archivos(directorio):
    
    return [os.path.join(directorio, f) 
            for f in os.listdir(directorio) 
            if f.endswith('.xlsx')
            ]
    
