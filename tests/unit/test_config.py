from aegis import __version__
from aegis.config import AegisConfig


def test_version_is_v010():
    assert __version__ == "0.1.0"


def test_config_defaults_are_bounded():
    assert AegisConfig().max_tool_calls > 0
