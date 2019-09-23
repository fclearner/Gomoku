import pygame
import sys
import os
from pygame.locals import *

import numpy as np

class Gomoku:

    def __init__(self):
        self.chessBoardImg = 'img/chessboard.png' # 800*800 棋盘左上角:29*29 棋盘间隔:54
        self.whileChessImg = 'img/white.png' # 53*53
        self.blackChessImg = 'img/black.png' # 53*53
        self.cL = np.zeros((19, 19))
        self.curx = 0
        self.cury = 0
        self.chessColor = 0

        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (160,40)
        self.screen = pygame.display.set_mode((1200, 800), 0, 32)
        #创建了一个窗口
        pygame.display.set_caption("Welcome to Gomoku!")

        self.background = pygame.image.load(self.chessBoardImg).convert()
        self.whiteChess = pygame.image.load(self.whileChessImg).convert_alpha()
        self.blackChess = pygame.image.load(self.blackChessImg).convert_alpha()
        self.surf1 = pygame.Surface((360,300))
        self.surf1.fill((255, 255, 255))

        self.surf2 = pygame.Surface((360,300))
        self.surf2.fill((255, 255, 255))

    def IsWin(self):
        i = self.curx
        j = self.cury
        maxc = 0
        curChessColor = (self.chessColor + 1) % 2 + 1

        count = 1
        for _ in range(4): # 左上
            i -= 1
            j -= 1
            if i >= 0 and j >= 0 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 上
            j -= 1
            if j >= 0 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 右上
            i += 1
            j -= 1
            if i < 19 and j >= 0 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 右
            i += 1
            if i < 19 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 右下
            i += 1
            j += 1
            if i < 19 and j < 19 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 下
            j += 1
            if j < 19 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 左下
            i -= 1
            j += 1
            if i >= 0 and j < 19 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        i = self.curx
        j = self.cury
        count = 1
        for _ in range(4): # 左
            i -= 1
            if i >= 0 and self.cL[i][j] == curChessColor:
                count += 1
            else:
                break
        maxc = max(maxc, count)

        s = ''
        if maxc == 5:
            if curChessColor == 1:
                s = 'white'
            else:
                s = 'black'
        return s

    def run(self):
        s = ''
        self.winMark = False
        while True:
        #游戏主循环
            for event in pygame.event.get():
                if event.type == QUIT:
                    #接收到退出事件后退出程序
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if not self.winMark:
                        x, y = pygame.mouse.get_pos()
                        self.curx = int((x-3)/53)
                        self.cury = int((y-3)/53)
                        if self.chessColor == 0:
                            self.cL[int((x-3)/53)][int((y-3)/53)] = 1
                            self.chessColor = (self.chessColor+1)%2
                        elif self.chessColor == 1:
                            self.cL[int((x-3)/53)][int((y-3)/53)] = 2
                            self.chessColor = (self.chessColor+1)%2

                        s = self.IsWin()
                    else:
                        self.winMark = False
                        self.cL = np.zeros((19, 19))
                        self.curx = 0
                        self.cury = 0
                        self.chessColor = 0
                        s = ''

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.surf1,(820,20))
            self.screen.blit(self.surf2,(820,480))

            for i in range(19): # 棋子刷新
                for j in range(19):
                    if self.cL[i][j] == 1:
                        self.screen.blit(self.whiteChess, (3+53*i, 3+53*j))
                    elif self.cL[i][j] == 2:
                        self.screen.blit(self.blackChess, (3+53*i, 3+53*j))

            if s == '':
                pass
            elif s == 'black':
                self.textFont = pygame.font.SysFont('italic',80)
                self.textSurface = self.textFont.render("Black Win",True,(0,0,0))
                self.textSurface.set_alpha(128)
                self.screen.blit(self.textSurface, (860, 370))
                self.winMark = True
            elif s == 'white':
                self.textFont = pygame.font.SysFont('italic',80)
                self.textSurface = self.textFont.render("White Win",True,(255,255,255))
                self.textSurface.set_alpha(128)
                self.screen.blit(self.textSurface, (860, 370))
                self.winMark = True

            pygame.display.update()

if __name__ == "__main__":
    g = Gomoku()
    g.run()