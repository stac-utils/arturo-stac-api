"""sort extension"""
import attr
from fastapi import FastAPI

from stac_api.api.extensions.extension import ApiExtension


@attr.s
class SortExtension(ApiExtension):
    """
    stac-api sort extension
    (https://github.com/radiantearth/stac-api-spec/blob/master/fragments/sort/README.md)
    """

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        pass
