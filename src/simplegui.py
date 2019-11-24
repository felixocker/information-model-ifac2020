#! /usr/bin/env python3
"""simple gui for interaction with the information model"""

from contextlib import redirect_stdout
import changepropagation
import consistency
import duplicateinfo
import findinfo
import formatcompatibility
from io import StringIO
import listclasses
import listinstances
import preprocess_query_results as prepro
import sys
import tkinter as tk
from tkinter import ttk

class exit_button(tk.Button):
    def __init__(self, master):
        tk.Button.__init__(self, master, text="Exit",  command=window.quit)

def call_external(ext, content, lbl, *args):
    funcs = {'change': [changepropagation.main, "Change propagation check completed!"],
             'consistency': [consistency.main, "Consistency check executed!"],
             'duplicate': [duplicateinfo.main, "Check for information duplicates executed!"],
             'find': [findinfo.main, "Search for related information completed!"],
             'format': [formatcompatibility.main, "Format compatibility check executed!"]}
    with StringIO() as buf, redirect_stdout(buf):
        try:
            func = funcs[ext][0]
        except KeyError:
            print('unknown function type')
            sys.exit(1)
        func(*args)
        content.config(text=buf.getvalue())
    lbl.config(text=funcs[ext][1])

# general setup
window = tk.Tk()
window.title("information model")
window.geometry('1400x800')
window.resizable(width=False, height=False)
window.option_add("*font","arial 10")

s = ttk.Style()
s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"font" : ('arial', '10', 'bold')} },
        "TNotebook.Tab": {"configure": {"padding": [50, 5],
                                        "font" : ('arial', '10', 'bold')},}})
s.theme_use("MyStyle")

#tabs
tab_parent = ttk.Notebook(window)
tab_consistency = ttk.Frame(tab_parent)
tab_duplicateinfo = ttk.Frame(tab_parent)
tab_formatcompatibility = ttk.Frame(tab_parent)
tab_findinfo = ttk.Frame(tab_parent)
tab_changepropagation = ttk.Frame(tab_parent)

tab_parent.add(tab_consistency, text="consistency check")
tab_parent.add(tab_duplicateinfo, text="duplicate info")
tab_parent.add(tab_formatcompatibility, text="format compatibility check")
tab_parent.add(tab_findinfo, text="find info")
tab_parent.add(tab_changepropagation, text="check change propagation")
tab_parent.pack(fill="both", expand=True)

# menu
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff = 0)
help_menu = tk.Menu(menubar, tearoff = 0)
file_menu.add_command(label="Nothing", command=window.quit)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)
window.config(menu=menubar)

# tab consistency
consistency_label = tk.Label(tab_consistency, text="Click button to the left to check consistency.")
consistency_output_label = tk.Label(tab_consistency, text="-", anchor="w", justify="left")
exit_button_tab_consistency = exit_button(tab_consistency)
consistency_button = tk.Button(tab_consistency, text="Check consistency", command=lambda: call_external("consistency",consistency_output_label,consistency_label))

consistency_button.grid(row=0, column=0, sticky="w")
consistency_label.grid(row=0, column=1, sticky="w")
consistency_output_label.grid(row=1, column=1, sticky="w")
exit_button_tab_consistency.grid(row=2, column=0, sticky="w")

# tab duplicate info
duplicates_label = tk.Label(tab_duplicateinfo, text="Click button to the left to find duplicate information.")
duplicates_output_label = tk.Label(tab_duplicateinfo, text="-", anchor="w", justify="left")
exit_button_tab_duplicateinfo = exit_button(tab_duplicateinfo)
duplicates_button = tk.Button(tab_duplicateinfo, text="Find duplicate information", command=lambda: call_external("duplicate",duplicates_output_label,duplicates_label))

duplicates_button.grid(row=0, column=0, sticky="w")
duplicates_label.grid(row=0, column=1, sticky="w")
duplicates_output_label.grid(row=1, column=1, sticky="w")
exit_button_tab_duplicateinfo.grid(sticky="w")

# tab format compatibility
format_label = tk.Label(tab_formatcompatibility, text="Click button to the left to find format incompatibilities.")
format_output_label = tk.Label(tab_formatcompatibility, text="-", anchor="w", justify="left")
exit_button_tab_format = exit_button(tab_formatcompatibility)
format_button = tk.Button(tab_formatcompatibility, text="Find format incompatibilities", command=lambda: call_external("format",format_output_label,format_label))

format_button.grid(row=0, column=0, sticky="w")
format_label.grid(row=0, column=1, sticky="w")
format_output_label.grid(row=1, column=1, sticky="w")
exit_button_tab_format.grid(sticky="w")

# tab findinfo
infokind_options = prepro.pp(listclasses.find())
infokind = tk.StringVar(tab_findinfo)
infokind.set("choose")
infokind_dropdown = tk.OptionMenu(tab_findinfo, infokind, *infokind_options)

system_options = prepro.pp(listinstances.find(":system"))
system = tk.StringVar(tab_findinfo)
system.set("choose")
system_dropdown = tk.OptionMenu(tab_findinfo, system, *system_options)

find_label = tk.Label(tab_findinfo, text="Click button to the find related information.")
find_output_label = tk.Label(tab_findinfo, text="-", anchor="w", justify="left")
exit_button_tab_find = exit_button(tab_findinfo)
find_button = tk.Button(tab_findinfo, text="Find info", command=lambda: call_external("find",find_output_label,find_label, 
                        infokind.get(), system.get()))

infokind_dropdown.grid(row=0, column=0, sticky="w")
system_dropdown.grid(row=1, column=0, sticky="w")
find_button.grid(row=2, column=0, sticky="w")
find_label.grid(row=2, column=1, sticky="w")
find_output_label.grid(row=3, column=1, sticky="w")
exit_button_tab_find.grid(sticky="w")

# tab change propagation
infoconc_options = prepro.pp(listinstances.find(":information_concretization"))
infoconc = tk.StringVar(tab_changepropagation)
infoconc.set("choose")
infoconc_dropdown = tk.OptionMenu(tab_changepropagation, infoconc, *infoconc_options)

change_label = tk.Label(tab_changepropagation, text="Click button to the left to check change propagation.")
change_output_label = tk.Label(tab_changepropagation, text="-", anchor="w", justify="left")
exit_button_tab_change = exit_button(tab_changepropagation)
change_button = tk.Button(tab_changepropagation, text="Check change propagation", command=lambda: call_external("change",
                          change_output_label,change_label,infoconc.get()))

infoconc_dropdown.grid(row=0, column=0, sticky="w")
change_button.grid(row=1, column=0, sticky="w")
change_label.grid(row=1, column=1, sticky="w")
change_output_label.grid(row=2, column=1, sticky="w")
exit_button_tab_change.grid(sticky="w")

window.mainloop()
