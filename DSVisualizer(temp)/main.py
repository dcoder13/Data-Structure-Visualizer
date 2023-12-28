import threading
import tkinter as tk
from tkinter import ttk
from src import sortRender
from src import dsRender


class DataStructureVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Structure Visualizer")
        self.root.geometry("700x500")
        self.root.configure(background="white")
        self.root.resizable(False, False)
        # when speed[1] = -1 : stop , 0 : pause , 1 : normal
        self.speed = [50,-1]

    def start_compute(self, SR , selection):
        print("start compute")

        if(self.speed[1] == 0):
            self.speed[1] = 1
            return
        else:
            # (self.speed[1] == -1):
            self.speed[1] = 1
            try:
                SR.startSort(selection)
            except Exception as e:
                print(e)
                if(e.args[0] == "Sort Stopped"):
                    SR.reset()
 
    def pause_compute(self):
        self.speed[1] = 0

    def stop_compute(self):
        self.speed[1] = -1

    def secondary_frame_setup(self):
        secondary_frame = tk.Frame(self.root)

        # title Frame
        title_frame = tk.Frame(secondary_frame)
        title_frame.pack()
        title_label = tk.Label(
            title_frame,
            text="DSA Visualizer",
            width=700,
            font=("Serif Sans", 15),
            background="black",
            foreground="white",
            justify="center",
            anchor="center",
        )
        title_label.config(padx=10, pady=10)
        title_label.pack()

        # setting up the canvas
        canvas_frame = tk.Frame(secondary_frame)
        canvas_frame.pack(side=tk.LEFT)
        canvas = tk.Canvas(canvas_frame, width=500, height=400, background="black")
        canvas.pack(pady=10)
        selection_frame = tk.Frame(secondary_frame)
        selection_frame.configure(height=500, width=200)
        selection_frame.pack(side=tk.RIGHT, anchor="n")
        selection_label = tk.Label(
            selection_frame,
            text="Select Algorithm",
            font=("Serif Sans", 10),
            width="200",
            background="black",
            foreground="white",
        )
        selection_label.pack(pady=10)

        # creating the selection combobox
        selection = tk.ttk.Combobox(selection_frame, width=200)
        selection["values"] = (
            "Bubble Sort",
            "Insertion Sort",
            "Selection Sort",
            "Merge Sort",
            "Quick Sort",
        )
        selection.current(0)
        selection.pack(pady=5)

        SR = sortRender.sortRender(canvas, self.speed)
        
        flow_control_frame = tk.Frame(selection_frame, width=200)
        flow_control_frame.pack(pady=10)

        def start_button_clicked():
            start_button.configure(text="Pause", command=pause_button_clicked)
            self.start_compute(SR, selection)
        
        def pause_button_clicked():
            start_button.configure(text="Start", command=start_button_clicked)
            self.pause_compute()

        def reset_button_clicked():
            self.stop_compute()
            start_button.configure(text="Start", command=start_button_clicked)

        # start button
        start_button = tk.Button(
            flow_control_frame,
            text="Start",
            command=lambda: start_button_clicked(),
            width=200,
        )
        start_button.pack(pady=10)

        # reset button
        reset_button = tk.Button(
            flow_control_frame,
            text="Reset",
            command= reset_button_clicked,
            width=200,
        )
        reset_button.pack(pady=10)

        # frame for algo speed
        speed_frame = tk.Frame(selection_frame, width=200)
        speed_frame.pack(pady=10)
        speed_label = tk.Label(
            speed_frame,
            text="Speed",
            width=100,
            background="black",
            foreground="white",
        )
        speed_label.pack(pady=10)
        speed_var = tk.IntVar(speed_frame, 5)
        # scroll bar for speed
        speed_scale = tk.Scale(
            speed_frame,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            variable=speed_var,
            resolution=1,
        )
        speed_scale.set(self.speed[0])
        speed_scale.pack(pady=10)

        # text box for speed
        speed_entry = tk.Entry(
            speed_frame,
            textvariable=speed_var,
            width=10,
        )
        speed_entry.insert(0, speed_var.get())
        speed_entry.pack(side=tk.LEFT, pady=10)

        def update_speed_scale(*args):
            if speed_var.get():
                self.speed[0] = min(100, speed_var.get())
            else:
                self.speed[0] = 1

        speed_var.trace_add("write", update_speed_scale)
        secondary_frame.pack()

    def main_frame_setup(self):
        pass

    def run(self):
        self.secondary_frame_setup()
        self.root.mainloop()


if __name__ == "__main__":
    visualizer = DataStructureVisualizer()
    visualizer.run()
