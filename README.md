## Solution ##

[Life.py](/gameoflife/Life.py) gains `setCell()` method for clearer iteration through 2D array in `evolve()`. Both `evolve()` and `setCell()` function correctly regardless of dimensions of array (whether square or not).

### Tests ###

It is assumed that Scenario 0 and 5 are identical in terms of input and expected output and as such, the predefined `test_no_interaction` test is assumed to be valid for both.

For the remainder of tests in [testlife.py][test]:

* `test_underpopulation` checks that for scenario 1, if a live cell has too _few_ live neighbouring cells it dies.
* `test_overcrowding` checks that for scenario 2, if a live cell has too _many_ live neighbouring cells it dies.
* `test_survival` checks that for scenario 3, if a live cell has 2 or 3 live neighbouring cells the cell survives (with [0,1],[1,0], and [2,2] having 2 neighbours and [1,2] and [2,1] having 3 neighbours).
* `test_creation` checks that for scenario 4, if an empty position has exactly 3 neighbouring cells a new live cell is created.
    * Note that `test_survival` checks that for 2 or 4 neighbouring live cells an empty cell doesn't create a live cell.
* `test_seeded_outcome` checks that for scenario 6, and with an array of a higher dimension (5x5), the example outcomes defined are correctly adhered to.
* `test_non_square` checks scenario 6 again, but with a [3x5] array.

### Assumptions ###

The most substantial assumption is that the evaluation of neighbouring cells is according to their intial value, and is not affected by evolutions that may precede the evaluation of a later cell.

Another assumption is that an array will be rectangular, i.e., there will be an equal number of cells in each row. It is also assumed that a live cell will only be defined as 1. The final assumption is that an output 2D array should retain the same dimensions as the input state array.

[test]: /tests/testlife.py
