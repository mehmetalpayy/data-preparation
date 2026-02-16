from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from dataclasses import field
from omegaconf import MISSING

from mehmet.config_schemas.data_processing import dataset_readers_schema
from mehmet.config_schemas.infrastructure import aws_schema


@dataclass
class DataProcessingConfig:
    version: str = MISSING
    data_local_save_dir: str = "./data/raw"
    dvc_remote_repo: str = "<github_repo_clone_link>"
    dvc_data_folder: str = "data/raw"
    github_user_name: str = "mehmetalpayy"
    github_access_token_secret_name: str = "example_secret_name"

    infrastructure: aws_schema.AWSConfig = field(default_factory=aws_schema.AWSConfig)

    dataset_reader_manager: dataset_readers_schema.DatasetReaderManagerConfig = MISSING


def setup_config() -> None:
    aws_schema.setup_config()
    dataset_readers_schema.setup_config()
    cs = ConfigStore.instance()
    cs.store(name="data_processing_config_schema", node=DataProcessingConfig)
