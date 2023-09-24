import pytest

@pytest.fixture(scope="module", autouse=True)
def init(module_mocker):
    # PURGE ENVIRONMENT FOR TEST
    env_default = {
        "POWERTOOLS_SERVICE_NAME": "POWERTOOLS_SERVICE_NAME",
        "POWER_TOOLS_LOG_LEVEL": "DEBUG",
    }
    module_mocker.patch.dict("os.environ", env_default, clear=True)
