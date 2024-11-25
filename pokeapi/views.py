from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
        # Obtener todos los registros de la tabla `Pokemon`
        pokemons = Pokemon.objects.all().values(
            'name', 'types', 'weight', 'abilities', 'image_front', 'image_back'
        )
        # Devolver la información en formato JSON
        return JsonResponse(list(pokemons), safe=False)
    return JsonResponse({'error': 'Método no permitido. Usa GET.'}, status=405)
