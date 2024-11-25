from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.cache import cache  # Importa la funcionalidad de caché
from .jobs import fetch_pokemon_data
from .models import Pokemon

@csrf_exempt  # Permite solicitudes sin token CSRF (para Postman)
def run_job(request):
    if request.method == 'POST':
        try:
            fetch_pokemon_data()  # Ejecutar el JOB
            cache.clear()  # Limpia la caché al actualizar los datos
            return JsonResponse({'message': 'El JOB se ejecutó correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa POST.'}, status=405)

def get_pokemons(request):
    if request.method == 'GET':
        try:
            # Parámetro de la página (por defecto es 1)
            page = int(request.GET.get('page', 1))

            # Crear una clave única para la caché basada en la página
            cache_key = f'pokemons_page_{page}'

            # Verificar si la respuesta está en la caché
            response = cache.get(cache_key)
            if response:
                return JsonResponse(response, status=200)  # Devuelve los datos cacheados

            # Si no está en caché, realiza la consulta
            pokemons = Pokemon.objects.all().values(
                'name', 'types', 'weight', 'abilities', 'image_front', 'image_back'
            )

            # Crear paginador con 20 elementos por página
            paginator = Paginator(pokemons, 20)

            # Obtener los datos de la página solicitada
            data = paginator.get_page(page)

            # Formato de respuesta
            response = {
                'current_page': data.number,  # Página actual
                'total_pages': paginator.num_pages,  # Total de páginas
                'total_items': paginator.count,  # Total de elementos
                'has_next': data.has_next(),  # Si hay una página siguiente
                'has_previous': data.has_previous(),  # Si hay una página previa
                'results': list(data),  # Resultados en esta página
            }

            # Cachear la respuesta con un timeout de 30 minutos (1800 segundos)
            cache.set(cache_key, response, timeout=1800)

            return JsonResponse(response, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)
