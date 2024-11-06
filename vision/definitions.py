from dagster import (
    Definitions,
    load_assets_from_modules,
    ConfigurableIOManager,
    ConfigurableResource,
)

from . import assets  # noqa: TID252

from .resources import *


class S3IOManager(ConfigurableIOManager):
    bucket: str = "raw"

    def handle_output(self, context, obj):
        pass

    def load_input(self, context):
        pass


raw_s3 = S3IOManager(bucket="raw")
pii_s3 = S3IOManager(bucket="pii")
doc_s3 = S3IOManager(bucket="doc")

starrocks = StarrocksResource(hostname="localhost", port=4000)

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={"raw_s3": raw_s3, "pii_s3": pii_s3, "doc_s3": doc_s3, "starrocks": starrocks},
)
