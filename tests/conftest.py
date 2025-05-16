# https://www.inspiredpython.com/article/five-advanced-pytest-fixture-patterns

import json
import os
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import cast

import pytest
from azure import functions as func
from pytest_socket import disable_socket

FUNCTION_SCOPE = 'function'


@pytest.fixture(autouse=True, scope='session')
def block_networs() -> None:
    """
    Fixture that blocks network usage.
    Enabled by default with autouse, but you  can disable and use @pytest.mark.usefixtures("block_networks")
    """
    disable_socket()


@pytest.fixture(scope='module')
def func_call(request: pytest.FixtureRequest) -> Callable:
    """
    Get the function call from the blueprint in the current modele.

    You should import the function as:
        from functions.myfunction_module import myfunction as trigger_function  # noqa F401
    """
    return cast(Callable, request.module.trigger_function.build().get_user_function())


@pytest.fixture(scope='module')
def make_req(request: pytest.FixtureRequest) -> Callable:
    """
    Factory builder for HttpRequest, it returns a contructor.
    It automatically picks up the function from the test module.

    You should import the function as:
        from functions.myfunction_module import myfunction as trigger_function  # noqa F401
    """

    def wrapper(
        body: bytes | None = b'',
        params: Mapping[str, str] = {'code': '<somecode>'},
        method: str = 'get',
    ) -> func.HttpRequest:
        return func.HttpRequest(
            method=method,
            body=body,
            url=request.module.trigger_function._function._trigger.route,
            params=params,
        )

    return wrapper


@pytest.fixture(scope='session', autouse=True)
def local_settings_environ_setup() -> None:
    """
    Fixture that automatically adds the local.settings.json to the environment
    """
    settings = json.loads((Path(__file__).parent.parent / 'local.settings.json').read_text())
    for key, setting_value in settings['Values'].items():
        os.environ[key] = setting_value
