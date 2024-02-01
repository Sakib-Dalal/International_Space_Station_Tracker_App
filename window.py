import turtle
import API_setup
import iss_pos


class Graphics:
    def __init__(self):
        self.iss_poss = iss_pos.SetPos()
        map_image = "./image_data/map1.gif"
        self.iss_screen = turtle.Screen()
        self.iss_screen.title("ISS APP")
        self.iss_screen.setup(width=1200, height=720)
        self.iss_screen.setworldcoordinates(-180, -90, 180, 90)

        self.iss_screen.register_shape("./image_data/iss_logo.gif")

        self.iss_screen.addshape(map_image)
        turtle.Turtle(map_image)

        self.iss = turtle.Turtle()
        self.iss.penup()
        self.iss.shape("./image_data/iss_logo.gif")

    def refresh_iss_pos(self):
        self.iss_poss.set_cor()
        iss_data = API_setup.IssApi()
        x = iss_data.generate()[0]
        y = iss_data.generate()[1]
        self.iss.color("#00BFFF")
        self.iss.goto(x=float(x) - 2, y=float(y) - 13)
        self.iss.pendown()
        self.iss_poss.clear_data()