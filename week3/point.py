class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y 

    def distance(self, p: "Point"):
        a = (p.x-self.x)**2
        b = (p.y-self.y)**2

        return (a+b)**(0.5)