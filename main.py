import tkinter as tk


def init():
	global window, root, window_width, window_height

	root = tk.Tk()

	window_width = 600
	window_height = 500
	window_color = "#694a0d"

	window = tk.Canvas(root, bg = window_color, width = window_width, height = window_height)
	window.pack()


	game()


class Floor:
	def __init__(self, x1 ,y1, width, height, tags, fill_color = "#828282", outline_color = None):
		self.limit_points = [x1, y1, x1 + width, y1 + height]
		self.fill_color = fill_color
		self.tags = tags

		if outline_color == None:
			self.outline_color = fill_color
		else:
			self.outline_color = outline_color

		self.draw()



	def draw(self):
		window.create_rectangle(
			self.limit_points,
			tags = self.tags,
			fill = self.fill_color,
			outline = self.outline_color
		)


class Ball:
	def __init__(self, x1, y1, width, tags = None, fill_color = "black", outline_color = None):
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

	def jump(self):
		pass


def handler_move(event):
	window.delete(player.tags)
	speed = 5

	if event.char == "d":
		player.move("right", speed)
		player.draw()
	elif event.char == "a":
		player.move("left", speed)
		player.draw()
	else:
		player.draw()


def game():
	global player

	main_floor = Floor(0, 450, window_width, 50, tags = "main_floor",)
	left_ground = Floor(50, 250, 200, 50, tags = "left_ground",)
	right_ground = Floor(350, 250, 200, 50, tags = "right_ground",)


	player_width = 75
	player_x1 = 50
	player_y1 = window_height - 52 - player_width

	player = Ball(player_x1, player_y1, player_width, "player", fill_color = "#d6c52b")
	root.bind('<Key>', handler_move)




if __name__ == '__main__':
	init()
	root.mainloop()