import tkinter as tk


def init():
	global window, root, window_width, window_height

	window_width = 1000
	window_height = 700
	window_color = "#694a0d"

	root = tk.Tk()
	root.title('Exit the gungeon')

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


class Cube:
	def __init__(self, x1, y1, width, height, tags = None, fill_color = "black", outline_color = None):
		self.limit_points = [x1, y1, x1 + width, y1 + height]
		self.fill_color = fill_color
		self.tags = tags
		self.is_jump = False
		self.jump_is_down = False
		self.jump_height = 300
		self.grounds = []
		self.start_y = y1 + height
		self.is_fall = False

		if outline_color == None:
			self.outline_color = fill_color
		else:
			self.outline_color = outline_color


		self.draw()


	def draw(self):
		window.create_rectangle(
			self.limit_points, 
			tags = self.tags, 
			outline = self.outline_color, 
			fill = self.fill_color
		)


	def move(self, direct, speed):
		if direct == "left":
			window.delete(self.tags)

			self.limit_points[0] -= speed
			self.limit_points[2] -= speed

			self.draw()
		elif direct == "right":
			window.delete(self.tags)

			self.limit_points[0] += speed
			self.limit_points[2] += speed

			self.draw()
		elif direct == "up":
			window.delete(self.tags)

			self.limit_points[1] -= speed
			self.limit_points[3] -= speed

			self.draw()
		elif direct == "down":
			window.delete(self.tags)

			self.limit_points[1] += speed
			self.limit_points[3] += speed

			self.draw()


	def update_start_y(self):
		self.start_y = self.limit_points[3]

	def fall(self):
		if self.check_grounds():
			self.is_fall = False
			return 0

		self.move("down", 4)

		root.after(8, self.fall)


	def check_grounds(self):
		for ground in self.grounds:
				if (self.limit_points[3] >= ground.limit_points[1] - 1) and (self.limit_points[3] <= ground.limit_points[3]):
					b_x1 = self.limit_points[0]
					b_x2 = self.limit_points[2]
					g_x1 = ground.limit_points[0]
					g_x2 = ground.limit_points[2]
					if ((b_x1 >= g_x1) and (b_x1 <= g_x2)) or ((b_x2 >= g_x1) and (b_x2 <= g_x2)):
						return True

		return False

	def check_walls(self, left_wall, right_wall):
		if left_wall.limit_points[2] >= self.limit_points[0]:
			return "left"
		elif right_wall.limit_points[0] <= self.limit_points[2]:
			return "right"

		return None
		


	def jump(self):
		jump_speed = 8
		time_speed = 8	

		if (self.limit_points[3] > self.start_y - self.jump_height) and not self.jump_is_down:
			self.move("up", jump_speed)
		else:
			self.jump_is_down = True
			if self.check_grounds():
				self.is_jump = False
				self.jump_is_down = False
				return 0
			self.move("down", jump_speed)


		root.after(time_speed, self.jump)
			


def handler_move(event):
	speed = 8
	wall_side = player.check_walls(left_wall, right_wall)
	player.grounds = [main_floor, left_ground, right_ground]

	if event.char == "d":
		if wall_side != "right":
			player.move("right", speed)
			if not player.is_jump and not player.check_grounds():
				player.is_fall = True
				player.fall()
	elif event.char == "a":
		if wall_side != "left":	
			player.move("left", speed)
			if not player.is_jump and not player.check_grounds():
				player.is_fall = True
				player.fall()
	if event.char == " " and not (player.is_jump or player.is_fall):
		player.is_jump = True
		player.update_start_y()
		player.jump()



def game():
	global player, main_floor, left_ground, right_ground, right_wall, left_wall

	ground_height = 25
	ground_width = 200

	main_floor_height = 60

	mf_x = 0
	mf_y = window_height - main_floor_height + 10

	lg_x = ((window_width / 2) - ground_width) / 2 
	lg_y = mf_y - 200

	rg_x = lg_x + ground_width + ((window_width / 2) - ground_width)
	rg_y = mf_y - 200

	main_floor = Floor(mf_x, mf_y, window_width, main_floor_height, tags = "main_floor")
	left_ground = Floor(lg_x, lg_y, ground_width, ground_height, tags = "left_ground")
	right_ground = Floor(rg_x, rg_y, ground_width, ground_height, tags = "right_ground")

	left_wall = Floor(0, 0, 10, window_height, tags = "left_wall")
	right_wall = Floor(window_width - 5, 0, 10, window_height, tags = "right_wall")

	player_width = 75
	player_x1 = 50
	player_y1 = mf_y - player_width - 1

	player = Cube(player_x1, player_y1, player_width, player_width, "player", fill_color = "#d6c52b")
	root.bind('<Key>', handler_move)




if __name__ == '__main__':
	init()
	root.mainloop()