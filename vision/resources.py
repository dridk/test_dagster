from dagster import (
    Definitions,
    load_assets_from_modules,
    ConfigurableIOManager,
    ConfigurableResource,
)


class StarrocksResource(ConfigurableResource):
    hostname: str = ""
    port: int = 234

    def sql(self, query: str):
        pass
