import time,copy,random,pygame,sys

black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
gray = [100,100,100]
blue = [0,0,255]

piece_colors = {
	2: [255,0,0],
	3: [0,255,0],
	4: [0,0,255],
	5: [255,255,0],
	6: [255,0,255],
	7: [0,255,255],
	8: [160,160,160]
	}

# all the different states for each of the 7 pieces. used http://www.colinfahey.com/tetris/tetris_diagram_pieces_orientations_new.jpg to determine orientations
o_states = [ [ [0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0] ] ]
i_states = [ [ [0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0] ], [ [0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0] ] ]
s_states = [ [ [0,0,0,0],[0,0,1,1],[0,1,1,0],[0,0,0,0] ], [ [0,0,1,0],[0,0,1,1],[0,0,0,1],[0,0,0,0] ] ]
z_states = [ [ [0,0,0,0],[0,1,1,0],[0,0,1,1],[0,0,0,0] ], [ [0,0,0,1],[0,0,1,1],[0,0,1,0],[0,0,0,0] ] ]
l_states = [ [ [0,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,0,0] ], [ [0,0,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,0] ], [ [0,0,0,1],[0,1,1,1],[0,0,0,0],[0,0,0,0] ], [ [0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0] ] ]
j_states = [ [ [0,0,0,0],[0,1,1,1],[0,0,0,1],[0,0,0,0] ], [ [0,0,1,1],[0,0,1,0],[0,0,1,0],[0,0,0,0] ], [ [0,1,0,0],[0,1,1,1],[0,0,0,0],[0,0,0,0] ], [ [0,0,1,0],[0,0,1,0],[0,1,1,0],[0,0,0,0] ] ]
t_states = [ [ [0,0,0,0],[0,1,1,1],[0,0,1,0],[0,0,0,0] ], [ [0,0,1,0],[0,0,1,1],[0,0,1,0],[0,0,0,0] ], [ [0,0,1,0],[0,1,1,1],[0,0,0,0],[0,0,0,0] ], [ [0,0,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0] ] ]

tetrominoes = {
	0: o_states,
	1: i_states,
	2: s_states,
	3: z_states,
	4: l_states,
	5: j_states,
	6: t_states
	}

board = [
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1]
	]

class Tetromino():
	def __init__(self):
		self.piece = random.choice(tetrominoes.keys())
		self.next_piece = random.choice(tetrominoes.keys())
		self.rotation = 0
		self.top = 0
		self.left = 4
		self.color = random.randint(2,8)
	
	def display(self, location):
		if location == 0:
			for row in range(4):
				for col in range(4):
					if tetrominoes[self.piece][self.rotation][row][col]:
						pygame.draw.rect(screen, piece_colors[self.color],((self.left * block_size) + (col * block_size), (self.top * block_size) + (row * block_size), block_size-2, block_size-2), 3)
				#else:
				#	pygame.draw.rect(screen, white,((grid_col * block_size) + (col * block_size), (grid_row * block_size) + (row * block_size), block_size-2, block_size-2), 3)
		else:
			for row in range(4):
				for col in range(4):
					if tetrominoes[self.piece][self.rotation][row][col]:
						pygame.draw.rect(screen, piece_colors[self.color],(300+(col*block_size), 10+(row*block_size), block_size-2, block_size-2),3)

#	def new_piece(self):
#		self.piece = self.next_piece
#		self.rotation = 0
#		self.top = 0
#		self.left = 4
#		self.color = random.randint(2,8)
#		self.next_piece = random.choice(tetrominoes.keys())
		
	def rotate(self):
		next_rotation = self.rotation + 1
		next_rotation %= len(tetrominoes[self.piece])
		
		if not self.iscollision(0,0, next_rotation):
			self.rotation += 1
			self.rotation %= len(tetrominoes[self.piece])
		

	#potentially move the block in 1 of 3 directions. updates the master array that holds the board information
	def move(self, direction):
		#do not affect the board by changing the array. only the display needs to be updated constantly. the array will be updated once the piece lands. 
		if direction == 'down':
			if not self.iscollision(1,0):
				self.top += 1
			else:
				self.snaptoboard()
				piece_swap()
		elif direction == 'left':
			if not self.iscollision(0,-1):
				self.left -= 1
		elif direction == 'right':
			if not self.iscollision(0,1):
				self.left += 1
	
	#collision detection algorithm. returns whether a collision is detected or not			
	#current_row/col are the coordinates for the topleft of the piece	
	def iscollision(self,move_row, move_col, rotation_change = None):
		
		#loops through the piece array and compares it to the board array, if a True from piece would move to a True from board, then a collision is detected
		for row in range(4):
			for col in range(4):
				#current_row+row gets to the piece super imposed on the board, +move checks for the next move, be it 1 space or more. in this case, only interested in 1 space
				if tetrominoes[self.piece][rotation_change if rotation_change is not None else self.rotation][row][col] and board[self.top+row+move_row][self.left+col+move_col]:
					return True
		return False

	#once a downward collision is detected, add the piece to the board array so we can check for row clearing as well as rendering the full board
	def snaptoboard(self):
		for row in range(4):
			for col in range(4):
				if tetrominoes[self.piece][self.rotation][row][col]:
					board[self.top+row][self.left+col] = self.color
		clear_rows()
		
		for col in range(1,11):
			if board[1][col]:
				sys.exit(0)
							
#display the board, using the array that stores the variables for the game
#boundaries are listed as 1, 0 is an open spot, and the color of the piece replaces the 0s to dictate where the pieces are
def draw_board():
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] > 1:
				pygame.draw.rect(screen, piece_colors[board[row][col]],((col * block_size) , (row * block_size), block_size-2, block_size-2), 3)

#check for a full row. if a full row is found, delete it, add the rows, determine level and drop the pieces
def clear_rows():
	global complete_rows
	global level
	global drop_speed
	
	rows = 17
	
	while rows >= 1:
		complete_row = True
		for cols in range(1,11):
			if not board[rows][cols]:
				complete_row = False
				break
		if complete_row:
			new_board = copy.deepcopy(board)
			complete_rows += 1
			if (complete_rows % 10) == 0:
				level += 1
				drop_speed -= 50

			for new_rows in range(1, rows):
				board[new_rows + 1] = new_board[new_rows]
		else:
			rows -= 1

#swaps the piece displayed in the Next location for the active piece and creates a new piece
def piece_swap():
	global active_piece
	global new_piece
	
	active_piece = new_piece
	new_piece = Tetromino()
	
	
top = 20
left = 20
block_size = 25
level = 1
drop_speed = 1000
lateral_speed = 150
complete_rows = 0
			
#pygame initialization
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)			
pygame.mixer.music.load('tetris.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.display.set_caption("Poor Man's Tetris")
pygame.time.set_timer(pygame.USEREVENT + 1, drop_speed)

size = [600,600]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
active_piece = Tetromino()
new_piece = Tetromino()

while done == False:
	#if not pygame.mixer.music.get_busy():
	#	pygame.mixer.music.play()
	
	for event in pygame.event.get():
	
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.USEREVENT + 1: active_piece.move('down')
		elif event.type == pygame.USEREVENT + 2: active_piece.move('left')
		elif event.type == pygame.USEREVENT + 3: active_piece.move('right')
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				active_piece.rotate()
			elif event.key == pygame.K_DOWN:
				pygame.time.set_timer(pygame.USEREVENT + 1, drop_speed / 10)
			elif event.key == pygame.K_LEFT:
				active_piece.move('left')
				pygame.time.set_timer(pygame.USEREVENT + 2, lateral_speed)
			elif event.key == pygame.K_RIGHT:
				active_piece.move('right')
				pygame.time.set_timer(pygame.USEREVENT + 3, lateral_speed)
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				pygame.time.set_timer(pygame.USEREVENT + 1, drop_speed)
			if event.key == pygame.K_LEFT:
				pygame.time.set_timer(pygame.USEREVENT + 2, 0)
			if event.key == pygame.K_RIGHT:
				pygame.time.set_timer(pygame.USEREVENT + 3, 0)
				
		
	screen.fill(black)
	screen.blit(screen, (320, 240))
	font = pygame.font.Font(None, 28)
	rows = font.render("Rows cleared: " + str(complete_rows), True, white)
	level_display = font.render("Level: " + str(level), True, white)
	screen.blit(rows, [320,320])
	screen.blit(level_display, [320,350])
	
	draw_board()
	active_piece.display(0)
	new_piece.display(1)
	pygame.draw.lines(screen, gray, False, [(10,10),(10, 460), (10,460),(290,460), (290,460),(290,10)],3)
	
	clock.tick(20)
	
	pygame.display.flip()
