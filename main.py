from tkinter import Tk, Label, Button, Entry, PhotoImage, Text, IntVar, StringVar, font
import random


class Millionaire:


  def __init__(self, master):
    self.master = master
    master.title("Who Wants To Be A Millionaire?")
    self.master.config(bg='navy blue')
    self.timer_var = StringVar()
    self.timer_var.set("15")
    self.timer = int(self.timer_var.get())
    self.mon = [
        100, 400, 500, 9000, 10000, 30000, 50000, 150000, 250000, 500000
    ]
    self.r_u_sure = Label(text="",
                          fg='white',
                          bg='navy blue',
                          font=('Elephant', 10, 'bold'))
    self.check = Label(text="Checkpoints: ☆ ☆ ☆",
                       fg='gold',
                       bg='navy blue',
                       font=('Times'))
    self.check.grid(row=0, column=0)
    self.time_display = Label(textvariable=self.timer_var,
                              fg='white',
                              bg='navy blue',
                              font=('Comic Sans MS', 10, 'bold'))

    phone = PhotoImage(file="phone.png")
    help = phone.subsample(3, 3)
    self.help_button = Button(master,
                              image=help,
                              command=self.help_button,
                              highlightbackground='green',
                              fg='white',
                              bg='navy blue',
                              activebackground='navy blue')
    self.help_button.image = help

    exit = PhotoImage(file="nigerundayoo_smokeyy.png")
    nigerundayoo = exit.subsample(3, 3)
    self.leave_button = Button(master,
                               image=nigerundayoo,
                               command=self.leave,
                               highlightbackground='green',
                               fg='white',
                               bg='navy blue')
    self.leave_button.image = nigerundayoo

    answer = PhotoImage(file='answer_box.png')
    answer_box = answer.subsample(2, 1)
    self.button_1 = Button(master,
                           image=answer_box,
                           fg='white',
                           compound='center',
                           highlightthickness=0,
                           relief='flat',
                           bg='navy blue',
                           wraplength=150,
                           activebackground='navy blue',
                           activeforeground='gold',
                           font=('Comic Sans MS', 10, 'bold'))
    self.button_1.image = answer_box

    self.button_2 = Button(master,
                           image=answer_box,
                           fg='white',
                           compound='center',
                           highlightthickness=0,
                           relief='flat',
                           bg='navy blue',
                           wraplength=150,
                           activebackground='navy blue',
                           activeforeground='gold',
                           font=('Comic Sans MS', 10, 'bold'))
    self.button_2.image = answer_box

    self.button_3 = Button(master,
                           image=answer_box,
                           fg='white',
                           compound='center',
                           highlightthickness=0,
                           relief='flat',
                           bg='navy blue',
                           wraplength=150,
                           activebackground='navy blue',
                           activeforeground='gold',
                           font=('Comic Sans MS', 10, 'bold'))
    self.button_3.image = answer_box

    self.button_4 = Button(master,
                           image=answer_box,
                           fg='white',
                           compound='center',
                           highlightthickness=0,
                           relief='flat',
                           bg='navy blue',
                           wraplength=150,
                           activebackground='navy blue',
                           activeforeground='gold',
                           font=('Comic Sans MS', 10, 'bold'))
    self.button_4.image = answer_box

    self.des = False
    self.skip_ques = False
    self.game_started = False
    self.checkpoint_1 = False
    self.checkpoint_2 = False
    self.checkpoint_3 = False
    self.check_ques = {
        0: False,
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False
    }

    self.player_money = 0
    self.money_display = Label(master,
                               text=f"Money: ${self.player_money}",
                               fg='green',
                               bg='navy blue',
                               font=('Times'))
    self.money_display.grid(row=0, column=1, columnspan=5)
    self.label_help = Label(master,
                            text="",
                            fg='white',
                            bg='navy blue',
                            font=('Comic Sans MS', 10, 'bold'))
    self.label_help.grid(row=2, column=0, columnspan=5)
    self.label_question = Label(
        master,
        text=
        "Welcome... \n\nTo Who Wants To Be A Millionaire!\n\nPress Start To Begin",
        fg='white',
        bg='navy blue',
        font=('Comic Sans MS', 15, 'bold'),
        wraplength=300)
    self.label_question.grid(row=2, column=0, columnspan=5)
    self.start_button = Button(master,
                               text="Start",
                               command=self.start_game,
                               highlightbackground='gold',
                               fg='black',
                               bg='green',
                               font=('Comic Sans MS', 10, 'bold'))
    self.start_button.grid(row=3, column=0, columnspan=5)

  def button_del(self):
    self.button_1.grid_forget()
    self.button_2.grid_forget()
    self.button_3.grid_forget()
    self.button_4.grid_forget()
    self.help_button.grid_forget()
    self.leave_button.grid_forget()

  def butt_dis(self):
    self.button_1.config(state='disabled')
    self.button_2.config(state='disabled')
    self.button_3.config(state='disabled')
    self.button_4.config(state='disabled')

  def butt_nor(self):
    self.button_1.config(state='normal')
    self.button_2.config(state='normal')
    self.button_3.config(state='normal')
    self.button_4.config(state='normal')

  def remember(self):
    self.label_help.config(text="")
    self.time_display.grid(row=5, column=1)
    self.button_1.grid(row=4, column=0)
    self.button_2.grid(row=4, column=2)
    self.button_3.grid(row=6, column=0)
    self.button_4.grid(row=6, column=2)
    self.label_question.grid(row=2, column=0, columnspan=5)
    self.timer = self.temp

  def col_switch(self):
    rando_butt.config(fg='white')
    rando_butt_1.config(fg='white')

  def help_button(self):
    self.butt_list = [
        self.button_1, self.button_2, self.button_3, self.button_4
    ]
    if random.randint(1, 2) == 1:
      self.temp = self.timer
      self.timer = 9000
      self.time_display.grid_forget()
      self.label_question.grid_forget()
      self.button_1.grid_forget()
      self.button_2.grid_forget()
      self.button_3.grid_forget()
      self.button_4.grid_forget()
      global rando_butt, rando_butt_1
      rando_butt = random.choice(self.butt_list)
      rando_butt.config(fg='green')
      self.butt_list.remove(rando_butt)
      rando_butt_1 = random.choice(self.butt_list)
      rando_butt_1.config(fg='green')
      self.label_help.config(
          text=
          "You decided to call your friend for help.\n\nHe decided on two possible answers.\nHe warns you that he is not an expert, and that both of the answers could be wrong.\n\n¯\_('_')_/¯",
          wraplength=300)
      self.master.after(5000, self.remember)
      if rando_butt['fg'] == 'green':
        self.master.after(9000, self.col_switch)
      self.help_button.grid_forget()

    # Goes to the next question, but forfeits the money from the question that was skipped
    else:
      if self.check_ques[9] != True:
        self.help_button.grid_forget()
        self.skip_ques = True
        self.temp = self.timer
        self.timer = 9000
        self.time_display.grid_forget()
        self.label_question.grid_forget()
        self.button_1.grid_forget()
        self.button_2.grid_forget()
        self.button_3.grid_forget()
        self.button_4.grid_forget()
        self.label_help.config(
            text=
            "You decided to skip this question.\n\nBy doing so, you also gave up on the rewards for this question.\nLet's hope you have better luck next question.\n\n¯\_('_')_/¯",
            wraplength=300)
        self.master.after(5000, self.remember)
        self.next_ques()
        self.help_button.grid_forget()

  def time_change(self):
    if self.timer_var.get() == 5:
      self.time_display.config(fg='red')

  def timer_upd(self):
    while self.timer > 0 and self.des != True:
      self.timer -= 1
      if self.timer == 5:
        self.time_display.config(fg='red')
      self.timer_var.set(self.timer)
      self.master.after(1000, self.master.update())
    if self.timer <= 0:
      self.timer_bad_end()

  def timer_bad_end(self):
    self.label_question.configure(text="You Ran Out Of Time\n\nYou Lose")
    self.master.after(100, self.flip_yes_no)
    self.master.after(2000, self.bad_end)

  def leave(self):
    self.timer = 9000
    self.time_display.grid_forget()
    for x in range(len(self.check_ques) - 1, -1, -1):
      if self.check_ques[x] == True:
        self.last_ques = x
        break
    self.label_question.config(
        text=
        f"You Got To Question {self.last_ques+1}\n\nYou Get To Walk Away With ${self.player_money}"
    )
    if self.r_u_sure.cget("text") == "Will You Lock That In?":
      self.r_u_sure_for_get()
    self.button_del()
    self.des = True
    self.master.after(3000, self.master.destroy)

  def start_game(self):

    self.start_button.config(self.start_button.grid_forget())
    self.ques_1()

  def ques_1(self):
    self.game_started = True
    self.check_ques[0] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(text="What is the capital of France?")
      self.button_1.config(
          text="Paris",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_1.grid(row=4, column=0)
      self.button_2.config(
          text="London",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.grid(row=4, column=2)
      self.button_3.config(
          text="Berlin",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.grid(row=6, column=0)
      self.button_4.config(
          text="Madrid",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.grid(row=6, column=2)
    else:
      self.label_question.config(text="What is the capital of Great Britain?")
      self.button_1.config(
          text="Paris",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_1.grid(row=4, column=0)
      self.button_2.config(
          text="London",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_2.grid(row=4, column=2)
      self.button_3.config(
          text="Berlin",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.grid(row=6, column=0)
      self.button_4.config(
          text="Madrid",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.grid(row=6, column=2)

    self.time_display.grid(row=5, column=1)

    self.help_button.grid(row=0, column=3)

    self.leave_button.grid(row=8, column=3)

    self.timer_upd()

  def ques_2(self):
    self.check_ques[1] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(text="Who created the painting 'Mona Lisa'?")
      self.button_1.config(
          text="Vincent Van Gogh",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Leonardo Da Vinci",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Pablo Picasso",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Michelangelo",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text="Which classical piece begins with 'DaDaDaDum'")
      self.button_1.config(
          text="Toccata and Fugue in D Minor",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Für Elise",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Beethoven Symphony No.5",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Moonlight Sonata",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_3(self):
    self.check_ques[2] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(text="The Chemical Symbol for Iron is...")
      self.button_1.config(
          text="Ir", command=lambda: [self.wrng_r_u_sure(),
                                      self.butt_dis()])
      self.button_2.config(
          text="Ag", command=lambda: [self.wrng_r_u_sure(),
                                      self.butt_dis()])
      self.button_3.config(
          text="Au", command=lambda: [self.wrng_r_u_sure(),
                                      self.butt_dis()])
      self.button_4.config(
          text="Fe", command=lambda: [self.corr_r_u_sure(),
                                      self.butt_dis()])
    else:
      self.label_question.config(text="The Chemical Symbol for Gold is...")
      self.button_1.config(
          text="Au", command=lambda: [self.corr_r_u_sure(),
                                      self.butt_dis()])
      self.button_2.config(
          text="Fe", command=lambda: [self.wrng_r_u_sure(),
                                      self.butt_dis()])
      self.button_3.config(
          text="Ag", command=lambda: [self.wrng_r_u_sure(),
                                      self.butt_dis()])
      self.button_4.config(
          text="Ir", command=lambda: [self.wrng_r_u_sure(),
                                      self.butt_dis()])

    self.timer_upd()

  def ques_4(self):
    self.check_ques[3] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(
          text=
          "What was the name of the Spanish waiter in the TV sitcom 'Fawlty Towers'?"
      )
      self.button_1.config(
          text="Alejandro",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Pedro",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Alfonso",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Manuel",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text=
          "Which former Beatle narrated the TV adventures of Thomas the Tank Engine?"
      )
      self.button_1.config(
          text="Ringo Starr",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="John Lennon",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="George Harrison",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Paul McCartney",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_5(self):
    self.check_ques[4] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(
          text="Queen Anne was the daughter of which English Monarch?")
      self.button_1.config(
          text="Henry VIII",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Victoria",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="William I",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="James II",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text=
          "In Doctor Who, what was the signature look of the fourth Doctor, as portrayed by Tom Baker?"
      )
      self.button_1.config(
          text="Pinstripe suit and trainers",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Wide-brimmed hat and extra long scarf",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Cape, velvet jacket and frilly shirt",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Bow-tie, braces and tweed jacket",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_6(self):
    self.check_ques[5] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(
          text="Which king was married to Eleanor of Aquitaine?")
      self.button_1.config(
          text="Henry I",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Henry II",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Richard I",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Henry IV",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text=
          "At the closest point, which island group is only 50 miles south-east of the coast of Florida?"
      )
      self.button_1.config(
          text="Bermuda",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="US Virgin Islands",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Turks and Caicos Islands",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Bahamas",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_7(self):
    self.check_ques[6] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(
          text=
          "Which Shakespeare play features the line 'Neither a borrower nor a lender be'?"
      )
      self.button_1.config(
          text="Othello",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="The Merchant of Venice",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Hamlet",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Macbeth",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text=
          "Which Shakespeare play features the line 'A man can die but once'?")
      self.button_1.config(
          text="Henry IV",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="A Midsummer Night's Dream",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Julius Caesar",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Hamlet",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_8(self):
    self.check_ques[7] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(text="Where would a 'peruke' be worn?")
      self.button_1.config(
          text="Around the neck",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="On the wrist",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="On the head",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Around the waist",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text=
          "Obstetrics is a branch of medicine particularly concerned with what?"
      )
      self.button_1.config(
          text="Childbirth",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Old Age",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Heart Conditions",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Broken Bones",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_9(self):
    self.check_ques[8] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(
          text=
          "Which of these islands was ruled by Britain from 1815 until 1864?")
      self.button_1.config(
          text="Corfu",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Cyprus",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Crete",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Corsica",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text="In which palace was Queen Elizabeth I born?")
      self.button_1.config(
          text="Hampton Court",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Kensington",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Richmond",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Greenwich",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def ques_10(self):
    self.check_ques[9] = True
    if random.randint(1, 2) == 1:
      self.label_question.config(
          text=
          "In 1718, which pirate died in battle off the coast of what is now North Carolina?"
      )
      self.button_1.config(
          text="Bartholomew Roberts",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="Blackbeard",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="Calico Jack",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="Captain Kidd",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
    else:
      self.label_question.config(
          text=
          "Who is the only British politician to have held all four 'Great Offices of State' at some point during their career?"
      )
      self.button_1.config(
          text="Harold Wilson",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_2.config(
          text="David Lloyd George",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])
      self.button_3.config(
          text="James Callaghan",
          command=lambda: [self.corr_r_u_sure(),
                           self.butt_dis()])
      self.button_4.config(
          text="John Major",
          command=lambda: [self.wrng_r_u_sure(),
                           self.butt_dis()])

    self.timer_upd()

  def corr_r_u_sure(self):
    self.r_u_sure.config(text="Will You Lock That In?")
    self.r_u_sure.grid(row=8, column=0, columnspan=5)
    self.button_yes = Button(
        self.master,
        text="Yes",
        command=lambda: [self.butt_nor(), self.next_ques()],
        highlightbackground='yellow',
        fg='white',
        bg='green',
        font=('Elephant', 10, 'bold'))
    self.button_yes.grid(row=9, column=0)
    self.button_no = Button(
        self.master,
        text="No",
        command=lambda: [self.butt_nor(),
                         self.r_u_sure_for_get()],
        highlightbackground='yellow',
        fg='white',
        bg='red',
        font=('Elephant', 10, 'bold'))
    self.button_no.grid(row=9, column=2)

  def wrng_r_u_sure(self):
    self.r_u_sure.config(text="Will You Lock That In?")
    self.r_u_sure.grid(row=8, column=0, columnspan=5)
    self.button_yes = Button(
        self.master,
        text="Yes",
        command=lambda: [self.butt_nor(
        ), self.bad_end(), self.flip_yes_no()],
        highlightbackground='yellow',
        fg='white',
        bg='green',
        font=('Elephant', 10, 'bold'))
    self.button_yes.grid(row=9, column=0)
    self.button_no = Button(
        self.master,
        text="No",
        command=lambda: [self.butt_nor(),
                         self.r_u_sure_for_get()],
        highlightbackground='yellow',
        fg='white',
        bg='red',
        font=('Elephant', 10, 'bold'))
    self.button_no.grid(row=9, column=2)

  def r_u_sure_for_get(self):
    self.r_u_sure.config(text="")
    self.r_u_sure.grid_forget()
    self.button_yes.grid_forget()
    self.button_no.grid_forget()

  def flip_yes_no(self):
    for x in range(len(self.check_ques) - 1, -1, -1):
      if self.check_ques[x] == True:
        self.check_ques[x] = False
        break

  def bad_end(self):

    self.des = True

    if self.checkpoint_1 == False and self.checkpoint_2 == False and self.checkpoint_3 == False:
      if self.r_u_sure.cget("text") == "Will You Lock That In?":
        self.r_u_sure_for_get()
      self.player_money = 0
      self.money_display.config(text=f"Money: {self.player_money}")
      self.label_question.config(
          text=
          f"You lost! \nYou didn't pass any checkpoints so you keep ${self.player_money}. \nBetter luck next time!",
          wraplength=300)
      self.button_del()
      self.master.after(3000, self.master.destroy)

    elif self.checkpoint_1 == True and self.checkpoint_2 == False and self.checkpoint_3 == False:
      if self.r_u_sure.cget("text") == "Will You Lock That In?":
        self.r_u_sure_for_get()
      self.player_money = 1000
      self.money_display.config(text=f"Money: {self.player_money}")
      self.label_question.config(
          text=
          f"You lost! \nYou get to keep ${self.player_money} for passing the first checkpoint! \nBetter luck next time!",
          wraplength=300)
      self.button_del()
      self.master.after(3000, self.master.destroy)

    elif self.checkpoint_1 == True and self.checkpoint_2 == True and self.checkpoint_3 == False:
      if self.r_u_sure.cget("text") == "Will You Lock That In?":
        self.r_u_sure_for_get()
      self.player_money = 10000
      self.money_display.config(text=f"Money: {self.player_money}")
      self.label_question.config(
          text=
          f"You lost! \nYou get to keep ${self.player_money} for passing the second checkpoint! \nBetter luck next time!",
          wraplength=300)
      self.button_del()
      self.master.after(3000, self.master.destroy)

    elif self.checkpoint_1 == True and self.checkpoint_2 == True and self.checkpoint_3 == True:
      if self.r_u_sure.cget("text") == "Will You Lock That In?":
        self.r_u_sure_for_get()
      self.player_money = 50000
      self.money_display.config(text=f"Money: {self.player_money}")
      self.label_question.config(
          text=
          f"You lost! \nYou get to keep ${self.player_money} for passing the third checkpoint! \nBetter luck next time!",
          wraplength=300)
      self.button_del()
      self.master.after(3000, self.master.destroy)

  def next_ques(self):
    if self.r_u_sure.cget("text") == "Will You Lock That In?":
      self.r_u_sure_for_get()

    if self.time_display['fg'] == 'red':
      self.time_display['fg'] = 'white'

    if self.check_ques[9] == True:

      self.des = True
      self.player_money += self.mon[9]
      self.money_display.config(text=f"Money: ${self.player_money}")
      self.win()

    elif self.check_ques[8] == True:
      self.timer = 60
      self.checkpoint_3 = True
      self.check.config(text="Checkpoint: ★ ★ ★")
      if self.skip_ques != True:
        self.player_money += self.mon[8]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_10()

    elif self.check_ques[7] == True:
      self.timer = 45
      if self.skip_ques != True:
        self.player_money += self.mon[7]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_9()

    elif self.check_ques[6] == True:
      self.timer = 45
      if self.skip_ques != True:
        self.player_money += self.mon[6]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_8()

    elif self.check_ques[5] == True:
      self.timer = 45
      self.checkpoint_2 = True
      self.check.config(text="Checkpoint: ★ ★ ☆")
      if self.skip_ques != True:
        self.player_money += self.mon[5]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_7()

    elif self.check_ques[4] == True:
      self.timer = 30
      if self.skip_ques != True:
        self.player_money += self.mon[4]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_6()

    elif self.check_ques[3] == True:
      self.timer = 30
      if self.skip_ques != True:
        self.player_money += self.mon[3]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_5()

    elif self.check_ques[2] == True:
      self.timer = 30
      self.checkpoint_1 = True
      self.check.config(text="Checkpoint: ★ ☆ ☆")
      if self.skip_ques != True:
        self.player_money += self.mon[2]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_4()

    elif self.check_ques[1] == True:
      self.timer = 15
      if self.skip_ques != True:
        self.player_money += self.mon[1]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_3()

    elif self.check_ques[0] == True:
      self.timer = 15
      if self.skip_ques != True:
        self.player_money += self.mon[0]
        self.money_display.config(text=f"Money: ${self.player_money}")
      self.ques_2()

  def win(self):
    self.label_question.config(text="You won! Congratulations!")
    self.time_display.grid_forget()
    self.button_del()
    self.des = True
    self.master.after(3000, self.master.destroy)


root = Tk()
my_gui = Millionaire(root)
root.mainloop()
