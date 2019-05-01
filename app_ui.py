import app
import tkinter
from tkinter import *

###############################################################################
#
# App_UI:
#   Front-end of the application. Uses Tkinter in conjunction with the back-end
#   to accept queries from and deliver results to the user.
#
###############################################################################

def get_tuples():
    # would perform the search here
    links = ["<put links here>", "https://www.coursera.org/learn/text-mining/lecture/8Ki0H/4-4-text-clustering-generative-probabilistic-models-part-3"]
    text = ["<text results go here>", "and what the likelihood function looks like. And we can also compute the maximum likelihood estimate, to estimate the parameters. In this lecture, we're going to do talk more about how exactly we're going to compute the maximum likelihood estimate. As in most cases the Algorithm can be used to solve this problem for mixture models. So here's the detail of this Algorithm for document clustering. Now, if you have understood how Algorithm works for topic models like TRSA, and I think here it would be very similar. And we just need to adapt a little bit to this new mixture model. So as you may recall Algorithm starts with initialization of all the parameters. So this is the same as what happened before for topic models."]

    results = []
    for i in range(len(links)):
      results.append((links[i], text[i]))

    return results

# Triggered upon hitting the 'submit' button in the UI
def submit():

    # we can get the users keywords they entered like this:
    user_input = search_box.get()
    num_results = int(v.get())

    result = app.search_query(user_input, num_results)

    Label(root, text="Results:").grid(row=2)

    prev = 4  # start at grid row 4
    for tup in result:
        Label(root, text=tup[0], fg="blue").grid(row=prev, column=1,pady=(25,0))
        prev = prev+4
        result = Text(root, height=4, width=100)
        result.insert(INSERT, tup[2])
        result.grid(row=prev, column=1)
        Label(root, text=tup[1]).grid(row=prev, column=0)
        prev= prev + 4


if __name__ == '__main__':
    # this is the main window frame to build off of
    root = tkinter.Tk()

    # add search / text entry box to take in user inputs
    Label(root, text="Search Keywords:", fg="blue").grid(row=0)
    search_box = Entry(root, bd=5)
    search_box.grid(row=0, column=1)
    Button(root, command=submit, text="Submit").grid(row=0, column=3)

    # option meaning
    my_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    v = StringVar()
    v.set("5")
    om = OptionMenu(root, v, *my_options)
    om.grid(row=0, column=2)

    root.mainloop()
