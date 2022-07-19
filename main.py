import turtle as t
from game import Master

TOP = -120, 300
M = Master()
screen = t.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)


while M.score != M.num_states and not M.should_quit:
    answer_state = t.textinput(M.show_score + " States Correct", "Type the name of a state.")
    if answer_state is None:
        M.should_quit = True
    else:
        M.check_guess(answer_state.title())

end_message_font = ("Consolas", 24, "bold")

if M.score == 50:
    M.create_state_name("Congratulations!", TOP[0], TOP[1], end_message_font)
else:
    M.create_state_name("Final Score:\n" + M.show_score + " states", TOP[0], TOP[1], end_message_font)

t.mainloop()
