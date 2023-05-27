Sorting is often referred to as "ordering" in Django, and it can be achieved in several ways. For the Django Rest Framework (DRF), the `OrderingFilter` is used to handle dynamic ordering of results. The client can control the ordering of the results by including an `ordering` parameter in the URL.

Here's how you can add ordering to your viewsets or generic views:

```python
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class GameTypeViewSet(viewsets.ModelViewSet):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = GameTypeFilter
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']  # default ordering
```

In this example, `ordering_fields` specifies the fields by which you can order, and `ordering` specifies the default ordering.

If you want to use `OrderingFilter` as a default filter backend for all the views in the entire project, you can add `rest_framework.filters.OrderingFilter` to the `DEFAULT_FILTER_BACKENDS` in your Django settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}
```

Then, you can specify the `ordering_fields` attribute in your viewsets and views as shown above. This will apply default ordering on all views.

Clients can control the ordering of the results by including the `ordering` parameter in the URL. For example, you can order `GameType` objects by `created_at` in descending order by accessing this URL: `http://api.example.com/gametypes?ordering=-created_at`.

The `ordering` parameter can also take multiple fields: `http://api.example.com/gametypes?ordering=created_at,name`.

Remember, you have to include the fields on which you want to apply ordering in `ordering_fields` attribute, and the fields must also be included in the model.
