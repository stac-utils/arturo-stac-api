"""query extension"""
from dataclasses import dataclass

from fastapi import FastAPI

from stac_api.api.extensions.extension import ApiExtension


@dataclass
class QueryExtension(ApiExtension):
    """
    stac-api query extension
    (https://github.com/radiantearth/stac-api-spec/tree/master/extensions/query)
    """

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        pass
