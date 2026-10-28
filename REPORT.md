# Assignment 3 Report

This document summarises the design and reasoning behind each task.

## Q1 – Lists and Slicing

- Store rainfall readings in a list.
- Use slicing for weekly totals: `readings[start:start+7]`.
- Use `max()` and `min()` with `enumerate()` to identify the days.
- Compute moving averages using a sliding window; the running sum reduces repeated additions from O(7n) to O(n).

## Q2 – Tuples, Mutability and Copying

- Tuples are immutable and hashable, so they are valid dictionary keys.
- A nested list such as `[[0] * cols] * rows` shares row objects.
- `copy.copy()` and slicing create shallow copies; `copy.deepcopy()` copies nested objects.

## Q3 – Dictionaries

- Use `dict.get()` and `setdefault()` to count words and accumulate groups.
- Dictionary lookup is average O(1) because Python uses a hash table.
- Sort by `(-count, word)` to get the highest counts and alphabetical tie-breaks.

## Q4 – Sets

- Set operators (`&`, `|`, `-`, `^`) are the natural way to find overlap and differences.
- Sets remove duplicates automatically and support average O(1) membership tests.
- For large datasets, using sets is faster than scanning lists or nested loops.

## Q5 – List Comprehension

- Comprehensions are concise for filtering and transforming data.
- Generator expressions save memory because they compute values lazily.
- List comprehensions are not always best for very large inputs when memory matters.

## Q6 – Nested Data Structures

- The timetable is a dictionary of train IDs to per-train dictionaries.
- Each train stores its name, list of stop tuples, and a set of running days.
- A station index reduces lookup cost because it avoids scanning all train schedules.

## Q7 – Contact Merging

- Normalise phone numbers and names before merging.
- Use a dictionary keyed by a canonical key to group contacts from different sources.
- Keep sets for phone numbers and emails to avoid duplicates while preserving all values.
- This design is O(n) average time versus O(n²) for pairwise comparisons.
