import turtle as t

SNAKE_WIDTH = 20

class Snake:
    segments = []

    def __init__(self, size):
        for i in range(size):
            self.createsegment(self, -i*SNAKE_WIDTH, 0)
        self.head = self.segments[0]

    @staticmethod
    def createsegment(self, x, y):
        newSegment = t.Turtle("square")
        newSegment.pensize(SNAKE_WIDTH)
        newSegment.color("white")
        newSegment.penup()
        newSegment.degrees(360)
        newSegment.speed(0)
        newSegment.setposition((x,y))
        self.segments.append(newSegment)

    @staticmethod
    def updatesegments(segments):
        for i in range(len(segments) - 1, 0, -1):
            segments[i].setposition(segments[i-1].position())

    def grow(self):
        self.createsegment(self, 0, 0)

    def move_forward(self):
        self.updatesegments(self.segments)
        self.segments[0].forward(SNAKE_WIDTH)

    def hititself(self):
        for seg in self.segments[1:]:
            if seg.distance(self.segments[0].position()) < 10:
                return True
        return False

    def hitthewall(self):
        if self.head.xcor() > 280 or \
                self.head.xcor() < -280 or \
                self.head.ycor() > 280 or \
                self.head.ycor() < -280:
            return True
        return False

    def hitfood(self, foodposition):
        if self.head.distance(foodposition) <= 20:
            return True
        return False


    def turn_up(self):
        if self.segments[0].heading() != -90:
            self.segments[0].setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(-90)

    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

