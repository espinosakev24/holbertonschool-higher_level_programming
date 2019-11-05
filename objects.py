import pygame as pg
from variables import *
from pygame.locals import *
import sys

class GameScreen():
	def __init__(self, wn, game):
		self.wn = wn
		self.game = game
		self.size = (WIDTH - 200) / GRID

	def update(self):
		for ev in pg.event.get():
			if ev.type == pg.KEYDOWN:
				if ev.key == K_ESCAPE:
					self.game.changeScreen(MenuScreen(self.wn, self.game))

	def render(self):
		pass
		#for a in range(d)

class Node():
	"""docstring for Node"""
	def __init__(self, face, pos, di):
		self.next = None
		self.prev = None

	def update():
		pass

	def render():
		pass
		

class Game():
	"""docstring for Screen"""
	def __init__(self, wn):
		self.screen = MenuScreen(wn, self)

	
	def update(self):
		self.screen.update()
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				pg.quit()
				sys.exit()
	def render(self):
		self.screen.render()
	def changeScreen(self, newscreen):
		self.screen = newscreen


class MenuScreen():
	def __init__(self, wn, game):
		""" Docstring
		"""
		size = Assets.font.size(TITLE)
		self.title = Text(Assets.font, TITLE, ((WIDTH / 2) - size[0] / 2, 50), wn, WHITE)
		self.btns = [Button(wn, None, (80, 200), PLAY), Button(wn, None, (80, 250), "CREDITS"), Button(wn, None, (80, 300), "EXIT")]
		self.idx = 0
		self.game = game
		self.wn = wn

	def update(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if ev.type == pg.KEYDOWN:
			
			#MENU CURSOR MOVMENT
				if ev.key == K_ESCAPE:
					pg.quit()
					sys.exit()
				if ev.key == K_UP:
					self.btns[self.idx].select = False
					self.idx -= 1
					if self.idx < 0:
						self.idx = len(self.btns) - 1
					self.btns[self.idx].select = True
				if ev.key == K_DOWN:
					self.btns[self.idx].select = False
					self.idx += 1
					if self.idx > len(self.btns) - 1:
						self.idx = 0
					self.btns[self.idx].select = True

			#PLAYBUTTON ACTION
				if ev.key == K_q:
					if self.idx == 0:
						self.game.changeScreen(GameScreen(self.wn, self.game))

	def render(self):
		for btn in self.btns:
			btn.render()			
		self.title.render()

class Button():
	def __init__(self, wn, action, pos, name):
		self.wn = wn
		self.action = action
		self.pos = pos
		self.name = name
		self.select = True if name == PLAY else False
		#positioning text of the button
		button_width = Assets.bNormal.get_rect()
		txt_width = Assets.font.size(name)
		text_position = (button_width.width / 2) - txt_width[0] / 2
		self.bText = Text(Assets.font, name, (text_position + pos[0], pos[1]), wn, TINNYRED)

	def update(self):
		pass


	def render(self):
		if self.select:
			self.wn.blit(Assets.bHlight, self.pos)
		else:
			self.wn.blit(Assets.bNormal, self.pos)
		self.bText.render()



class Text():
	""" docstring of text class
	"""

	def __init__(self, font, text, pos, wn, color):
		""" constructor function
		"""
		self.font = font
		self.text = text
		self.pos = pos
		self.wn = wn
		self.color = color

	def render(self):
		"""
		"""
		string = self.font.render(self.text, True, self.color)
		self.wn.blit(string, self.pos)
