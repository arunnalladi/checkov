from typing import Optional, Any, Dict
from collections.abc import Sized
from checkov.common.util.type_forcers import force_int
from .length_less_than_attribute_solver import LengthLessThanAttributeSolver
from checkov.common.graph.checks_infra.enums import Operators


class LengthGreaterThanOrEqualAttributeSolver(LengthLessThanAttributeSolver):
    operator = Operators.LENGTH_GREATER_THAN_OR_EQUAL  # noqa: CCE003  # a static attribute

    def _get_operation(self, vertex: Dict[str, Any], attribute: Optional[str]) -> bool:
        attr = vertex.get(attribute)  # type:ignore[arg-type]  # due to attribute can be None
        if attr is None:
            return False

        value_int = force_int(self.value)

        if value_int is None:
            return False
        if isinstance(attr, Sized):
            # this resolver assumes the attribute is a string or a list.
            # if a dict is received, default the length to 1.
            if isinstance(attr, dict):
                return 1 >= value_int
            return len(attr) >= value_int

        return False
