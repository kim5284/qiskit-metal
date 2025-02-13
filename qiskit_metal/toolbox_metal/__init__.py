## -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
=================================================
Toolbox_metal (:mod:`qiskit_metal.toolbox_metal`)
=================================================

.. currentmodule:: qiskit_metal.toolbox_metal

This folder contains code that is more specific to Metal.

Custom Exceptions
-----------------

.. autosummary::
    :toctree: ../stubs/

    QiskitMetalExceptions
    QiskitMetalDesignError


Submodules
---------------

.. autosummary::
    :toctree: ../stubs/

    about
    import_export
    math_and_overrides
    parsing

"""

from .parsing import parse_value
from .parsing import is_variable_name
from .parsing import is_numeric_possible

from .. import config
if config.is_building_docs():
    from . import about
    from .exceptions import QiskitMetalDesignError
    from .exceptions import QiskitMetalExceptions
    from . import import_export
    from . import parsing
    from . import math_and_overrides
