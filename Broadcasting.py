'''
Broadcasting
A way in which NumPy handles operations between arrays of different
shapes without requiring to manually reshape/ copy data.

A smaller array can thus be used with a larger one by "stretching"
it LOGICALLY so the shapes match, practically NumPy only duplicates
data in memory, the same values are used during computation.

A matrix X 
a vector b that applies to cols
A vector w that applies to rows

When adding b to X, Numpy treats b as if it repeats across every row
Each row in X gets the same column wise bias added.

When multiplying with w, each row of the result needs to be scaled 
to a different value., by viewing w as a column instead of a row, NumPy understands each value in w belongs to a row and it applies the value across the whole row.
'''
