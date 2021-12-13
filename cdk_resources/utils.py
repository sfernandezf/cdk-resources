import os
import typing


# Constants
ALLOWED_ENVIRONMENTS = os.environ.get("ALLOWED_ENVIRONMENTS", [])
COMMON_ENVIRONMENT_KEY = os.environ.get("COMMON_ENVIRONMENT_KEY", "default")
ENVIRONMENT_CONTEXT_KEY = os.environ.get(
    "ENVIRONMENT_CONTEXT_KEY", "environment"
)

# Shared var
app_context = {}


def combine_configurations(
    config: typing.Any,
    key: typing.Optional[str] = None,
    exclude_keys: typing.Optional[list] = None,
) -> typing.Any:
    exclude_keys = exclude_keys or []

    def filter_config(conf: dict) -> dict:
        filtered_config = {
            k: v for k, v in conf.items() if k not in exclude_keys
        }
        return filtered_config if key is None else filtered_config.get(key, {})

    if isinstance(config, dict) is False:
        return config

    # Environments
    environment = app_context["environment"]
    if environment is None:
        # Not environment app
        return filter_config(config.get(COMMON_ENVIRONMENT_KEY, config))

    environments = ALLOWED_ENVIRONMENTS + [COMMON_ENVIRONMENT_KEY]
    env_config = {k: v for k, v in config.items() if k in environments}
    if len(env_config) == 0:
        # Not environment app
        return filter_config(config)

    combined_config = dict(
        env_config.get(COMMON_ENVIRONMENT_KEY, {}),
        **config.get(environment, {}),
    )
    return filter_config(combined_config)


def get_context_variable(key: str) -> typing.Any:
    context_variable = app_context["app"].node.try_get_context(key)
    context_variable = combine_configurations(context_variable)
    return context_variable