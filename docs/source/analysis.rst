Analysis Tools
==============

Generalized 3-D Particle Distribution Tools
--------------------------------------------

The tools documented in this section are not intended to be called
directly by PySPEDAS users; rather, they are provided as building blocks
for mission-specific 3-D particle distribution tools.  Mission-specific wrappers
will generally be needed to load the particle data to be operated on,
perform any calibration, sanitization, or other preliminary steps, then
populate the data structures used by the general-purpose particle tools.

For documentation of mission-specific particle tools, see the "Mission Specific Tools" page.

Plasma Moments
--------------

This group of routines calculates plasma moments (density, velocity, fluxes, pressure tensors, etc.) from
3-D particle distributions (with two dimensions being azimuthal and elevation angles, and the third dimension
representing energy bins).

moments_3d
^^^^^^^^^^

This routine takes a data structure containing the particle distribution function,
and other information like angle and energy bin definitions and sizes, and returns
a dictionary containing plasma moments generated from the particle distributions.

.. autofunction:: pyspedas.moments_3d

spd_pgs_moments
^^^^^^^^^^^^^^^

Basically a wrapper around moments_3d

.. autofunction:: pyspedas.spd_pgs_moments

spd_pgs_moments_tplot
^^^^^^^^^^^^^^^^^^^^^^^^

Converts a dictionary (as returned by moments_3d) to tplot variables

.. autofunction:: pyspedas.spd_pgs_moments_tplot


Other quantities derived from 3-D particle distributions
---------------------------------------------------------

spd_pgs_do_fac
^^^^^^^^^^^^^^

.. autofunction:: pyspedas.particles.spd_part_products.spd_pgs_do_fac.spd_pgs_do_fac

spd_pgs_regrid
^^^^^^^^^^^^^^

.. autofunction:: pyspedas.particles.spd_part_products.spd_pgs_regrid

Slices of 3-D particle distributions
----------------------------------------

This set of routines creates 1-D and 2-D slices through 3-D particle distributions.

slice1d_plot
^^^^^^^^^^^^

This routine plots the values along the x or y axis of a 2-D slice.

.. autofunction:: pyspedas.slice1d_plot

slice2d
^^^^^^^

.. autofunction:: pyspedas.slice2d

slice2d_plot
^^^^^^^^^^^^

.. autofunction:: pyspedas.slice2d_plot



Magnetic Null Finding
---------------------

For missions such as MMS or Cluster, with at least four spacecraft in a relatively close tetrahedron-like configuration,
measuring the magnetic field simultaneously at four distinct locations allows the calculation of
field gradients in each field component along the X, Y, and Z directions (in other words, a Jacobian matrix).
This information is sufficient to find the location of magnetic null points (where all three field components
are zero), and infer the topology of the magnetic field at the null point.

.. autofunction:: pyspedas.find_magnetic_nulls_fote

.. autofunction:: pyspedas.classify_null_type

.. autofunction:: pyspedas.lingradest
