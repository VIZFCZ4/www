import random as _orig_random
from functools import wraps as _wraps
import sys as _sys

_IS_READY = False
def _init():
  global _IS_READY

  _orig_random.seed()
  _IS_READY = True

  # Put back original random module
  _sys.modules["random"] = _orig_random



def __getattr__(key):
  orig = getattr(_orig_random, key)
  if _IS_READY:
    return orig

  @_wraps(orig)
  def wrapper(*args, **kwargs):
    if not _IS_READY:
      raise RuntimeError(f"Cannot use random.{key}() outside of request context")

  return wrapper
