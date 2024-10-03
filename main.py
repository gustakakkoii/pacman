import random
import pygame

pygame.init()

#Costante
AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0,0,255)
BRANCO = (255, 255, 255)
VELOCIDADE = 1

TAMANHO_TELA = 644

screen = pygame.display.set_mode((TAMANHO_TELA, TAMANHO_TELA),0)
class Cenario:
    def __init__(self, tamanho, pac):
        self.tamanho = tamanho
        self.pacman = pac
        self.matar = False
        self.pontos = 0
        self.fim = 0
        self.matriz = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
    [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
    [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
    [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
    [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
    [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
    [2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)

    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            cor = PRETO
            if coluna == 2:
                cor = AZUL
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho),0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2,y + self.tamanho/2), self.tamanho//10)
            if coluna == 3:
                cor = BRANCO
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho),0)
            if coluna == 4:
                pygame.draw.circle(tela, AMARELO, (x + self.tamanho/2,y + self.tamanho/2), self.tamanho//4)

    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao

        if (col > 0 and col <= 28) and (0 <= lin < 29):
            if self.matriz[lin][col] != 2 and self.matriz[lin][col] !=3:
                self.pacman.aceitar_movimento()
        fim = 0
        for e in (self.matriz):
            for a in e:
                if a == 1:
                    fim = fim + 1
        print(fim)
        if fim == 0:
            self.fim = 2
            


    
    def somar_pontos(self):
        linha = self.pacman.linha
        coluna = self.pacman.coluna
        if self.matriz[linha][coluna] == 1:
            self.matriz[linha][coluna] = 0
            self.pontos = self.pontos + 10
        if self.matriz[linha][coluna] == 4:
            self.matriz[linha][coluna] = 0
            self.pontos = self.pontos + 10
            self.matar = True
            self.pacman.cor = BRANCO

        
        

class Fantasmas:
    def __init__(self, tamanho_fantasma, pac, cenario):
        self.pacman = pac
        self.cenario = cenario
        self.tamanho = tamanho_fantasma

        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.cor = (self.r,self.g,self.b)

        self.raio = self.tamanho/2
        self.linha = random.randint(13, 15)
        self.coluna = random.randint(11, 16)
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.centro_x = 0
        self.centro_y = 0
        self.direcao = random.randint(1, 2)
        self.vel_x = VELOCIDADE
        self.vel_y = VELOCIDADE
        self.mortinho = 0
        self.morte = 0
        self.x = 0

    def calcular_regras(self):
        
        if self.cenario.matar == False:
            if self.centro_x == pacman.centro_x and self.centro_y == pacman.centro_y:
                self.cenario.fim = 1
            if self.coluna_intencao == self.pacman.coluna and self.linha_intencao == self.pacman.linha:
                self.cenario.fim = 1

        
        else:
            self.cor = AZUL
            if (self.linha == pacman.linha) and (self.coluna == pacman.coluna):
                self.cenario.pontos = self.cenario.pontos + 200
                self.mortinho = 1
                self.linha = random.randint(13, 15)
                self.coluna = random.randint(11, 16)
            if (self.linha == pacman.linha_intencao) and (self.coluna == pacman.coluna_intencao):
                self.cenario.pontos = self.cenario.pontos + 200
                self.mortinho = 1
                self.linha = random.randint(13, 15)
                self.coluna = random.randint(11, 16)

        if self.cenario.matar == True:
            if self.pacman.poder == 500:
                self.pacman.poder = 0
                self.cenario.matar = False
                self.pacman.cor = AMARELO
            self.pacman.poder = self.pacman.poder + 1
            



    def pintar (self, tela):
        pygame.draw.circle(tela, self.cor, (self.centro_x+1, self.centro_y), self.raio, 0)
        pygame.draw.rect(tela, self.cor, (self.centro_x+1-self.raio, self.centro_y, self.tamanho+1, self.tamanho/1.7), 0)

        #olho
        pygame.draw.circle(tela, BRANCO, ((self.centro_x+self.raio/2)+1, self.centro_y-self.raio/2.5), self.raio/2.5, 0)
        pygame.draw.circle(tela, BRANCO, (self.centro_x-self.raio/2, self.centro_y-self.raio/2.5), self.raio/2.5, 0)

        pygame.draw.circle(tela, PRETO, ((self.centro_x+self.raio/2)+1, self.centro_y-self.raio/2.5), self.raio/5, 0)
        pygame.draw.circle(tela, PRETO, (self.centro_x-self.raio/2, self.centro_y-self.raio/2.5), self.raio/5, 0)
    
    def processar_eventos(self):
        #controle X - coluna
        self.coluna_intencao = self.coluna + self.vel_x
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        #controle Y - linha
        self.linha_intencao = self.linha + self.vel_y
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        col = self.coluna_intencao
        lin = self.linha_intencao

        if self.mortinho == 1:
            self.x = self.x + 1
            if (col > 11 and col <= 16) and (13 <= lin < 16):
                if (self.cenario.matriz[lin][col] != 2) or (self.cenario.matriz[lin][col] != 3):
                    self.coluna = self.coluna_intencao
                    self.linha = self.linha_intencao
            self.cor = AZUL
            if self.x == 300:
                self.mortinho = 0
                self.x = 0
                self.vel_y = -VELOCIDADE   

        else:
            self.cor = (self.r,self.g,self.b)
            if (col > 0 and col <= 28) and (0 <= lin < 29):
                if self.cenario.matriz[lin][col] != 2:
                    self.coluna = self.coluna_intencao
                    self.linha = self.linha_intencao
            
            #descendo
            if self.direcao == 1:
                if self.cenario.matriz[self.linha-1][self.coluna] != 2:
                    self.vel_x = 0
                    self.vel_y = -VELOCIDADE
                else:
                    self.direcao = random.randint(3, 4)
            if self.direcao == 2:
                if self.cenario.matriz[self.linha+1][self.coluna] != 2:
                    self.vel_x = 0
                    self.vel_y = VELOCIDADE
                else:
                    self.direcao = random.randint(3, 4)
            if self.direcao == 3:
                if self.cenario.matriz[self.linha][self.coluna+1] != 2:
                    self.vel_x = VELOCIDADE
                    self.vel_y = 0
                else:
                    self.direcao = random.randint(1, 2)
            if self.direcao == 4:
                if self.cenario.matriz[self.linha][self.coluna-1] != 2:
                    self.vel_x = -VELOCIDADE
                    self.vel_y = 0
                else:
                    self.direcao = random.randint(1, 2)
        

        



class Pacman:
    def __init__(self, tamanho_celula):
        self.linha = 1
        self.coluna = 1
        self.centro_x = 320
        self.centro_y = 320
        self.tamanho = tamanho_celula
        self.raio = self.tamanho/2
        self.tamanho_boca = self.raio
        self.cor = AMARELO
        self.poder = 0
        self.vel_x = 0
        self.vel_y = 0
        self.boca = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.i = 0

    def calcular_regras(self):
        #controle X - coluna
        self.coluna_intencao = self.coluna + self.vel_x
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        #controle Y - linha
        self.linha_intencao = self.linha + self.vel_y
        self.centro_y = int(self.linha * self.tamanho + self.raio)
    
    def aceitar_movimento(self):
        self.coluna = self.coluna_intencao
        self.linha = self.linha_intencao

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                    self.boca = 0
                
                if e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                    self.boca = 1

                if e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                    self.boca = 2
                
                if e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
                    self.boca = 3

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                
                if e.key == pygame.K_LEFT:
                    self.vel_x = 0
                
                if e.key == pygame.K_UP:
                    self.vel_y = 0
                
                if e.key == pygame.K_DOWN:
                    self.vel_y = 0

    def pintar(self, tela):
        #corpo
        pygame.draw.circle(tela, self.cor, (self.centro_x,self.centro_y), self.raio, 0)

        #boca
        canto_boca = (self.centro_x, self.centro_y)

        #boca vira pro lado que ele anda
        if self.boca == 0:
            lado_inferior = (self.centro_x + self.raio, (self.centro_y+self.tamanho_boca))
            lado_superior = (self.centro_x + self.raio, (self.centro_y-self.tamanho_boca))

            #olho
            pygame.draw.circle(tela, PRETO, (self.centro_x,self.centro_y - self.raio/2), self.raio/8, 0)

        if self.boca == 1:
            lado_inferior = (self.centro_x - self.raio, (self.centro_y+self.tamanho_boca))
            lado_superior = (self.centro_x - self.raio, (self.centro_y-self.tamanho_boca))

            #olho
            pygame.draw.circle(tela, PRETO, (self.centro_x,self.centro_y - self.raio/2), self.raio/8, 0)

        if self.boca == 2:
            lado_inferior = ((self.centro_x + self.tamanho_boca), self.centro_y-self.raio)
            lado_superior = ((self.centro_x - self.tamanho_boca), self.centro_y-self.raio)

            #olho
            pygame.draw.circle(tela, PRETO, (self.centro_x - self.raio/2, self.centro_y), self.raio/8, 0)

        if self.boca == 3:
            lado_inferior = ((self.centro_x + self.tamanho_boca), self.centro_y+self.raio)
            lado_superior = ((self.centro_x - self.tamanho_boca), self.centro_y+self.raio)

            #olho
            pygame.draw.circle(tela, PRETO, (self.centro_x + self.raio/2, self.centro_y), self.raio/8, 0)
        
        pontos_boca = [canto_boca, lado_inferior, lado_superior]
        pygame.draw.polygon (tela, PRETO, pontos_boca, 0)
    
    def animacao(self):
        if self.i %4 == 0:
            self.tamanho_boca = self.raio
        else:
            self.tamanho_boca = 0

        self.i = self.i + 1

if __name__ == '__main__':
    n_colunas = 28
    bloco_labirinto = int(TAMANHO_TELA//n_colunas)

    pacman = Pacman(bloco_labirinto)
    cenario = Cenario(bloco_labirinto, pacman)
    fantasma1 = Fantasmas(bloco_labirinto, pacman, cenario)
    fantasma2 = Fantasmas(bloco_labirinto, pacman, cenario)
    fantasma3 = Fantasmas(bloco_labirinto, pacman, cenario)
    fantasma4 = Fantasmas(bloco_labirinto, pacman, cenario)
    
    display_surface = pygame.display.set_mode((TAMANHO_TELA, TAMANHO_TELA))

    pygame.display.set_caption('Pac Man')
    font = pygame.font.Font('freesansbold.ttf', 32)
    while True: 
        if cenario.fim == 0:
            text = font.render(str(cenario.pontos), True, AMARELO, AZUL) 
            textRect = text.get_rect()
            textRect.center = (TAMANHO_TELA // 2, TAMANHO_TELA // 4)
            screen.blit(text, textRect)
        if cenario.fim == 1:
            text = font.render("Voce Perdeu", True, (255, 0, 0), PRETO) 
            textRect = text.get_rect()
            textRect.center = (TAMANHO_TELA // 2, TAMANHO_TELA // 2)
            screen.blit(text, textRect)
        if cenario.fim == 2:
            text = font.render("Voce Perdeu", True, (0,255,255), PRETO) 
            textRect = text.get_rect()
            textRect.center = (TAMANHO_TELA // 2, TAMANHO_TELA // 2)
            screen.blit(text, textRect)

        pygame.display.update()

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        #regras
        fantasma1.calcular_regras()
        fantasma2.calcular_regras()
        fantasma3.calcular_regras()
        fantasma4.calcular_regras()
        cenario.calcular_regras()
        pacman.calcular_regras()

        #pintar

        screen.fill(PRETO)
        if cenario.fim == 0:
            cenario.pintar(screen)
            screen.blit(text, textRect)


            pacman.pintar(screen)
            pacman.animacao()

            fantasma1.pintar(screen)
            fantasma2.pintar(screen)
            fantasma3.pintar(screen)
            fantasma4.pintar(screen)

        cenario.somar_pontos()
        pygame.time.delay(100)
        #eventos
        pacman.processar_eventos(eventos)
        fantasma1.processar_eventos()
        fantasma2.processar_eventos()
        fantasma3.processar_eventos()
        fantasma4.processar_eventos()
