import keyboard
import os
import time
from pathlib import Path

# Define a list to store recorded keystrokes
recorded_sequence = []

# Define the path to the user's Downloads folder
downloads_folder = str(Path.home() / "Downloads")

# Define the file path for the recorded sequence
file_path = os.path.join(downloads_folder, "recorded_sequence.txt")

# Create the directory structure if it doesn't exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Function to process key events
def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        key = e.name

        # Handle space key separately to insert a space character
        if key == "space":
            key = " "  # Replace "space" with a space character
        else:
            # Print the key that was pressed
            print(f"Key '{key}' pressed")

        # Append the key to the recorded sequence
        recorded_sequence.append(key)

try:
    print("Recording... Press 'esc' to stop.")

    # Create a keyboard listener
    keyboard.on_press(on_key_event)

    while True:
        # Continuously run and capture keystrokes
        # Save the recorded sequence to the Downloads folder
        with open(file_path, 'w') as file:
            file.write("".join(recorded_sequence))
        print(f"Recorded sequence saved to '{file_path}'")
        time.sleep(1)  # Sleep for 1 second before checking again

except KeyboardInterrupt:
    pass
finally:
    # Unhook all keyboard events
    keyboard.unhook_all()
