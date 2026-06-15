# 🚆 Rail Yatra - Optimal Railway Path Finder

A web application that finds the shortest railway route between Indian railway stations using Dijkstra's shortest path algorithm.

## Overview

Rail Yatra is an interactive tool built with **Streamlit** that helps users find the most efficient railway route between any two stations in the Indian railway network. It uses a graph-based approach with the Dijkstra algorithm to compute the shortest distance path.

## Features

- 🗺️ **Comprehensive Railway Network**: Covers 56 major Indian railway stations
- 🔍 **Shortest Path Algorithm**: Uses Dijkstra's algorithm for optimal route finding
- 🎯 **User-Friendly Interface**: Simple Streamlit web interface for easy navigation
- 📊 **Distance Calculation**: Displays total distance in kilometers
- 🛤️ **Visual Route Display**: Shows the complete path with stations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sasiakula006-prog/Optimal_Railway_path_finder.git
cd Optimal_Railway_path_finder
```

2. Install required dependencies:
```bash
pip install streamlit heapq
```

3. Run the application:
```bash
streamlit run Rail_yatri/optimal_path_finder.py
```

## How to Use

1. Open the application in your browser
2. Select a **Source Station** from the dropdown menu
3. Select a **Destination Station** from the dropdown menu
4. Click **"Find Route"** button
5. View the shortest route and total distance

## Algorithm Details

The project implements **Dijkstra's Shortest Path Algorithm**:
- **Time Complexity**: O((V + E) log V) where V = vertices, E = edges
- **Space Complexity**: O(V)
- Uses a min-heap (priority queue) for efficient node selection

## Railway Network Coverage

The network includes stations across major Indian routes:
- **Hyderabad Region**: Hyderabad, Kazipet, Warangal, Khammam
- **Andhra Pradesh**: Vijayawada, Rajahmundry, Vizag, Tirupati
- **Tamil Nadu**: Chennai, Tirupati routes
- **Odisha**: Bhubaneswar, Cuttack, Balasore
- **Maharashtra & Other Regions**: Nagpur, Delhi, Agra

## Project Structure

```
Optimal_Railway_path_finder/
├── Rail_yatri/
│   └── optimal_path_finder.py    # Main application
└── README.md
```

## Class: RailwayPlanner

### Methods

- **`__init__()`**: Initializes the railway graph
- **`add_station(station)`**: Adds a new station to the network
- **`add_connection(s1, s2, distance)`**: Adds bidirectional connection between two stations
- **`shortest_path(start, end)`**: Finds the shortest path using Dijkstra's algorithm
  - Returns: `(path, distance)` tuple or `(None, None)` if no route exists

## Dependencies

- **streamlit**: Web framework for building the interactive UI
- **heapq**: Python's built-in heap queue module for priority queue operations

## Example Usage

```python
railway = RailwayPlanner()
railway.add_station("Hyderabad")
railway.add_station("Chennai")
railway.add_connection("Hyderabad", "Chennai", 600)

path, distance = railway.shortest_path("Hyderabad", "Chennai")
# Output: (['Hyderabad', 'Chennai'], 600)
```

## Future Enhancements

- Add more stations to expand network coverage
- Implement alternative routes with different criteria (time, cost)
- Add real-time train schedules
- Include fare information
- Support for intermediate stop suggestions
- Route visualization with maps

## Author

Created by: sasiakula006-prog

## License

MIT License - Feel free to use and modify for your projects

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature suggestions.

---

**Disclaimer**: This is a demonstration project. For actual railway travel planning, please refer to official Indian Railways websites.
