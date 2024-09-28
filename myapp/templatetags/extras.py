from django import template

register = template.Library()

@register.filter
def get_filename_from_url(url):
    """
    Toma una URL y devuelve el nombre del archivo.
    La URL debe tener el formato /photos/nombre_de_imagen.jpg
    """
    return url.split('/photos/')[-1]
