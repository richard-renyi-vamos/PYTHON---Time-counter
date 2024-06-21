import tkinter as tk
from datetime import datetime, timedelta

class TimeCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Counter ⏲️")
        
        self.start_time = None
        self.running = False

        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start 🏁", command=self.start, font=("Helvetica", 14))
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(root, text="Stop ⏹️", command=self.stop, font=("Helvetica", 14))
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Reset 🔄", command=self.reset, font=("Helvetica", 14))
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_clock()

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - (self.elapsed_time if self.start_time else timedelta())
            self.running = True
            self.update_clock()
    
    def stop(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.start_time = None
        self.time_label.config(text="00:00:00")

    def update_clock(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            self.time_label.config(text=str(elapsed_time).split('.')[0])
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    time_counter = TimeCounter(root)
    root.mainloop()
