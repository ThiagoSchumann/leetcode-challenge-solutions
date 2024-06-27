# LeetCode Challenge Solutions

[Leia em Português](README.pt-br.md)

This repository contains solutions to LeetCode challenges, organized by difficulty (easy, medium, hard). Each solution is accompanied by automated tests using `unittest`.

## Project Structure

```
leetcode-challenge-solutions/
├── README.md
└── src
    ├── __init__.py
    ├── problems
    │   ├── __init__.py
    │   ├── easy
    │   │   ├── __init__.py
    │   ├── medium
    │   │   └── __init__.py
    │   └── hard
    │       └── __init__.py
    └── tests
        ├── __init__.py
        ├── easy
        │   ├── __init__.py
        ├── medium
        │   └── __init__.py
        └── hard
            └── __init__.py
```

## Requirements

- Python 3.10 or higher
- `unittest` (included in Python's standard library)

## Virtual Environment Setup

It's recommended to use a virtual environment to isolate the project's dependencies. Follow these steps to set up the environment:

1. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment:
    - On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    - On Windows:
        ```cmd
        .venv\Scripts\activate
        ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## File Structure

### Problems

Each problem is located in the `src/problems` folder, organized by difficulty (`easy`, `medium`, `hard`). Each solution is in its own Python file.

#### Example: `merge_sorted_array.py`

```python
# src/problems/easy/merge_sorted_array.py

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """     
        del(nums1[m: (m + n)])              
        nums1 += nums2
        nums1.sort()
```

### Tests

The tests for each problem are located in the `src/tests` folder, also organized by difficulty (`easy`, `medium`, `hard`). We use the `unittest` framework to create and run the tests.

#### Example: `test_merge_sorted_array.py`

```python
# src/tests/easy/test_merge_sorted_array.py

import unittest
from problems.easy.merge_sorted_array import Solution

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_merge_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

if __name__ == "__main__":
    unittest.main()
```

## Running Tests

To run all tests, use the following command:

```bash
python3 -m unittest discover -s src/tests -p "test_*.py"
```

This command discovers and runs all test files that match the `test_*.py` pattern in the `src/tests` folder.

## Adding New Problems

1. Create a new directory for the problem in the corresponding difficulty folder (`easy`, `medium`, `hard`).
2. Add the solution file to the new directory.
3. Create a corresponding test file in the `src/tests` folder following the same naming pattern.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for new problems, improvements to existing solutions, or bug fixes.
