from dagster import asset, AssetKey
from .resources import StarrocksResource

# LE GROUP_NAME est automatiquement crée depuis le dossier ou se trouve l'asset


@asset(group_name="glims", name="results", key_prefix=["glims"], io_manager_key="raw_s3")
def create_glims_result():

    return 4


@asset(group_name="glims", name="atb", key_prefix=["glims"], io_manager_key="raw_s3")
def create_glims_result():

    return 4


# Test doublons asset name
@asset(group_name="xway", name="results", key_prefix=["xway"], io_manager_key="raw_s3")
def create_xway_result():

    return 4


# Creation cora dans different bucket
@asset(
    group_name="cora",
    name="diag",
    key_prefix=["cora"],
    io_manager_key="raw_s3",
    description="bucket raw",
)
def create_cora_diag():
    return 5


@asset(group_name="cora", name="actes", key_prefix=["cora"], io_manager_key="raw_s3")
def create_cora_actes():
    return 5


@asset(
    group_name="cora",
    name="raw_doc",
    key_prefix=["cora"],
    io_manager_key="doc_s3",
    description="bucket doc",
    kinds=["secure"],
)
def create_cora_rawdoc():
    return 5


# Creation de l'asset clean doc
@asset(
    group_name="cora",
    name="doc",
    key_prefix=["cora"],
    io_manager_key="doc_s3",
    description="bucket doc",
    deps=AssetKey(["cora", "raw_doc"]),
)
def create_cora_doc():
    return 5


# Table starrocks OMOP
@asset(
    group_name="omop",
    name="dag",
    key_prefix=["omop"],
    deps=AssetKey(["cora", "diag"]),
    kinds=["mysql"],
)
def create_starrocks_docs(starrocks: StarrocksResource):
    starrocks.sql("CREATE TABLE")


@asset(group_name="omop", name="patients", key_prefix=["omop"], deps=["gam"], kinds=["mysql"])
def create_starrocks_patient(starrocks: StarrocksResource):
    starrocks.sql("CREATE TABLE")


@asset(
    group_name="omop",
    name="doc",
    key_prefix=["omop"],
    deps=AssetKey(["cora", "doc"]),
    kinds=["mysql"],
)
def create_starrocks_diag(starrocks: StarrocksResource):
    starrocks.sql("CREATE TABLE")


# Creation de datamart


# Creation d'un asset verge dependant de rien ! Genre le outlier
@asset(group_name="datamart", name="radioprotection", key_prefix=["datamart"], kinds=["oracle"])
def create_radio_protection(starrocks: StarrocksResource):
    # Je fais une sauvegarde dans le starrocks directement depuis oracle
    starrocks.sql("CREATE TABLE")


@asset(group_name="datamart", name="basile_test", key_prefix=["datamart"], kinds=["oracle"])
def create_basile_test(starrocks: StarrocksResource):
    # Je fais une sauvegarde dans le starrocks directement depuis oracle
    starrocks.sql("CREATE TABLE")
