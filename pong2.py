from tkinter import *
import time

class jogo(object):
	"""docstring for jogo"""
	def __init__(self):
		self.root = Tk()
		self.root.title('Pong 1.0')
		self.canvas_width = 700
		self.canvas_heigh = 500
		self.canvas = Canvas(self.root, width = self.canvas_width, heigh = self.canvas_heigh, bg = 'black')
		self.canvas.pack()
		self.button = Button(self.root, text = 'Start!', command = self.start)
		self.root.focus_set()
		self.button.pack()
		self.pontos = 0
		self.placar1 = Label(self.root,text = self.pontos)
		self.placar1.pack(side = LEFT)
		self.pontos2 = 0
		self.placar2 = Label(self.root, text = self.pontos2)
		self.canvas.create_rectangle(348,0,352,500, fill = 'white', outline = 'white')
		self.placar2.pack(side = RIGHT)
		self.newGame()
		self.root.mainloop()

	def newGame(self):
		#self.bola = self.canvas.create_oval(300,250,330,280, fill = 'white', outline = 'white', tag = 'bola')
		self.placar1['text'] = self.pontos
		self.placar2['text'] = self.pontos2
		self.b_x = 300
		self.b_y = 250
		self.b_vx = self.b_vy = 5
		self.v_player = 35
		self.gol = self.canvas.create_rectangle(0,0,5,self.canvas_heigh, fill = 'black', tag = 'gol')
		self.gol2 = self.canvas.create_rectangle(695,0,700,self.canvas_heigh, fill = 'black', tag = 'gol2')
		self.campo()
		self.root.bind('<Up>',self.move_playerUp)
		self.root.bind('<Down>',self.move_playerDown)
		self.root.bind('<F11>',self.move_player2Up)
		self.root.bind('<F12>',self.move_player2Down)
		self.jogando = True

	def campo(self):
		#time.sleep(2)
		self.bola = self.canvas.create_oval(self.b_x,self.b_y,self.b_x+30,self.b_y+30, fill = 'white', tag = 'bola')
		self.player = self.canvas.create_rectangle(5,self.canvas_heigh/2 - 50, 15,self.canvas_heigh/2 + 50, fill = 'white', tag = 'player')
		self.player2 = self.canvas.create_rectangle(685,self.canvas_heigh/2 - 50, 695,self.canvas_heigh/2 + 50, fill = 'white', tag = 'player2')
	def start(self):
		if self.jogando:
			self.move()
			self.colisao()
			self.ponto()
			self.ponto2()
			self.root.after(25,self.start)
		else:
			print('teste')
	def move(self):
			
			self.canvas.move('bola',self.b_vx,self.b_vy)
			self.b_x = self.b_x + self.b_vx
			self.b_y = self.b_y + self.b_vy
			if self.b_y >= self.canvas_heigh - 30 or self.b_y < 0:
				self.b_vy *= -1
			if self.b_x >= self.canvas_width - 30 or self.b_x < 0:
				self.b_vx *= -1
	def move_playerUp(self,event):
		self.canvas.move('player',0,-self.v_player)
	def move_playerDown(self,event):
		self.canvas.move('player',0,self.v_player)
	def move_player2Up(self,event):
		self.canvas.move('player2',0,-self.v_player)
	def move_player2Down(self,event):
		self.canvas.move('player2',0,self.v_player)

	def colisao(self):
		bola = self.canvas.find_withtag('bola')
		player = self.canvas.find_withtag('player')
		player2 = self.canvas.find_withtag('player2')

		x1,y1,x2,y2 = self.canvas.bbox(bola)
		overlap = self.canvas.find_overlapping(x1,y1,x2,y2)
		for ovr in overlap:
			if player[0] == ovr or player2[0] == ovr:
				self.b_vx *= -1
	def ponto(self):
		bola = self.canvas.find_withtag('bola')
		gol = self.canvas.find_withtag('gol')

		x1,y1,x2,y2 = self.canvas.bbox(bola)
		overlap = self.canvas.find_overlapping(x1+5,y1,x2+5,y2)
		for ovr in overlap:
			if gol[0] == ovr:
				self.canvas.itemconfig(self.bola, fill = 'red')
				self.pontos2 += 1
				time.sleep(2)
				self.delete_all()
				self.newGame()
	def ponto2(self):
		bola = self.canvas.find_withtag('bola')
		gol2 = self.canvas.find_withtag('gol2')

		x1,y1,x2,y2 = self.canvas.bbox(bola)
		overlap = self.canvas.find_overlapping(x1-5,y1,x2-5,y2)
		for ovr in overlap:
			if gol2[0] == ovr:
				self.canvas.itemconfig(self.bola, fill = 'red')
				self.pontos += 1
				time.sleep(2)
				self.delete_all()
				self.newGame()
	def delete_all(self):
		self.canvas.delete(self.bola)
		self.canvas.delete(self.player)
		self.canvas.delete(self.player2)
		
	


  		
if __name__ == '__main__':
	jogo()

