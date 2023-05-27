You can use these filters in viewsets and generic views using the `filterset_class` attribute. Here is how you can apply filters to your `ViewSet` or generic view:

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import GameType, Game, GameRate, UserBid, GameResult, BidGameResultMapping
from .filters import (GameTypeFilter, GameFilter, GameRateFilter, 
                      UserBidFilter, GameResultFilter, BidGameResultMappingFilter)
from .serializers import (GameTypeSerializer, GameSerializer, 
                          GameRateSerializer, UserBidSerializer,
                          GameResultSerializer, BidGameResultMappingSerializer)


class GameTypeViewSet(viewsets.ModelViewSet):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GameTypeFilter


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GameFilter

# Similar for other ViewSets
```

For applying a filter on a generic view:

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import GameType
from .filters import GameTypeFilter
from .serializers import GameTypeSerializer


class GameTypeList(generics.ListAPIView):
    queryset = GameType.objects.all()
    serializer_class = GameTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GameTypeFilter
```

To use these filters as default for the entire Django project, you will have to modify your settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

Now, `DjangoFilterBackend` will be used as the default filter backend for the entire Django project.

However, for each ViewSet or generic view, you will still need to specify `filterset_class` in order to specify which filterset to use for that specific ViewSet or view. The `filterset_class` attribute tells Django which filter class should be used for the corresponding view. Without this attribute, Django wouldn't know which filters to apply.
