from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache  # Importa la funcionalidad de caché
from .jobs import fetch_pokemon_data
from .models import Pokemon, Ability  # Importa el modelo Ability
from django.core.paginator import Paginator


@csrf_exempt
def run_job(request):
    if request.method == 'POST':
        try:
            fetch_pokemon_data()
            cache.clear()
            return JsonResponse({'message': 'El JOB se ejecutó correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa POST.'}, status=405)


def get_pokemons(request):
    if request.method == 'GET':
        try:
            page = int(request.GET.get('page', 1))
            cache_key = f'pokemons_page_{page}'
            response = cache.get(cache_key)
            if response:
                return JsonResponse(response, status=200)
            pokemons = Pokemon.objects.all().values(
                'name', 'types', 'weight', 'abilities', 'image_front', 'image_back'
            )
            paginator = Paginator(pokemons, 20)
            data = paginator.get_page(page)
            response = {
                'current_page': data.number,
                'total_pages': paginator.num_pages,
                'total_items': paginator.count,
                'has_next': data.has_next(),
                'has_previous': data.has_previous(),
                'results': list(data),
            }
            cache.set(cache_key, response, timeout=1800)
            return JsonResponse(response, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)


def get_abilities(request):
    if request.method == 'GET':
        try:
            abilities = Ability.objects.all().values('name', 'description', 'short_effect')
            response = {'abilities': list(abilities)}
            return JsonResponse(response, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)
