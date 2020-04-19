import pygame
import random
from pygame import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("ice crean run")
tempo = pygame.time.Clock()
largura=600
altura=150
rosa = (255,105,180)
azul = (0,0,255)
carmesim = (220, 20, 60)
branco = (255,255,255)
preto = (0,0,0)
fonte = pygame.font.get_default_font()
fonte_jn= pygame.font.SysFont(fonte, 25)
bg_x = 0
fundo = pygame.display.set_mode((largura, altura))
class dinossauro():
    
    def __init__(self, pos_x, pos_y):
        self.pos_x= 66
        self.pos_y= 107
        self.pulo = False
        self.puloconta = 10

    def draw(self):
        pygame.draw.rect(fundo, azul, [self.pos_x, self.pos_y,20,-20])

    def pular(self):
        if self.pulo:
          if self.puloconta >= -10:
              neg = -1 if self.puloconta < 0 else 1
              self.pos_y -= (self.puloconta ** 2) * 0.1 * neg
              self.puloconta -= 1
          else:
              self.pulo = False
              self.puloconta = 10
class cactu():
    def __init__(self, pos_c, pos_z):
        self.pos_c = 600
        self.pos_z = 107
    def draw(self):
        pygame.draw.rect(fundo, carmesim, [self.pos_c, self.pos_z,20, -40],)
    def anda(self):
        if self.pos_c >= largura:
            self.pos_c = 0
        if self.pos_c <= 0:
            self.pos_c = largura
            
        self.pos_c-=2
def jogo(dinossauro, cactu):

    
   
    

    jogar = True
    fim_de_jogo = False
    fundo = pygame.display.set_mode((largura, altura))
    
    dino = dinossauro(66,107)
    cact = cactu(600, 107)
    while jogar:
        dt = tempo.tick(60)
        while fim_de_jogo:
            fundo.fill(rosa)
            msg = ("Precione S para jogar novamente")
            msg2 = ("Precione N para sair do jogo")
            texto = fonte_jn.render(msg, True, preto)
            texto2 = fonte_jn.render(msg2, True, preto)
            fundo.blit(texto,(200,30))
            fundo.blit(texto2,(200,55))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogar = False
                    fim_de_jogo = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        jogo(dinossauro, cactu)
                    if event.key == pygame.K_n:
                        jogar = False
                        fim_de_jogo = False
 
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogar = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.pulo = True
            

        
        fundo.fill(rosa)
        msg3 = ("Precione espaço para começar")
        texto3 = fonte_jn.render(msg3, True, preto)
        fundo.blit(texto3,(100,30))
        pygame.draw.line(fundo,branco,[0,109],[600,109],7)
        
        
        
        
        dino.pular()
        dino.draw()
        cact.draw()
        cact.anda()
        pygame.display.update()    
    pygame.quit()


jogo(dinossauro, cactu)




