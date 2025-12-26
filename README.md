# ds-hw4-column-optimization-
Block Diameter Optimization

This project addresses the problem of finding the maximum achievable diameter using a set of rectangular blocks.

Each block can be used individually, or two blocks with identical base dimensions can be stacked together. The goal is to select the configuration that produces the largest possible diameter.

Problem Description

For each block, three dimensions are given. The dimensions are sorted in descending order so that:

The largest dimension is considered the height.

The remaining two dimensions define the base.

The diameter of:

a single block is equal to its height.

two stacked blocks is the minimum of the base width and the sum of their heights.

Solution Approach

Evaluate all blocks individually to determine the best single-block diameter.

Group blocks that have the same base dimensions.

For each group, choose the two blocks with the greatest heights.

Compute the diameter obtained by stacking these two blocks.

Compare all results and keep the maximum value.

Input

The input consists of:

An integer representing the number of blocks.

A sequence of blocks, each described by three integer dimensions.

Output

The output contains:

The number of blocks used in the optimal solution.

The indices of the selected block(s).

The maximum achievable diameter.

Key Features

Efficient grouping based on block base dimensions.

Supports both single-block and two-block solutions.

Deterministic and clear output.

Implementation Notes

Implemented in Python.

Uses file-based input and output.

Suitable for algorithmic and competitive programming tasks