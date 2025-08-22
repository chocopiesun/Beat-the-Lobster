import pygame

pygame.init()

axeman_sprites = [
    [
        pygame.transform.scale(pygame.image.load("assets/axeman_moving1.png"),(120,120)),
        pygame.transform.scale(pygame.image.load("assets/axeman_moving2.png"),(120,120))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/axeman_attacking1.png"),(120,120)),
        pygame.transform.scale(pygame.image.load("assets/axeman_attacking2.png"),(120,120))
    ]
]

fishman_sprites = [
    [
        pygame.transform.scale(pygame.image.load("assets/fishman_moving1.png"),(120,120)),
        pygame.transform.scale(pygame.image.load("assets/fishman_moving2.png"),(120,120))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/fishman_attacking1.png"),(120,120)),
        pygame.transform.scale(pygame.image.load("assets/fishman_attacking2.png"),(120,120))
    ]  
]

coverman_sprites = [
    [  
        pygame.transform.scale(pygame.image.load("assets/coverman_moving1.png"),(130, 130)),
        pygame.transform.scale(pygame.image.load("assets/coverman_moving2.png"),(130, 130))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/coverman_attacking1.png"),(130, 130)),
        pygame.transform.scale(pygame.image.load("assets/coverman_attacking2.png"),(130, 130))
    ]
]

swallow_sprites = [
    [  
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking1.png"),(1000, 110)),
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking1.png"),(1000, 110)),
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking2.png"),(1000, 110)),
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking3.png"),(1000, 110)),
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking4.png"),(1000, 110)),
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking5.png"),(1000, 110)),
        pygame.transform.scale(pygame.image.load("assets/swallow_attacking6.png"),(1000, 110))
    ]
]

icon_images = [
    [pygame.transform.scale(pygame.image.load("assets/axeman_icon.png"),(100, 100)), 2],
    [pygame.transform.scale(pygame.image.load("assets/fishman_icon.png"),(100, 100)), 10],
    [pygame.transform.scale(pygame.image.load("assets/coverman_icon.png"),(100, 100)), 5],
    [pygame.transform.scale(pygame.image.load("assets/swallow.png"), (100,100)), 7]
]

seashell_sprites = [
    [
        pygame.transform.scale(pygame.image.load("assets/seashell_moving1.png"),(100,100)),
        pygame.transform.scale(pygame.image.load("assets/seashell_moving2.png"),(100,100))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/seashell_attacking1.png"),(100,100)),
        pygame.transform.scale(pygame.image.load("assets/seashell_attacking2.png"),(100,100))
    ]
]

lobster_sprites = [
    [
        pygame.transform.scale(pygame.image.load("assets/lobster_walking1.png"),(100,100)),
        pygame.transform.scale(pygame.image.load("assets/lobster_walking2.png"),(100,100))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/lobster_attacking1.png"),(100,100)),
        pygame.transform.scale(pygame.image.load("assets/lobster_attacking2.png"),(100,100))
    ]
]

my_base_images = [
    [
        pygame.transform.scale(pygame.image.load("assets/my_base_peace.png"),(130,130))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/my_base_death.png"), (130, 130))
    ]
]

enemy_base_images = [
    [
        pygame.transform.scale(pygame.image.load("assets/enemy_base_peace.png"),(130, 130))
    ],
    [
        pygame.transform.scale(pygame.image.load("assets/enemy_base_death.png"), (130, 130))
    ]
]

field_background1_image = pygame.transform.scale(pygame.image.load("assets/field_background1.png"), (1500, 250))
field_background2_image = pygame.transform.scale(pygame.image.load("assets/field_background2.png"), (1500, 170))

player_spawn_locked_image = pygame.transform.scale(pygame.image.load("assets/player_spawn_locked.png"), (100, 100))

coin_earning_upgrade_image = pygame.transform.scale(pygame.image.load("assets/coin_earning_upgrade.png"), (100, 100))