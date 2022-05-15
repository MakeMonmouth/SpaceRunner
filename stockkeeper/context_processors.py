from .models import ComponentType

def component_types(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    component_types = []
    for component in ComponentType.objects.order_by('name'):
        component_types.append(
                {"name": component.name,
                 "description": component.description,
                 "id": component.id})

    return {"component_types": component_types}
