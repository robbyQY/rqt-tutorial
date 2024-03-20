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

To run inference and obtain trajectories, you can use ``PlannerBase._generate_plan()`` function:

.. autofunction:: PlannerBase.PlanBase._generate_plan

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

