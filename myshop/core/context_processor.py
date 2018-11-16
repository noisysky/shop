from core.models import TelescopeType


def telescope_types(request):
    return {'telescope_types': TelescopeType.objects.all()}