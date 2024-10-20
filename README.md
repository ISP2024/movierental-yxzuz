## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

### 2.1. what refactoring signs (code smells) suggest this refactoring?
Dead Code because Movie does not need price_code attribute, get_price_code since it is being used in rental instead.
### 2.2 what design principle suggests this refactoring? Why?
Single Responsibility Principle (SRP) because movie and price_code are not relating to each other, so there's no point to keep in movie.

