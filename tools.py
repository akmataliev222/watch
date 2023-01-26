def convert_to_digit_format(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)

def draw_number(number, x, y, font_digit, clr=color(0, 255, 0)): 
    fill(clr)
    textSize(120)
    textFont(font_digit)
    number = convert_to_digit_format(number)
    text(number, x, y)
    
def delim(x, y, font_digit):
    textSize(20)
    textFont(font_digit)
    text(":", 565, 575)
    
    noFill()
    stroke(30, 0, 0, 50)
    arc(580, 350, 600, 600, PI * 155 / 225, PI * 360 / 157)
    arc(580, 350, 490, 490, PI * 155 / 210, PI * 360 / 160)
    arc(580, 350, 370, 370, PI * 155 / 210, PI * 360 / 160)
    
