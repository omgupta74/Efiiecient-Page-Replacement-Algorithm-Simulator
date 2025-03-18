# Page Replacement Algorithm Simulator

## Overview
This project is a **Page Replacement Algorithm Simulator** built using Python and Tkinter. It allows users to simulate different page replacement algorithms, including **FIFO, LRU, and Optimal**, and visualize their performance in terms of page faults.

## Features
- **Graphical User Interface (GUI)** using Tkinter.
- **Supports three page replacement algorithms:**
  - FIFO (First In First Out)
  - LRU (Least Recently Used)
  - Optimal Page Replacement
- **Displays real-time simulation output** showing memory state after each page request.
- **Calculates and displays total page faults.**

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.x recommended). You can download it from [Python Official Website](https://www.python.org/downloads/).

### Install Dependencies
Run the following command to install Tkinter (if not already installed):
```sh
pip install tk
```

## Usage
### Run the Simulator
Execute the script using:
```sh
python page_replacement_simulator.py
```

### How to Use
1. **Enter the Page Reference String** (comma-separated values, e.g., `7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2`).
2. **Enter the Number of Frames** available for page storage.
3. **Select an Algorithm** from the dropdown list (FIFO, LRU, or Optimal).
4. Click the **Simulate** button.
5. The results, including memory state and total page faults, will be displayed.

## Example
### Input:
```
Page Reference String: 7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2
Number of Frames: 3
Algorithm: FIFO
```

### Output:
```
Algorithm: FIFO
Page: 7 | Memory: [7]
Page: 0 | Memory: [7, 0]
Page: 1 | Memory: [7, 0, 1]
Page: 2 | Memory: [0, 1, 2]
...
Total Page Faults: 9
```

## Contributing
If you’d like to contribute:
1. **Fork** this repository.
2. Create a new **branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m "Add new feature"`).
4. **Push** to the branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

## License
This project is open-source and available under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out at [omgupta200408@gmail.com](mailto:omgupta200408@gmail.com).
