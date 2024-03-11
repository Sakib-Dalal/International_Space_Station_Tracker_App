import turtle
import API_setup

ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class SetPos:
    def __init__(self):
        self.lat = None
        self.long = None
        self.latitude = None
        self.longitude = None

    def set_cor(self):
        data = API_setup.IssApi()
        self.long = data.generate()[0]
        self.lat = data.generate()[1]

        self.longitude = turtle.Turtle()
        self.longitude.hideturtle()
        self.longitude.penup()
        self.longitude.setpos(x=-146, y=-85)

        self.latitude = turtle.Turtle()
        self.latitude.hideturtle()
        self.latitude.penup()
        self.latitude.setpos(x=-150, y=-90)

        self.longitude.pendown()
        self.longitude.color("white")
        self.longitude.write(f"Longitude:{self.long}", False, ALIGN, FONT)

        self.longitude.pendown()
        self.latitude.color("white")
        self.latitude.write(f"Latitude:{self.lat}", False, ALIGN, FONT)

    def clear_data(self):
        self.longitude.clear()
        self.latitude.clear()