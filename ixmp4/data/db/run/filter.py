from ixmp4.db import filters
from ixmp4.data.db import filters as base


class RunFilter(base.RunFilter, metaclass=filters.FilterMeta):
    def join(self, exc, **kwargs):
        return exc
