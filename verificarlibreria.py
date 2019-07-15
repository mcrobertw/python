try:
     import urllib.request  as urllib2 
except ImportError:
    # Que hacer si el módulo no se puede importar
    print("Módulo no instalado")