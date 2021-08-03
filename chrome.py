from turtle import*

setup(500,500)
bgcolor('white')
speed(5)

def middle():
	   color('#0099FF','#0099FF')
	   penup()
	   goto(100,100)
	   pendown()
	   begin_fill()
	   setheading(108)
	   circle(152,360)
	   end_fill()

def red():
	   color('#CC0033','#CC0033')
	   penup()
	   goto(100,100)
	   pendown()
	   begin_fill()
	   goto(200,110)
	   setheading(100)
	   circle(250,120)
	   goto(-200,50)
	   setheading(-90)
	   circle(152,-150)
	   end_fill()
	   
def green():
	   color('#019934','#019934')
	   penup()
	   goto(-200,50)
	   pendown()
	   begin_fill()
	   goto(-208,260)
	   setheading(220)
	   circle(250,120)
	   goto(-50,-97)
	   setheading(-1)
	   circle(152,-100)
	   goto(-200,50)
	   end_fill()
	   
def yellow():
	   color('#FDD20A','#FDD20A' )
	   penup()
	   goto(-50,-97)
	   pendown()
	   begin_fill()
	   goto(-135,-165)
	   setheading(340)
	   circle(250,150)
	   goto(100,100)
	   setheading(108)
	   circle(152,-115)
	   goto(-50,-97)
	   end_fill()
	   
middle()
red()
green()
yellow()

done()
	   
