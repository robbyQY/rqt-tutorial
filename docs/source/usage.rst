Usage
=====

.. _installation:

Installation
------------

To use agile_autonomy, launch it in terminal:

.. code-block:: console

   $ source devel/setup.bash
   $ roslaunch agile_autonomy simulation.launch

key functions
----------------

To run inference and obtain trajectories, you can use ``PlannerBase.preprocess_depth()`` function:

.. autofunction:: PlannerBase.PlanBase.preprocess_depth

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

