"""Compatibility alias for the jupyter-kernel-gateway distribution.

The PyPI package is named ``jupyter-kernel-gateway``, but modern installs expose
the importable package as ``kernel_gateway``. Some dependencies still import the
old ``jupyter_kernel_gateway`` name only to verify that the gateway package is
installed.
"""

from kernel_gateway import *  # noqa: F401,F403

