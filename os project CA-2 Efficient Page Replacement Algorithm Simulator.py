import tkinter as tk
from tkinter import ttk, messagebox

class PageReplacementSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Simulator")
        self.root.geometry("500x500")

        # Labels and Entry Fields
        tk.Label(root, text="Page Reference String (comma-separated):").pack(pady=5)
        self.page_entry = tk.Entry(root, width=50)
        self.page_entry.pack(pady=5)

        tk.Label(root, text="Number of Frames:").pack(pady=5)
        self.frame_entry = tk.Entry(root, width=10)
        self.frame_entry.pack(pady=5)

        tk.Label(root, text="Select Algorithm:").pack(pady=5)
        self.algo_choice = ttk.Combobox(root, values=["FIFO", "LRU", "Optimal"])
        self.algo_choice.pack(pady=5)
        self.algo_choice.set("FIFO")

        # Run Button
        tk.Button(root, text="Simulate", command=self.run_simulation, bg="blue", fg="white").pack(pady=10)

        # Output Box
        self.output_text = tk.Text(root, height=15, width=60)
        self.output_text.pack(pady=10)

    def run_simulation(self):
        try:
            pages = list(map(int, self.page_entry.get().split(",")))
            frames = int(self.frame_entry.get())
            algorithm = self.algo_choice.get()

            if frames <= 0:
                messagebox.showerror("Error", "Frames must be a positive number!")
                return

            if algorithm == "FIFO":
                result, faults = self.fifo(pages, frames)
            elif algorithm == "LRU":
                result, faults = self.lru(pages, frames)
            elif algorithm == "Optimal":
                result, faults = self.optimal(pages, frames)
            else:
                messagebox.showerror("Error", "Invalid algorithm selected!")
                return

            self.display_result(result, faults, algorithm)
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Enter numbers separated by commas.")

    def fifo(self, pages, frames):
        memory, page_faults, result = [], 0, []

        for page in pages:
            if page not in memory:
                if len(memory) < frames:
                    memory.append(page)
                else:
                    memory.pop(0)
                    memory.append(page)
                page_faults += 1
            result.append(f"Page: {page} | Memory: {memory}")

        return result, page_faults

    def lru(self, pages, frames):
        memory, page_faults, result, recent = [], 0, [], {}

        for i, page in enumerate(pages):
            if page not in memory:
                if len(memory) < frames:
                    memory.append(page)
                else:
                    lru_page = min(recent, key=recent.get)
                    memory.remove(lru_page)
                    memory.append(page)
                page_faults += 1
            recent[page] = i
            result.append(f"Page: {page} | Memory: {memory}")

        return result, page_faults

    def optimal(self, pages, frames):
        memory, page_faults, result = [], 0, []

        for i, page in enumerate(pages):
            if page not in memory:
                if len(memory) < frames:
                    memory.append(page)
                else:
                    future = {mem_page: pages[i + 1:].index(mem_page) if mem_page in pages[i + 1:] else float("inf") for mem_page in memory}
                    memory.remove(max(future, key=future.get))
                    memory.append(page)
                page_faults += 1
            result.append(f"Page: {page} | Memory: {memory}")

        return result, page_faults

    def display_result(self, result, faults, algorithm):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Algorithm: {algorithm}\n")
        self.output_text.insert(tk.END, "\n".join(result))
        self.output_text.insert(tk.END, f"\n\nTotal Page Faults: {faults}")

# Run the GUI Application
root = tk.Tk()
app = PageReplacementSimulator(root)
root.mainloop()
