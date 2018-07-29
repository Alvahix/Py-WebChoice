from tkinter import *
import webbrowser
root = Tk()

# logo frame
logo_window = Frame(root, bd=1, bg='black')
logo_window.pack(side=TOP, anchor=N, fill=X)

# question frame
question_window = Frame(root, bd=1, bg='black')
question_window.pack(side=TOP, anchor=N, fill=X)

# entry frame
entry_window = Frame(root, bd=1, bg='gray')
entry_window.config(highlightbackground='black')
entry_window.pack(side=TOP, anchor=N, fill=X)

# title frame
title_window = Frame(root, bd=1, bg='black')
title_window.pack(side=TOP, anchor=N, fill=X)

# button frame
button_window = Frame(root, bd=1, bg='black')
button_window.pack(side=TOP, anchor=N, fill=X)

# logo
photo_logo = PhotoImage(file='webchoice.png')
label_1 = Label(logo_window, image=photo_logo)
label_1.pack()

# speed key functions
class speed_buttons:
    def __init__(self,name,func):
        self.name = name

        button = Button(button_window, text=name,command=func, bg='gray')
        button.pack(side=TOP, anchor=NE, fill=X)

def google():
    webbrowser.open('https://www.google.com/')
def youtube():
    webbrowser.open('https://www.youtube.com/')
def reddit():
    webbrowser.open('https://www.reddit.com/')
def hulu():
    webbrowser.open('https://www.hulu.com/')
def netflix():
    webbrowser.open('https://www.netflix.com/')
def weather():
    webbrowser.open('https://www.weather.com/')

# question prompts
label_question = Label(question_window, text='What website would you like to go to?', bg='gray64', font=('Helvetica', 11))
label_question.pack(fill=X)

# entry space
entry_choose = Entry(entry_window, width=43)
entry_choose.pack(side=LEFT)

# get submitted info, possibly as questions
def sitechoice(event):
    web = entry_choose.get() # entry is returned as a string
    # reddit
    if web in ['reddit', 'Reddit']:
        label_question.destroy()
        entry_choose.destroy()
        submit_button.destroy()
        label_sub = Label(question_window, text='What subreddit would you like to view?', bg='gray64', font=('Helvetica', 11))
        label_sub.pack(fill=X)
        entry_sub = Entry(entry_window, width=43)
        entry_sub.pack(side=LEFT)

        def subchoice(event):
            global sub_1
            sub_1 = entry_sub.get()
            webbrowser.open('www.reddit.com/r/' + sub_1)
            return subchoice

        root.bind('<Return>', subchoice)
        global red_but
        red_but = PhotoImage(file='reddit.png')
        sub_button = Button(entry_window, image=red_but, bg='gray64', width=53)
        sub_button.bind('<Button>', subchoice)
        sub_button.pack(side=RIGHT)
        # webbrowser.open('www.' + web + '.com/r/' + sub)
    # weather
    elif web in ['weather', 'Weather']:
        label_question.destroy()
        entry_choose.destroy()
        submit_button.destroy()
        label_loc = Label(question_window, text='What zipcode would you like to view?', bg='gray64',font=('Helvetica', 11))
        label_loc.pack(fill=X)
        entry_loc = Entry(entry_window, width=43)
        entry_loc.pack(side=LEFT)

        def locchoice(event):
            global loc
            loc = entry_loc.get()
            webbrowser.open('https://weather.com/weather/today/l/' + loc + ':4:US')
            root.destroy
            return locchoice

        root.bind('<Return>', locchoice)
        global wea_but
        wea_but = PhotoImage(file='weather.png')
        loc_button = Button(entry_window, image=wea_but, bg='gray64', width=53)
        loc_button.bind('<Button>', locchoice)
        loc_button.pack(side=RIGHT)
    # youtube
    elif web in ['youtube', 'Youtube']:
        label_question.destroy()
        entry_choose.destroy()
        submit_button.destroy()
        label_vid = Label(question_window, text='For homepage, hit enter. Or search:', bg='gray64',font=('Helvetica', 11))
        label_vid.pack(fill=X)
        entry_vid = Entry(entry_window, width=43)
        entry_vid.pack(side=LEFT)

        def vidchoice(event):
            global vid
            vid = entry_vid.get()
            if vid in ['home', 'Home']:
                webbrowser.open('https://www.youtube.com')
            else:
                vid = entry_vid.get()
                webbrowser.open('https://www.youtube.com/results?search_query=' +vid)
                root.destroy
            return vidchoice

        root.bind('<Return>', vidchoice)
        global vid_but
        vid_but = PhotoImage(file='youtube.png')
        vid_button = Button(entry_window, image=vid_but, bg='gray64', width=53)
        vid_button.bind('<Button>', vidchoice)
        vid_button.pack(side=RIGHT)
    # netflix
    elif web in ['Netflix', 'netflix']:
        label_question.destroy()
        entry_choose.destroy()
        submit_button.destroy()
        label_watch = Label(question_window, text='For homepage, hit enter. Or search:',  bg='gray64',font=('Helvetica', 11))
        label_watch.pack(fill=X)
        entry_watch = Entry(entry_window, width=43)
        entry_watch.pack(side=LEFT)

        def watchchoice(event):
            global watch
            watch = entry_watch.get()
            if watch == '':
                webbrowser.open('https://www.netflix.com/browse')
            else:
                webbrowser.open('https://www.netflix.com/search?q=' + watch)
            return watchchoice

        root.bind('<Return>', watchchoice)
        global watch_but
        watch_but = PhotoImage(file='netflix.png')
        watch_button = Button(entry_window, image=watch_but, bg='gray64', width=53)
        watch_button.bind('<Button>', watchchoice)
        watch_button.pack(side=RIGHT)

    #google
    elif web in ['google', 'Google']:
        label_question.destroy()
        entry_choose.destroy()
        submit_button.destroy()
        label_cho = Label(question_window, text='Are you looking for mail, calendar, or drive?',  bg='gray64',font=('Helvetica', 11))
        label_cho.pack(fill=X)
        entry_cho = Entry(entry_window, width=43)
        entry_cho.pack(side=LEFT)

        def chochoice(event):
            global cho
            cho = entry_cho.get()
            if cho in ['drive', 'Drive']:
                webbrowser.open('https://drive.google.com/drive/my-drive')
            elif cho in ['mail', 'Mail']:
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            elif cho in ['calendar', 'Calendar']:
                webbrowser.open('https://calendar.google.com/calendar/r?pli=1')
            else:
                webbrowser.open('https://www.google.com')
            return chochoice

        root.bind('<Return>', chochoice)
        global cho_but
        cho_but = PhotoImage(file='google.png')
        cho_button = Button(entry_window, image=cho_but, bg='gray64', width=53)
        cho_button.bind('<Button>', chochoice)
        cho_button.pack(side=RIGHT)
    # hulu
    elif web in ['Hulu', 'hulu']:
        label_question.destroy()
        entry_choose.destroy()
        submit_button.destroy()
        label_hul = Label(question_window, text='For homepage, hit enter. Or search:',  bg='gray64',font=('Helvetica', 11))
        label_hul.pack(fill=X)
        entry_hul = Entry(entry_window, width=43)
        entry_hul.pack(side=LEFT)

        def hulchoice(event):
            global hul
            hul = entry_hul.get()
            if hul == '':
                webbrowser.open('https://www.hulu.com')
            else:
                hul = entry_hul.get()
                webbrowser.open('https://www.hulu.com/search?q=' + hul)
                root.destroy
            return hulchoice

        root.bind('<Return>', hulchoice)
        global hul_but
        hul_but = PhotoImage(file='hulu.png')
        hul_button = Button(entry_window, image=hul_but, bg='gray64', width=53)
        hul_button.bind('<Button>', hulchoice)
        hul_button.pack(side=RIGHT)
    else:
        webbrowser.open('www.' + web + '.com/')
        root.destroy

# bind enter key to submit button
root.bind('<Return>', sitechoice)

# submit button
submit_button = Button(entry_window, text='Go!', bg='gray64', command=sitechoice, width=7)
submit_button.pack(side=RIGHT)

# speed keys
label_speed = Label(title_window, text='Speed Buttons:', bg='gray64')
label_speed.pack(fill=X)
google = speed_buttons('Google',google)
youtube = speed_buttons('Youtube', youtube)
reddit = speed_buttons('Reddit', reddit)
hulu = speed_buttons('Hulu', hulu)
netflix = speed_buttons('Netflix', netflix)
weather = speed_buttons('Weather', weather)

root.mainloop()  # window is continuously on screen until you close it, infinite loop

# END