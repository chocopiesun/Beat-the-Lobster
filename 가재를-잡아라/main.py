import pygame
from constants import *
from player import Player
from base import Base
from health_bar import HealthBar
from enemy import Enemy
import time
from loaded_assets import *
from button import Button
from timer import Timer

pygame.init()

screen = pygame.display.set_mode((1500, 720))

clock = pygame.time.Clock()

my_base = Base(1370, 365, 1000, my_base_images, 'player')
enemy_base = Base(0, 365, 1000, enemy_base_images, 'enemy')

my_base_health_bar = HealthBar(1380, 335, 110, 20, my_base.health)
enemy_base_health_bar = HealthBar(10, 335, 110, 20, enemy_base.health)

players = [my_base]
health_bars_of_players = []

enemies = [enemy_base]

enemy_spawn_times = [1, 4, 7, 7.5, 12, 15, 25, 25.5]

coin_earning_upgrade_button = Button(1200, 550, 100, 100, coin_earning_upgrade_image)

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

coin = 7
coin_earning_per_second = 2
coin_earning_per_second_level = 1

game_start_time = time.time() 
recent_time = 0

axeman_cooltime_timer = Timer(3)
fishman_cooltime_timer = Timer(10)
coverman_cooltime_timer = Timer(5)
swallow_cooltime_timer = Timer(3)

boss_appeared = False

boss_health_bar = HealthBar(250, 20, 1000, 50, 1000)

boss_health = 1000

while True:
    # 화면 배경색상 설정
    screen.fill((135, 206, 235))
    clock.tick(FPS)
    
    # 발판 그리기
    screen.blit(field_background1_image, (0, 300))
    screen.blit(field_background2_image, (0, 540))

    # 초당 2코인 증가
    coin += coin_earning_per_second**coin_earning_per_second_level / FPS

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if coin >= 2 and (not axeman_cooltime_timer.start_time or axeman_cooltime_timer.is_time_up()):
                    axeman_cooltime_timer.start()
                    coin -= 2
                    players.append(Player(name='axeman', width=120, height=120, speed=30, damage=40, attack_range=30, health=100, attack_cooltime=2.5, sprites=axeman_sprites))
            if event.key == pygame.K_2 :
                if coin >= 10 and (not fishman_cooltime_timer.start_time or fishman_cooltime_timer.is_time_up()):
                    fishman_cooltime_timer.start()
                    coin -= 10
                    players.append(Player(name='fishman', width=120, height=120, speed=30, damage=50, attack_range=25, health=150, attack_cooltime=3, sprites=fishman_sprites))
            if event.key == pygame.K_3 :
                if coin >= 5 and (not coverman_cooltime_timer.start_time or coverman_cooltime_timer.is_time_up()):
                    coverman_cooltime_timer.start()
                    coin -= 5
                    players.append(Player(name='coverman', width=120, height=120, speed=25, damage=20, attack_range=20, health=300, attack_cooltime=34, sprites=coverman_sprites))
            if event.key == pygame.K_4 :
                if coin >= 7 and (not swallow_cooltime_timer.start_time or swallow_cooltime_timer.is_time_up()):
                    swallow_cooltime_timer.start()
                    coin -= 5
                    players.append(Player(name='swallow', width=120, height=120, speed=150, damage=20, attack_range=10, health=300, attack_cooltime=1.6, sprites=swallow_sprites))

    # 조개 적 스폰
    if int(time.time() - game_start_time) in enemy_spawn_times: 
        for i in range(enemy_spawn_times.count(int(time.time() - game_start_time))):
            enemies.append(Enemy(name='seashell', width=100, height=100, speed=30, damage=25, attack_range=30, health=250, attack_cooltime=2.5, sprites=seashell_sprites))

    for i in enemy_spawn_times:
        if int(time.time() - game_start_time) >= i:
            enemy_spawn_times.remove(i)

    # 가재 적 스폰
    if int(time.time() - game_start_time) == 3 and boss_appeared == False:
        enemies.append(Enemy(name='lobster', width=100, height=100, speed=50, damage=75, attack_range=30, health=1000, attack_cooltime=1.5, sprites=lobster_sprites))
        boss_appeared = True

    # 가재 스폰 됐을때 보스 체력바 상단에 띄우기    
    if boss_appeared == True:
        boss_health_bar.update_health(boss_health)
        boss_health_bar.draw(screen)
        draw_text(f"{boss_health} / 1000", 50, (0,0,0), 670, 30)


    # 플레이어 그리기, 이동, 공격 개시, 죽음 감지
    for i in players:
        if i.name == "swallow":
            print(i.x)
        i.draw(screen)
        if i.type != 'player_base':
            i.move()
            i.attack(enemies)
            if i.health <= 0:
                players.remove(i)

    # 적을 죽였을때 코인 보상 주기
    for i in enemies:
        if i.health <= 0 and i.name == 'seashell':
            coin += 4
        if i.name == "lobster":
            boss_health = i.health
            if i.health <= 0:
                boss_appeared = False

    # 적 그리기, 이동, 공격 개시, 죽음 감지
    for i in enemies:
        i.draw(screen)
        if i.type != 'enemy_base':
            i.move()
            i.attack(players)
            if i.health <= 0:
                enemies.remove(i)

    # 베이스 체력바 그리기
    my_base_health_bar.update_health(my_base.health)
    my_base_health_bar.draw(screen)
    enemy_base_health_bar.update_health(enemy_base.health)  
    enemy_base_health_bar.draw(screen)

    # 플레이어 아이콘 그리기
    for i in icon_images:
        screen.blit(i[0], (50 + 110 * icon_images.index(i), 550))

    # 플레이어 스폰 쿨타임 표시 그리기
    if axeman_cooltime_timer.start_time and not axeman_cooltime_timer.is_time_up():
        screen.blit(player_spawn_locked_image, (50, 550))
    if fishman_cooltime_timer.start_time and not fishman_cooltime_timer.is_time_up():
        screen.blit(player_spawn_locked_image, (160, 550))
    if coverman_cooltime_timer.start_time and not coverman_cooltime_timer.is_time_up():
        screen.blit(player_spawn_locked_image, (270, 550))
    if swallow_cooltime_timer.start_time and not swallow_cooltime_timer.is_time_up():
        screen.blit(player_spawn_locked_image, (380, 550))

    # 텍스트 그리기
    draw_text(f"{int(coin)} COIN", 40, (255,215,0), 1300, 30)
    for i in icon_images:
        draw_text(f"{i[1]} COIN", 40, (255,215,0), 50 + 110 * icon_images.index(i), 660)
    draw_text(f"COST : {5** coin_earning_per_second_level}", 40, (255,255,255), 1200, 660)

    # 코인 초당 수입 업그레이드 버튼 그리기
    coin_earning_upgrade_button.draw(screen)
    if coin_earning_upgrade_button.is_clicked(pygame.mouse.get_pos(), event):
        if coin >= 5**coin_earning_per_second_level:
            coin -= 5**coin_earning_per_second_level
            coin_earning_per_second_level += 1

    pygame.display.flip()