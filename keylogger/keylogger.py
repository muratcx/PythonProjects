import keyboard
import os
import time

# Define a list to store recorded keystrokes
recorded_sequence = []

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

# Function to save the recorded sequence to a file
def save_recorded_sequence_to_file(file_name):
    try:
        with open(file_name, 'a') as file:  # Use 'a' for append mode
            file.write("".join(recorded_sequence))
            file.write("\n")  # Add a newline to separate recordings
        print(f"Recorded sequence saved to '{file_name}'")
    except Exception as e:
        print(f"Error: {e}")

# Function to save the recorded data and reset the sequence
def save_and_clear_sequence(file_name):
    if len(recorded_sequence) > 0:
        save_recorded_sequence_to_file(file_name)
        recorded_sequence.clear()  # Clear the recorded data

# Set the idle time threshold in seconds (adjust as needed)
idle_time_threshold = 3 # 3 seconds of inactivity

# Initialize the last activity time
last_activity_time = time.time()

try:
    print("Recording... Press 'esc' to stop and save.")
    
    # Create a keyboard listener
    keyboard.on_press(on_key_event)

    while True:
        # Continuously run and capture keystrokes

        # Check if the 'esc' key has been pressed to exit the loop
        if keyboard.is_pressed('esc'):
            break

        # Check for inactivity and save data if the threshold is reached
        current_time = time.time()
        if (current_time - last_activity_time) >= idle_time_threshold:
            current_directory = os.getcwd()
            file_name = os.path.join(current_directory, "recorded_sequence.txt")
            save_and_clear_sequence(file_name)
            last_activity_time = current_time  # Update last activity time

        time.sleep(1)  # Sleep for 1 second before checking again

except KeyboardInterrupt:
    pass
finally:
    # Ensure the recorded data is saved before exiting
    current_directory = os.getcwd()
    file_name = os.path.join(current_directory, "recorded_sequence.txt")
    save_and_clear_sequence(file_name)

    # Unhook all keyboard events
    keyboard.unhook_all()
