import tkinter as tk


def init():
	global window, root, my_ball

	root = tk.Tk()

	window_width = 600
	window_height = 500
	window_color = "#eeeeee"

	window = tk.Canvas(root, bg = window_color, width = window_width, height = window_height)
	window.pack()

	ball_width = 75
	ball_x1 = 50
	ball_y1 = window_height - 50 - ball_width 

	my_ball = Ball(ball_x1, ball_y1, ball_width, "my_ball", fill_color = "red")

	root.bind('<Key>', handler_move)


class Ball:
	def __init__(self, x1, y1, width, tags, fill_color = "black", outline_color = None):
		self.limit_points = [x1, y1, x1 + width, y1 + width]
		self.fill_color = fill_color
		self.tags = tags

		if outline_color == None:
			self.outline_color = fill_color
		else:
			self.outline_color = outline_color


		self.draw()


	def draw(self):
		window.create_oval(
			self.limit_points, 
			tags = self.tags, 
			outline = self.outline_color, 
			fill = self.fill_color
		)


	def move(self, direct, speed):
		if direct == "left":
			self.limit_points[0] -= speed
			self.limit_points[2] -= speed
		elif direct == "right":
			self.limit_points[0] += speed
			self.limit_points[2] += speed


def handler_move(event):
	window.delete(my_ball.tags)
	speed = 5

	if event.char == "d":
		my_ball.move("right", speed)
		my_ball.draw()
	elif event.char == "a":
		my_ball.move("left", speed)
		my_ball.draw()
	else:
		my_ball.draw()




if __name__ == '__main__':
	init()
	root.mainloop()