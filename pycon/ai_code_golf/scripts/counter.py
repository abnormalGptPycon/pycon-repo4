import tkinter as tk
import threading
import time
import os

try:
    import keyboard
except ImportError:
    print("Please install the 'keyboard' package using 'pip install keyboard==0.13.5'.")


class KeystrokeCounter:
    def __init__(self):
        self.count = 0
        self.running = True
        self.log_file = "keystrokes.log"
        self.create_log_file()
        self.start_logging()

    def increment_count(self, event):
        self.count += 1

    def start_counting(self):
        keyboard.on_press(self.increment_count)
        while self.running:
            keyboard.wait()

    def stop_counting(self):
        self.running = False
        keyboard.unhook_all()

    def create_log_file(self):
        # Ensure the log file is created in the same directory as the script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.log_file = os.path.join(script_dir, "keystrokes.log")
        with open(self.log_file, "w") as file:
            file.write("Keystrokes: 0\n")

    def start_logging(self):
        def log_count():
            while self.running:
                try:
                    with open(self.log_file, "w") as file:
                        file.write(str(self.count))
                except IOError as e:
                    print(f"Error writing to log file: {e}")
                time.sleep(0.1)  # Log every 100 milliseconds

        logging_thread = threading.Thread(target=log_count)
        logging_thread.daemon = True
        logging_thread.start()


class KeystrokeOverlay(tk.Tk):
    def __init__(self, counter):
        super().__init__()
        self.counter = counter
        self.start_time = time.time()
        self.title("Keystroke Counter")
        self.geometry("200x100+100+100")  # Reduced height for compact display
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.8)  # Semi-transparent
        self.overrideredirect(True)  # Remove window borders

        # Keystroke count label
        self.label = tk.Label(self, text="Keystrokes: 0", font=("Helvetica", 22))
        self.label.pack(pady=(15, 0))  # Reduced padding

        # Timer label with increased font size
        self.timer_label = tk.Label(self, text="00:00", font=("Helvetica", 20, "bold"))
        self.timer_label.pack(pady=(0, 0))  # Minimal padding

        self.wm_attributes("-topmost", 1)  # Ensure the window stays on top
        # Bind mouse events for dragging
        self.bind("<Button-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)
        self._drag_data = {"x": 0, "y": 0}

    def start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def do_drag(self, event):
        x = self.winfo_x() + event.x - self._drag_data["x"]
        y = self.winfo_y() + event.y - self._drag_data["y"]
        self.geometry(f"+{x}+{y}")

    def update_display(self):
        # Update keystroke count
        self.label.config(text=f"Keystrokes: {self.counter.count}")

        # Update timer
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

        self.after(100, self.update_display)  # Update every 100 milliseconds


def start_overlay(counter):
    overlay = KeystrokeOverlay(counter)
    overlay.update_display()
    overlay.mainloop()


def main():
    counter = KeystrokeCounter()
    counting_thread = threading.Thread(target=counter.start_counting)
    counting_thread.daemon = True
    counting_thread.start()

    try:
        start_overlay(counter)
    finally:
        counter.stop_counting()


if __name__ == "__main__":
    main()
