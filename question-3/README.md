# Real-time Multiplayer Game with Python and Textual

## Components

### server.py

This script implements the game server using `socketio` and `eventlet`.  It handles:

* **User Management:** Tracks connected users and their readiness status.
* **Room Management:** Creates and manages game rooms, including tracking users in each room.
* **Game Logic:** Handles starting new rounds, receiving player scores, determining winners, and broadcasting game events to clients.
* **Messaging:** Allows users to send and receive chat messages within rooms.

### client.py

This script implements the client-side UI using the Textual framework. It provides:

* **Connection:** use `socketio` for real-time communication.
* **Room Interaction:** Allows users to create or join rooms.
* **Gameplay:** Enables players to mark themselves as ready, submit scores during a round, and view the winner(s).
* **Chat:** Displays messages sent by other players in the room.
* **UI:** Uses Textual to create a simple text-based interface for interaction.

## How to Run

1. **Install Dependencies:**
    ```bash
    pip install socketio eventlet textual
    ```
2. **Run the Server:**
    ```bash
    python server.py
    ```
3. **Start the Client (in a separate terminal):**
    ```bash
    python client.py
    ```
The client will prompt you for your name and then present options to create or join a room.

