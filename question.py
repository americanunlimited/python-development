
import turtle
turtle.shape("turtle")
daddy_paying_will = turtle.textinput("Answer Question", "Is Daddy paying me or has me in the will? Enter Yes or No.\n")
if daddy_paying_will == "Yes":
         turtle.write("LIES\nALTERNATIVE FACTS\nFAKE NEWS\nSO SAD\n\nClick window to exit.", align="center", font=("Comic Sans MS", 32,))
         turtle.exitonclick()
else:
         turtle.write("I'm Fucked\n\nClick window to exit.", align="center", font=("Comic Sans MS", 32,))
         turtle.exitonclick()
