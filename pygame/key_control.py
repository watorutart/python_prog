import sys
import pygame
from pygame.locals import *

pygame.init() # pygameの初期化
screen = pygame.display.set_mode((400, 300)) # ウインドウの大きさ
pygame.display.set_caption("PyGame") # タイトルバー
image = pygame.image.load("C:/Users/watoru/Pictures/チョコボ.png")

pygame.key.set_repeat(5,5) # キーの押下と押しっぱなしの取得
position = [200, 150] # 座標を配列に[x, y]

# mainループ
def main():
    while True:
        screen.fill((0, 0, 0)) # ウインドウの背景色
        # イベントの取得
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() # 閉じるボタンが押されたらプログラムを終了
                sys.exit() # ()がないとエラー

            # キー操作
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    position[0] -= 5
                elif event.key == K_RIGHT:
                    position[0] += 5
                elif event.key == K_UP:
                    position[1] -= 5
                elif event.key == K_DOWN:
                    position[1] += 5

        # 画面の端に行ったら反対から出るようにする
        position[0] = position[0] % 400
        position[1] = position[1] % 300

        # 画面の描画位置
        rect = image.get_rect()
        rect.center = position

        screen.blit(image, rect)# 画像を描画
        pygame.display.update()

if __name__ == "__main__":
    main()
