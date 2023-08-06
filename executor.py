import ast_execution
import bnd_execution
import tkinter as tk

def execute():
  program = program_var.get()
  if program == "ast_execution":
    import ast_execution
    ast_execution.main()
  elif program == "bnd_execution":
    import bnd_execution
    bnd_execution.main()
  else:
    print("Please select a program to run.")

    root.quit()

def main():
  root = tk.Tk()
  root.title("Executor")

  label = tk.Label(root, text="Which program would you like to run?")
  label.pack()

  global program_var
  program_var = tk.StringVar()
  radio_ast = tk.Radiobutton(root, text="Playlist-yt \nDownlode", variable=program_var, value="ast_execution")
  radio_bnd = tk.Radiobutton(root, text="Video-yt \nDownlode", variable=program_var, value="bnd_execution")
  radio_ast.pack()
  radio_bnd.pack()

  button = tk.Button(root, text="Execute", command=execute)
  button.pack()

  root.mainloop()

if __name__ == "__main__":
  main()

