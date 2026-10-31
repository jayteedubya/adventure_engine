"""window.py
This file contains ultities and constants for managing windows (sectors of the map).
"""

WINDOW_WIDTH = 80
WINDOW_HEIGHT = 80


class Window:
    """Manages a 'window' or section of the full map."""

    _window_upper_bound: int
    _window_lower_bound: int
    _window_right_bound: int
    _window_left_bound: int
    _map_chunk: str

    def __init__(
        self,
        map_chunk: str,
        window_upper_bound: int,
        window_lower_bound: int,
        window_right_bound: int,
        window_left_bound: int,
    ) -> None:
        self._map_chunk = map_chunk
        self._window_upper_bound = window_upper_bound
        self._window_lower_bound = window_lower_bound
        self._window_right_bound = window_right_bound
        self._window_left_bound = window_left_bound

    def xy_to_linear(self, x: int, y: int) -> int:

        return 0
