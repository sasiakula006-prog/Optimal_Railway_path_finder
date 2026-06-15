import streamlit as st
import heapq


class RailwayPlanner:
    def __init__(self):
        self.graph = {}

    def add_station(self, station):
        self.graph[station] = {}

    def add_connection(self, s1, s2, distance):
        self.graph[s1][s2] = distance
        self.graph[s2][s1] = distance

    def shortest_path(self, start, end):
        distances = {station: float('inf') for station in self.graph}
        parent = {}

        distances[start] = 0
        pq = [(0, start)]

        while pq:
            curr_dist, curr_station = heapq.heappop(pq)

            if curr_station == end:
                break

            if curr_dist > distances[curr_station]:
                continue

            for neighbor, weight in self.graph[curr_station].items():
                new_dist = curr_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = curr_station
                    heapq.heappush(pq, (new_dist, neighbor))

        if distances[end] == float('inf'):
            return None, None

        path = []
        current = end

        while current != start:
            path.append(current)
            current = parent[current]

        path.append(start)
        path.reverse()

        return path, distances[end]


# Create Railway Network
railway = RailwayPlanner()

stations = [
    "Hyderabad", "Kazipet", "Warangal", "Khammam",
    "Madira", "Vijayawada", "Eluru", "Tadepalligudem",
    "Rajahmundry", "Samalkota", "Annavaram", "Tuni",
    "Anakapally", "Vizag", "Vizianagaram", "Bhubaneswar",
    "Cuttack", "Bhadrakh", "Balasore", "Kharagpur",
    "Howrah", "Nalgonda", "Miryalaguda", "Piduguralla",
    "Guntur", "Tenali", "Ongole", "Nellore", "Gudur",
    "Renigunda", "Tirupati", "Puttur", "Nagari",
    "Tiruttani", "Tiruvallur", "Avadi", "Chennai",
    "Katpadi", "Jolarpttai", "Bengaluru", "Guntakal",
    "Nagpur", "Itarsi", "Bhopal",
    "Lakshmi Bhai Jhansi", "Gwalior", "Agra", "Delhi",
    "Bhimavaram Town", "Akividu", "Kaikaluru",
    "Gudivada", "Bapatla", "Chirala",
    "Kavali", "Sullurupeta", "Gummidipoondi", "Perambur"
]

for station in stations:
    railway.add_station(station)

connections = [
    ("Hyderabad", "Kazipet", 135),
    ("Kazipet", "Warangal", 10),
    ("Warangal", "Khammam", 108),
    ("Khammam", "Madira", 45),
    ("Madira", "Vijayawada", 54),

    ("Vijayawada", "Tenali", 32),
    ("Tenali", "Ongole", 107),
    ("Ongole", "Nellore", 116),
    ("Nellore", "Gudur", 39),

    ("Gudur", "Renigunda", 83),
    ("Renigunda", "Tirupati", 10),
    ("Renigunda", "Puttur", 22),
    ("Puttur", "Nagari", 15),
    ("Nagari", "Tiruttani", 15),
    ("Tiruttani", "Tiruvallur", 51),
    ("Tiruvallur", "Avadi", 21),
    ("Avadi", "Chennai", 21),

    ("Bhimavaram Town", "Akividu", 20),
    ("Akividu", "Kaikaluru", 18),
    ("Kaikaluru", "Gudivada", 38),
    ("Gudivada", "Vijayawada", 40),

    ("Tenali", "Bapatla", 50),
    ("Bapatla", "Chirala", 17),
    ("Chirala", "Ongole", 35),

    ("Ongole", "Kavali", 57),
    ("Kavali", "Nellore", 60),

    ("Gudur", "Sullurupeta", 52),
    ("Sullurupeta", "Gummidipoondi", 42),
    ("Gummidipoondi", "Perambur", 35),
    ("Perambur", "Chennai", 8)
]

for s1, s2, d in connections:
    railway.add_connection(s1, s2, d)


# ---------------- UI ----------------

st.set_page_config(
    page_title="Rail Yatra",
    page_icon="🚆",
    layout="centered"
)

st.title("🚆 Rail Yatra")
st.subheader("Find the Shortest Railway Route")

source = st.selectbox(
    "Select Source Station",
    sorted(railway.graph.keys())
)

destination = st.selectbox(
    "Select Destination Station",
    sorted(railway.graph.keys())
)

if st.button("Find Route"):

    path, distance = railway.shortest_path(
        source,
        destination
    )

    if path:
        st.success(
            f"Shortest Distance: {distance} km"
        )

        st.markdown("### Route")

        st.write(" ➜ ".join(path))

    else:
        st.error("No route found.")
        