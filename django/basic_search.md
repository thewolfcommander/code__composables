The Django Rest Framework includes a SearchFilter backend that you can enable for your viewsets or generic views. When you include this backend, it adds a `search` parameter to your API that you can use to search your data.

First, add `SearchFilter` to your `filter_backends` attribute:

```python
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class GameTypeViewSet(viewsets.ModelViewSet):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = GameTypeFilter
    search_fields = ['name']  # Update this with the fields you want to search
```

Now, you can search GameTypes by their name by appending `?search=<your_search_term>` to the API endpoint in your browser or HTTP client. 

You can also perform complex queries using various options:

- `^` Starts-with search.
- `=` Exact matches.
- `@` Full-text search. (Currently only supported Django's PostgreSQL backend.)
- `$` Regex search.

To use these, modify the `search_fields` attribute like this:

```python
search_fields = ['=name', '^open_time']
```

Here, 'name' field is an exact match and 'open_time' is a starts-with search.

For a Generic API view, you can use the same `filter_backends` and `search_fields`:

```python
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class GameTypeList(generics.ListAPIView):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = GameTypeFilter
    search_fields = ['name']
```

Remember to add the fields on which you want to apply the search in `search_fields` attribute. In this case, it is the 'name' field.

If you want to use search as a default filter backend for all the views in the entire project, you can add `rest_framework.filters.SearchFilter` to the `DEFAULT_FILTER_BACKENDS` in settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    ]
}
```

Then, you can specify the `search_fields` attribute in your viewsets and views as shown above.
