from pydantic.dataclasses import dataclass
from hydra.core.config_store import ConfigStore

@dataclass
class AWSConfig:
    region_name: str = "eu-central-1"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="aws_config_schema", node=AWSConfig)