# pydantic_fix.py
import pydantic
import typing

# Patch ForwardRef._evaluate for Python 3.12 compatibility
if not hasattr(pydantic.typing.ForwardRef, "_evaluate_orig"):
    pydantic.typing.ForwardRef._evaluate_orig = pydantic.typing.ForwardRef._evaluate

    def _evaluate_patch(self, globalns=None, localns=None, recursive_guard=None):
        return self._evaluate_orig(globalns=globalns, localns=localns, recursive_guard=recursive_guard or set())

    pydantic.typing.ForwardRef._evaluate = _evaluate_patch
