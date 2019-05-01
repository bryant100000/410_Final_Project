import app
import tkinter
from tkinter import *

###############################################################################
#
# ***RUN THIS in order to use the GUI and thereby the application!
# App_UI:
#   Front-end of the application. Uses Tkinter in conjunction with the back-end
#   to accept queries from and deliver results to the user.
#
###############################################################################


# global list to hold active result tkinter widgets
active_result_widgets = []

def clear_current_results():
    # clear old tkinter result widgets on the screen

    global active_result_widgets
    for result in active_result_widgets:
        for obj in result:
            obj.destroy()

    active_result_widgets.clear()

def add_results_to_gui(tup, row_count):
    # place each result tuple onto gui window
    # each result tuple displays the video link for reference, text
    # search results, and associated timestamp

    link = Label(root, text=tup[0], fg="blue")
    link.grid(row=row_count, column=1,pady=(25,0))
    row_count += 4

    txt = Text(root, height=4, width=100)
    txt.insert(INSERT, tup[2])
    txt.grid(row=row_count, column=1)

    ts = Label(root, text=tup[1])
    ts.grid(row=row_count, column=0)
    row_count += 4

    result_objs = [link, txt, ts]
    active_result_widgets.append(result_objs)

    return row_count

def submit():
    # clicking submit button triggers this function

    # fetch user input (keywords) and number of requested results
    user_input = search_box.get()
    num_results = int(v.get())

    # perform search
    result = app.search_query(user_input, num_results)

    # clear any leftover results on gui screen before displaying new results
    clear_current_results()

    # add "results" header onto Gui
    Label(root, text="Results:").grid(row=2)

    row_count = 4 # start at grid row 4 (when displaying results)

    for tup in result:
        row_count = add_results_to_gui(tup, row_count)


if __name__ == '__main__':

    # this is the main window object of the gui
    root = tkinter.Tk()

    # add search / text entry box to take in user inputs
    Label(root, text="Search Keywords:", fg="blue").grid(row=0)
    search_box = Entry(root, bd=5)
    search_box.grid(row=0, column=1)
    Button(root, command=submit, text="Submit").grid(row=0, column=3)

    # add OptionMenu to offer user selection of number of results
    my_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    v = StringVar()
    v.set("5")
    om = OptionMenu(root, v, *my_options)
    om.grid(row=0, column=2)

    # start gui
    root.mainloop()
