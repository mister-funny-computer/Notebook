import tkinter as tk

window = tk.Tk()
window.title("Блокнот")
window.geometry("400x400")

content_text = tk.Text(window, wrap = "word")
content_text.place(x = 0, y = 0, relwidth = 1, relheight = 1)

main_menu = tk.Menu(window)
window.configure(menu = main_menu)

file_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Файл", menu = file_menu)

new_file_icon = tk.PhotoImage(file = "new_file.gif")

open_file_gif = tk.PhotoImage(file = "open_file.gif")

save_file_gif = tk.PhotoImage(file = "save_file.gif")


file_menu.add_command(label = "Новый", image = new_file_icon, compound = "left",)
file_menu.add_command(label = "Открыть", image = open_file_gif, compound = "left",)
file_menu.add_command(label = "Сохранить", image = save_file_gif, compound = "left")

window.mainloop()

