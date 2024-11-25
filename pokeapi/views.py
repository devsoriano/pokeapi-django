from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .jobs import fetch_pokemon_data
from .models import Pokemon

@csrf_exempt  # Permite solicitudes sin token CSRF (para Postman)
def run_job(request):
    if request.method == 'POST':
        try:
            fetch_pokemon_data()  # Ejecutar el JOB
            return JsonResponse({'message': 'El JOB se ejecutó correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa POST.'}, status=405)

def get_pokemons(request):
    if request.method == 'GET':
        try:
            # Obtener todos los registros de Pokémon
            pokemons = Pokemon.objects.all().values(
                'name', 'types', 'weight', 'abilities', 'image_front', 'image_back'
            )

            # Parámetro de la página (por defecto es 1)
            page = int(request.GET.get('page', 1))

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

            return JsonResponse(response, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)
