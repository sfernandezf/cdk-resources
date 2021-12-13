import inspect
import typing

from aws_cdk import core

from cdk_resources.utils import combine_configurations, app_context


__all__ = ["Resource", "ResourceType"]

ResourceType = typing.TypeVar("ResourceType")


class Resource(typing.Generic[ResourceType]):
    """ """

    # Construct attrs
    construct_class = None
    construct_props = None

    # Lookup
    construct_lookup_method = None
    construct_lookup_props = None

    def __new__(
        cls,
        scope: typing.Optional[core.Stack] = None,
        construct_id: typing.Optional[str] = None,
        force_lookup: bool = False,
        *args,
        **kwargs,
    ) -> ResourceType:
        if hasattr(cls, "construct") and force_lookup is False:
            return cls.construct
        scope = scope or app_context["current_stack"]
        assert isinstance(scope, core.Stack), "Scope is required"
        assert isinstance(construct_id, str), "construct_id is required"
        if force_lookup is True:
            return cls.lookup(scope, construct_id, *args, **kwargs)
        cls.construct = cls.create(scope, construct_id, *args, **kwargs)
        cls.post_create()
        return cls.construct

    @classmethod
    def render_props(cls, configurations: typing.Union[list, dict]) -> dict:
        def transform_value(value):
            if isinstance(value, tuple):
                return getattr(value[0].get(), value[1])
            if inspect.isclass(value) is True and issubclass(value, cls):
                return value()
            if hasattr(value, "__call__"):
                return value()
            if (
                isinstance(value, str)
                and hasattr(cls, value)
                and hasattr(getattr(cls, value), "__call__")
            ):
                return getattr(cls, value)()
            return value

        if isinstance(configurations, dict) or isinstance(configurations, list):
            list_values = (
                configurations.items()
                if isinstance(configurations, dict)
                else enumerate(configurations)
            )
            for key, value in list_values:
                if isinstance(value, dict) or isinstance(value, list):
                    cls.render_props(value)
                else:
                    configurations[key] = transform_value(value)
        return configurations

    # region Construct Create
    @classmethod
    def create(cls, scope: core.Stack, construct_id: str, *args, **kwargs) -> ResourceType:
        construct_class = cls.get_construct_class(*args, **kwargs)
        construct_props = cls.get_construct_props(*args, **kwargs)
        construct = construct_class(scope, construct_id, **construct_props)
        return construct

    @classmethod
    def get_construct_class(
        cls, *args, **kwargs
    ) -> typing.Type[core.Construct]:
        construct_class = cls.construct_class
        assert issubclass(
            construct_class, core.Construct
        ), "construct_class is required"
        return construct_class

    @classmethod
    def get_construct_props(cls, *args, **kwargs) -> dict:
        construct_props = cls.construct_props
        assert isinstance(construct_props, dict), "construct_props is required"
        construct_props = combine_configurations(construct_props)
        construct_props = cls.render_props(construct_props)
        return construct_props

    @classmethod
    def post_create(cls) -> None:
        pass

    # endregion

    # region Lookup
    @classmethod
    def lookup(cls, scope: core.Stack, construct_id: str, *args, **kwargs):
        construct_class = cls.get_construct_class(*args, **kwargs)
        construct_lookup_method = cls.get_construct_lookup_method(
            *args, **kwargs
        )
        construct_lookup_props = cls.get_construct_lookup_props(*args, **kwargs)
        construct = getattr(construct_class, construct_lookup_method)(
            scope, construct_id, **construct_lookup_props
        )
        return construct

    @classmethod
    def get_construct_lookup_method(
        cls, construct_class: core.Construct, *args, **kwargs
    ) -> str:
        construct_lookup_method = cls.construct_lookup_method
        assert isinstance(
            construct_lookup_method, str
        ), "construct_lookup_method is required"
        assert hasattr(construct_class, construct_lookup_method) and hasattr(
            getattr(construct_class, construct_lookup_method), "__call__"
        ), "Incorrect construct_lookup_method"
        return construct_lookup_method

    @classmethod
    def get_construct_lookup_props(cls, *args, **kwargs) -> dict:
        construct_lookup_props = cls.construct_lookup_props
        assert isinstance(
            construct_lookup_props, dict
        ), "construct_lookup_props is required"
        construct_lookup_props = combine_configurations(construct_lookup_props)
        construct_lookup_props = cls.render_props(construct_lookup_props)
        return construct_lookup_props

    # endregion
