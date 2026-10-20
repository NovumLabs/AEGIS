import pytest

from aegis.exceptions import ToolExecutionError
from aegis.tools.mock_tools import MockTools


def test_configured_mock_fault_raises_domain_error():
    with pytest.raises(ToolExecutionError, match="Simulated failure"):
        MockTools(fail_tools={"unstable"}).invoke("unstable", {})
