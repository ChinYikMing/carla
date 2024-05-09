import sys
import curses

# Since carla is not installed via pip, so we have to add path of it
carla_path = '/home/yikming2222/carla-0-9-11/PythonAPI/carla/dist/carla-0.9.11-py3.7-linux-x86_64.egg'
sys.path.append(carla_path)

import carla
import random

def main(stdcsr):
    # Setup Carla client
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    spectator = world.get_spectator()

    # Set up screen
    curses.curs_set(0)
    stdcsr.nodelay(1)
    stdcsr.timeout(100)

    # Main loop
    while True:
        key = stdcsr.getch()

        new_transform = spectator.get_transform()

        # control the yaw to change view left and right based on left, right arrow key
        if key == curses.KEY_LEFT:
            new_transform.rotation.yaw -= 5
            stdcsr.addstr(0, 0, "LEFT\n")
        elif key == curses.KEY_RIGHT:
            new_transform.rotation.yaw += 5
            stdcsr.addstr(0, 0, "RIGHT\n")
        else:
            continue

        spectator.set_transform(new_transform)

        # Refresh the screen
        stdcsr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)

