from tools import *

font_digit = None
font_digit1 = None


def setup():
    global font_digit, font_digit1
    size(1200, 800)
    font_digit = loadFont("Cambria-110.vlw")
    font_digit1 = loadFont("Cambria-170.vlw")

a = 7    
def draw():
    background(0, 0, 70)
    
    global a
    a+= 2
    fill(0, map(a, 0, 800, 0, 255), 0)
    noStroke()
    if a > width:
        a = 0

    f = 5
    for i in range(300):
        for j in range(300):
            fill(0, i * 255 / 300, j * 255 / 300)
            noStroke()
            rect(0 + i * (f + 0), 0 + j * (f + 0), f, f)

    draw_number(second(), 490, 400, font_digit1)
    delim(150, 250, font_digit)
    draw_number(hour(), 445, 590, font_digit, color(255, 0, 0))
    draw_number(minute(), 595, 590, font_digit, color(0, 0, 255))
    

    noFill()
    strokeWeight(30)

    stroke(255, 0, 0)
    arc(580, 350, 600, 600, PI * 155 / 225, map(second(), 0, 59, PI * 155 / 225, PI * 360 / 157))
    stroke(0, 150, 0)
    arc(580, 350, 490, 490,PI * 155 / 210, map(minute(), 0, 59, PI * 155 / 210, PI * 360 / 160))
    stroke(0, 255, 255)
    arc(580, 350, 370, 370,PI * 155 / 210, map(hour(), 0, 24, PI * 155 / 210, PI * 360 / 160))
    
    
   
        
        
        
