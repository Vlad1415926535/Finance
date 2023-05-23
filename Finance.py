import random
import pygame
pygame.init()

clock = pygame.time.Clock()
addcl = 0

pygame.display.set_caption("финансы")

sc_info = pygame.display.Info()

full = False
W, H = 1000, 700
WW, HH = sc_info.current_w, sc_info.current_h
win = pygame.display.set_mode((W, H))

t30 = pygame.font.SysFont('franklingothicmedium', 30)
t50 = pygame.font.SysFont('franklingothicmedium', 50)
t100 = pygame.font.SysFont('franklingothicmedium', 100)

white = (255, 255, 255)
black = (10, 10, 10)
colchan, colgr = 0, True

colors = [[(255, 160, 110), (255, 220, 105)], [(35, 125, 15), (20, 200, 255)], [(0, 255, 195), (0, 190, 255)], [(15, 200, 215), (50, 30, 120)], [(185, 0, 255), (255, 130, 45)], [(230, 120, 10), (230, 215, 50)], [(190, 255, 0), (0, 255, 110)], [(55, 0, 95), (55, 40, 125)], [(165, 0, 0), (65, 0, 0)], [(120, 120, 120), (250, 250, 250)], [(100, 100, 100), (0, 0, 0)]]

moven = 0

plx, ply, vec = 0, 0, 0



class Player():
    name = ''
    alife = True
    insure = 0
    cosin = 250
    cash = (random.randrange(5, 46))*100
    lose = cash
    #cash = 99999
    income = (random.randrange(1, 10))*100
    #income = 1000
    shares = 0
    business = 0
    happy = 0
    color = []

    def __init__(self):
        pass

def Howmuch():
    fact = False
    global plx, ply, vec
    players = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    gradcol = 0

    while not fact:

        win.fill(black)

        pygame.draw.rect(win, white, (W/10, H/10, W*4/5, H*4/5), 10)

        TextC(t50, 'Hello!', (gradcol, gradcol, gradcol), (W/2)+plx, (H/4)+ply)
        TextC(t50, 'How many players?', (gradcol, gradcol, gradcol), (W/2)+plx, (H * 1/3)+ply)
        TextC(t30, '(no more than 9, at least 2)', (gradcol, gradcol, gradcol), (W/2), (H*3/4)+20)

        gradcol = Arise(gradcol, 5)

        if gradcol == 255:
            Spin(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_F4:
                    Fullscreen()
                key_name = pygame.key.name(event.key)
                if key_name.isdigit():
                    if 10 > int(key_name) > 1:
                        noperm = []
                        players = players[:int(key_name)]
                        for a in players:
                            a = Player()
                            obj = a
                            noperm.append(obj)
                        players = noperm
                        return players
                        fact = True

        clock.tick(30)
        pygame.display.update()

def Names(players):
    Transition(0, 'Z', 300)
    global plx, ply, vec
    for a in range (0, len(players)):

        fact = False
        choice = ''
        plx, ply, vec = 0, 0, 0

        while not fact:

            win.fill(black)

            pygame.draw.rect(win, white, (W / 10, H / 10, W * 4 / 5, H * 4 / 5), 10)

            TextC(t50, 'What is name of', white, W / 2, H / 4)
            TextC(t50, f'player number {(a+1)}?', white, W / 2, H / 4 +50)
            TextC(t50, f'{choice}', white, (W / 2)+plx, H / 2 + ply)

            Spin(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_F4:
                        Fullscreen()
                    if event.unicode.isalpha() and len(choice) < 10:
                        choice += event.unicode
                    elif event.key == pygame.K_RETURN and len(choice) > 0:
                        players[a].name = choice
                        fact = True
                    elif event.key == pygame.K_BACKSPACE:
                        if len(choice) > 0:
                            choice = choice[:-1]

            clock.tick(30)
            pygame.display.update()
        Transition(0, 'Z', 300)

    fact = False
    while not fact:

        win.fill(black)

        pygame.draw.rect(win, white, (W / 10, H / 10, W * 4 / 5, H * 4 / 5), 10)

        ply = 2
        for a in players:
            TextC(t30, f'{a.name},', white, W / 3*0.95, H / 7*ply*0.95)
            ply += 0.5

        TextC(t30, 'So,', white, W / 3 * 0.95, H / 7 * 1.5 * 0.95)

        text2 = ['Cool names!', '(actually no).', 'So, I am too lazy to write', 'rules of the game here and', 'therefore just let\'s start']
        ply = 1.5
        for a in range (0, len(text2)):
            TextC(t30, f'{text2[a]}', white, W * 2/3, H / 7 * ply*0.95)
            ply += 0.5

        fact = Enter(3, 5)

        clock.tick(30)
        pygame.display.update()
    for a in players:
        b = random.randrange(0, len(colors))
        a.color = colors[b]
        colors.pop(b)
    #for a in range (0, len(players)):
        #players[a].color = colors[a]


def Game():
    final = random.randrange(30, 71)
    #final = 5
    rects0, rects1 = H / 10 * -1, H / 10 * -1
    inch = 10
    global moven, colchan, colgr

    while moven < final:
        moven += 1

        if inch > 10:
            inch = random.randrange(1, 51)
        else:
            inch = 11
        #inch = 5

        shco = random.uniform(0.5, 1.6)
        buin = random.randrange(-2, 6) * 1000

        for p in players:
            corcol = 0
            colchan, colgr = 0, True
            gradcol = 0

            if p.business == 0:
                screen = 'income'
            elif p.shares > 0:
                screen = 'shares'
            else:
                screen = 'business'

            p.lose += 10

            while p.alife and moven > 1 and not screen == 'choice':
                fact = False

                corcol = BG(p, corcol)
                gradcol = Arise(gradcol, 3)
                pygame.draw.rect(win, black, (W / 10, H / 10, W * 4 / 5, H * 4 / 5))
                pygame.draw.rect(win, white, (W / 10, H / 10, W * 4 / 5, H * 4 / 5), 10)
                if gradcol > 99:
                    fact = Enter(1, 1.5)

                if screen == 'income':
                    if inch > 5:
                        TextC(t50, f'Income from your', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'job is {p.income}$', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)
                    else:
                        TextC(t50, f'You don\'t have income', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'from work on this move', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)

                    if gradcol > 101 and fact:
                        colchan, colgr = 0, True
                        gradcol = 0

                        if p.shares > 0:
                            screen = 'shares'
                        elif 8 > inch > 2:
                            screen = 'loss'
                        else:
                            screen = 'choice'
                        if inch > 5:
                            p.cash += p.income

                elif screen == 'shares':

                    TextC(t50, f'The shares price has', (gradcol, gradcol, gradcol), W / 2, H / 3)
                    TextC(t50, f'changed by {int(shco*100)-100}%', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)

                    if gradcol > 101 and fact:
                        if p.business > 0:
                            screen = 'business'
                        elif 8 > inch > 2:
                            screen = 'loss'
                        else:
                            screen = 'choice'
                            corcol = Transition(corcol, p, 45)
                        p.cash += int(p.shares * shco)
                        p.shares = 0
                        colchan, colgr = 0, True
                        gradcol = 0

                elif screen == 'business':
                    if buin >= 0:
                        TextC(t50, f'Income from your business', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'is ${buin * p.business}', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)
                    else:
                        TextC(t50, f'The loss of the business', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'is ${buin * p.business}', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)
                        if buin * p.business + p.cash < 0:
                            TextC(t50, f'You don\'t even have that money..', (gradcol, gradcol, gradcol), W / 2, H / 3 + 100)

                    if gradcol > 101 and fact:
                        if p.cash + buin * p.business < 0:
                            screen = 'death'
                        elif 8 > inch > 2:
                            screen = 'loss'
                        else:
                            screen = 'choice'
                            corcol = Transition(corcol, p, 45)

                        if p.cash + buin * p.business >= 0:
                            p.cash += buin * p.business

                        colchan, colgr = 0, True
                        gradcol = 0

                elif screen == 'loss':
                    TextC(t50, f'Oh no! You must spend ${p.lose}!', (gradcol, gradcol, gradcol), W / 2, H / 3)
                    if p.cash < p.lose:
                        TextC(t50, f'You don\'t have that, game over', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)
                    if gradcol > 101 and fact:
                        colchan, colgr = 0, True
                        gradcol = 0
                        if p.cash < p.lose:
                            screen = 'death'
                        else:
                            p.cash -= p.lose
                            screen = 'choice'
                            corcol = Transition(corcol, p, 45)

                if screen == 'death':
                    if p.insure > 0:
                        TextC(t50, f'Stop, you have the insure', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'you\'r in the game', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)
                        if gradcol > 101 and fact:
                            screen = 'choice'
                            p.cash = 1000
                            if p.cosin < 8000:
                                p.cosin *= 2
                            corcol = Transition(corcol, p, 45)
                    elif p.business > 0:
                        TextC(t50, f'Well, you just sold', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'a business, you\'r in the game', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)
                        if gradcol > 101 and fact:
                            screen = 'choice'
                            p.cash = 1000
                            p.lose -= 1500
                            p.business -= 1
                            corcol = Transition(corcol, p, 45)
                    else:
                        p.alife = False

                pygame.display.update()

            if p.alife:
                move = True
                choice, gradcol, spent = 0, 0, 0
                screen = 'choice'

                if p.insure > 0:
                    p.insure -= 1

                if p.business == 0 and 1 < moven <= 10:
                    p.income += 50
                if moven >= 40 and p.income > 0:
                    p.income -= 50

                while move:
                    corcol = BG(p, corcol)

                    pygame.draw.rect(win, black, (W / 10, H / 10, W * 4 / 5, H * 4 / 5))
                    pygame.draw.rect(win, white, (W / 10, H / 10, W * 4 / 5, H * 4 / 5), 10)

                    R = (p.color[0][0] - 255) * -1
                    G = (p.color[0][1] - 255) * -1
                    B = (p.color[0][2] - 255) * -1

                    if p.cash > 30000:
                        screen = 'enter'
                        colchan, colgr = 0, True
                        entext = [f'Cash can\'t be', f'more than 30000$']
                        afsc = 'choice'
                        p.cash = 30000

                    if screen == 'choice':
                        def Rects0(r, fact):
                            if r <= 0 and fact:
                                r += 2 + (1+full)
                                if r > 0:
                                    r = 0
                            elif r > H/10 * -1:
                                r -= 2 + (1+full)
                            return r
                        rects0 = Rects0(rects0, choice <= 2)
                        rects1 = Rects0(rects1, choice > 2)

                        def Rects1(listik, r, ch):
                            time = 1
                            for a in range (0, 3):
                                if a == ch:
                                    col = (R, G, B)
                                else:
                                    col = white

                                pygame.draw.rect(win, black, (W / 10*time, r+W/100, W / 5, H / 10-W/50))
                                pygame.draw.rect(win, col, (W / 10*time, r+W/100, W / 5, H / 10-W/50), 2)
                                if a == 0:
                                    TextC(t30, listik[0], col, W / 10*time+W/10, r+H/20)
                                if a == 1:
                                    TextC(t30, listik[1], col, W / 10*time+W/10, r + H / 20)
                                if a == 2:
                                    TextC(t30, listik[2], col, W / 10 * time + W / 10, r + H / 20)
                                time += 3

                        Rects1(['end the turn', 'for yourself', 'shares'], rects0, choice)
                        Rects1(['business', 'insure', 'give up'], rects1, choice-3)
                        TextC(t100, f'CHOOSE!', (colchan, colchan, colchan), W / 2, H / 2)

                        for a in range (0, p.business):
                            pygame.draw.rect(win, (30, 255, 30), (W/10+(a+1)*50, H * 4.2 / 5, 20, 20))
                            pygame.draw.polygon(win, (30, 255, 30), [(W/10+(a+1)*50-5, H * 4.2 / 5), (W/10+(a+1)*50+25, H * 4.2 / 5), (W/10+(a+1)*50+10, H * 4.15 / 5)])
                        for a in range (0, p.insure):
                            pygame.draw.rect(win, (30, 30, 255), (W * 8.5/10 - (a + 1) * 20, H * 4.2 / 5, 10, 20))

                        Colchan(1, 1.5)

                        if choice < 3:
                            pygame.draw.rect(win, (R, G, B), (colchan / 20 + W * 18.5 / 20, H / 20, 1 / 20 * W, H / 100))
                            pygame.draw.polygon(win, (R, G, B), [(colchan / 20 + 19.3 / 20 * W, H / 20 - 5), (colchan / 20 + 19.3 / 20 * W, (H / 20 - 5) + H / 100 + 10),(colchan / 20 + W * 19.7 / 20, H / 20 + H / 200)])
                        else:
                            pygame.draw.rect(win, (R, G, B), (abs(W - W * 18.5 / 20) - 1 / 20 * W - colchan / 20, H / 20, 1 / 20 * W, H / 100))
                            pygame.draw.polygon(win, (R, G, B), [(abs(W - 19.3 / 20 * W) - colchan / 20, H / 20 - 5), (abs(W - 19.3 / 20 * W) - colchan / 20, (H / 20 - 5) + H / 100 + 10), (abs(W - W * 19.7 / 20) - colchan / 20, H / 20 + H / 200)])

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    exit()
                                if event.key == pygame.K_LEFT:
                                    if choice > 0:
                                        choice -= 1
                                if event.key == pygame.K_RIGHT:
                                    if choice < 5:
                                        choice += 1
                                if event.key == pygame.K_UP:
                                    if choice < 3:
                                        choice += 3
                                if event.key == pygame.K_DOWN:
                                    if choice > 2:
                                        choice -= 3
                                if event.key == pygame.K_F4:
                                    Fullscreen()
                                if event.key == pygame.K_RETURN:
                                    rects0, rects1 = H / 10 * -1, H / 10 * -1

                                    if choice == 0:
                                        screen = 'choice0'
                                    if choice == 1:
                                        screen = 'choice1'
                                        quan = ''
                                    if choice == 2:
                                        screen = 'choice2'
                                        quan = ''
                                    if choice == 3:
                                        if p.business < 5:
                                            screen = 'choice3'
                                            quan = ''
                                    if choice == 4:
                                        if p.insure < 5:
                                            screen = 'choice4'
                                    if choice == 5:
                                        screen = 'choice5'

                    if screen == 'choice0':
                        decide = Decide(t50, 'Are you sure?', white, W/2, H/3, (R, G, B))
                        if decide == False:
                            screen = 'choice'
                        elif decide == True:
                            corcol = Transition(corcol, p, 45)
                            move = False
                    if screen == 'choice1':
                        result, quan = Quan("How much do you want to spend?", quan)
                        if result:
                            if not quan == '':
                                if int(quan) <= p.cash:
                                    if int(quan) + spent > 10000:
                                        screen = 'enter'
                                        colchan, colgr = 0, True
                                        entext = [f'You can\'t spend more than 10000$', f'in one turn (you spent {spent})']
                                        afsc = 'choice'
                                    else:
                                        quan = int(quan)
                                        spent += quan
                                        p.cash -= quan
                                        p.happy += quan
                                        screen = 'choice'
                                else:
                                    pass
                            else:
                                screen = 'choice'
                    if screen == 'choice2':
                        result, quan = Quan("How much do you want to spend?", quan)
                        if result:
                            if not quan == '':
                                if int(quan) <= p.cash:
                                    p.shares += int(quan)
                                    p.cash -= int(quan)
                                    screen = 'choice'
                            else:
                                screen = 'choice'
                    if screen == 'choice3':
                        decide = Decide(t50, 'Cost of a company is $10000', white, W / 2, H / 3, (R, G, B))
                        if decide == False:
                            screen = 'choice'
                        elif decide == True and p.cash >= 10000:
                            p.cash -= 10000
                            p.business += 1
                            p.lose += 1500
                            screen = 'choice'
                    if screen == 'choice4':
                        decide = Decide(t50, f'For that you need to spend ${p.cosin+p.business*1000}', white, W / 2, H / 3, (R, G, B))
                        if decide == False:
                            screen = 'choice'
                        elif decide == True and p.cash >= p.cosin+p.business*1000:
                            p.cash -= p.cosin+p.business*1000
                            p.insure += 1
                            screen = 'choice'
                    if screen == 'choice5':
                        decide = Decide(t50, 'Are you sure?', white, W / 2, H / 3, (R, G, B))
                        if decide == False:
                            screen = 'choice'
                        elif decide == True:
                            p.alife = False
                            move = False
                            corcol = Transition(corcol, p, 45)

                    if screen == 'enter':

                        TextC(t50, f'{entext[0]}', (gradcol, gradcol, gradcol), W / 2, H / 3)
                        TextC(t50, f'{entext[1]}', (gradcol, gradcol, gradcol), W / 2, H / 3 + 50)

                        gradcol = Arise(gradcol, 3)
                        if gradcol > 101:
                            fact = Enter(1, 1.5)
                            if fact:
                                corcol = Transition(corcol, p, 45)
                                screen = afsc
                                gradcol = 0

                    clock.tick(120 + addcl * 5)
                    pygame.display.update()

    time, colchan, colgr = 0, 0, True
    while 1:
        fact = False
        while not fact:
            win.fill(black)
            pygame.draw.rect(win, white, (W / 10, H / 10, W * 4 / 5, H * 4 / 5), 10)

            if time > 100:
                TextC(t50, f'That is the', (gradcol, gradcol, gradcol), W / 2 + plx, H / 3 + ply)
                TextC(t50, f'end of the game!', (gradcol, gradcol, gradcol), W / 2 + plx, H / 3 + 50 + ply)

                gradcol = Arise(gradcol, 3)
                if gradcol > 50:
                    Spin(10)
                    fact = Enter(3, 5)
            else:
                time += 1

            clock.tick(30)
            pygame.display.update()
        Transition(0, 'Z', 300)

        result = []
        while len(players) > 0:
            max = 0
            best = 0
            for a in range (0, len(players)):
                if players[a].happy > max:
                    max = players[a].happy
                    best = a
            result.append(players[best])
            players.pop(best)

        col = 30
        while 1:
            win.fill((col, col, col))
            pygame.draw.rect(win, (285-col, 285-col, 285-col), (W / 10, H / 10, W * 4 / 5, H * 4 / 5), 10)

            TextC(t50, f'Let\'s compare your results!', (285 - col, 285 - col, 285 - col), W / 2, H / 7 * 0.95 + 30)
            TextC(t30, f'Thank you for playing!', black, W / 2-plx*0.75, H * 19 / 20-ply*0.75)
            Spin(16)

            y = 2
            for a in range(0, len(result)):
                TextC(t50, f'{a + 1})', (285 - col, 285 - col, 285 - col), W / 3 * 0.95, H / 7 * y * 0.95)

                if a == 0:
                    text = t50.render(f'{result[a].name}', 1, (200, 200, 30))
                else:
                    text = t50.render(f'{result[a].name}', 1, (285 - col, 285 - col, 285 - col))
                text1 = text.get_rect(x=W / 3 * 0.95 + 30, y=H / 7 * y * 0.95 - 25)
                win.blit(text, text1)

                y += 0.5

            if col < 254:
                col += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4:
                        Fullscreen()
                    elif event.key == pygame.K_ESCAPE:
                        exit()
                    elif event.key == pygame.K_RETURN:
                        exit()
            clock.tick(30)
            pygame.display.update()

def BG(p, corcol):

    R = (p.color[1][0] - p.color[0][0])/W
    G = (p.color[1][1] - p.color[0][1])/W
    B = (p.color[1][2] - p.color[0][2])/W

    for a in range (0, int(W/2)):
        if not a+corcol >= W:
            pygame.draw.line(win, (p.color[0][0]+R*a*2, p.color[0][1]+G*a*2, p.color[0][2]+B*2*a), (a+corcol, 0), (a+corcol, H))
        else:
            pygame.draw.line(win, (p.color[0][0] + R * a * 2, p.color[0][1] + G * a * 2, p.color[0][2] + B * a * 2), (a-W+corcol, 0), (a-W+corcol, H))
    for a in range (0, int(W/2)):
        if not a+corcol+W/2 >= W:
            pygame.draw.line(win, (p.color[1][0]-R*a*2, p.color[1][1]-G*a*2, p.color[1][2]-B*2*a), (a+corcol+(W/2), 0), (corcol+a+(W/2), H))
        else:
            pygame.draw.line(win, (p.color[1][0]-R*a*2, p.color[1][1]-G*a*2, p.color[1][2]-B*2*a), ((corcol+a+(W/2))-W, 0), ((corcol+a+(W/2))-W, H))

    pygame.draw.rect(win, black, (0, H*(19/20), W, H*0.05))
    pygame.draw.line(win, white, (0, H*(19/20)), (W, H*(19/20)), 2)

    text = t30.render(f'{p.name}', 1, p.color[0])
    text1 = text.get_rect(x=W * (1 / 20),y=H * (19.1/20) - 2)
    win.blit(text, text1)

    if p.business == 0:
        TextC(t30, f'inc {p.income}$', white, W * 2 / 5, H * 19.5 / 20)
    else:
        TextC(t30, f'inc~{p.business*1500}$', white, W * 2 / 5, H * 19.5 / 20)
    TextC(t30, f'turn {moven}', white, W * 3 / 5, H * 19.5 / 20)
    TextC(t30, f'{p.cash}$', white, W * 9/10, H * 19.5/20)

    if corcol < W:
        corcol += 1
    else:
        corcol = 0
    return corcol

def Colchan(p, m):
    global colgr, colchan
    if colgr:
        colchan += p
        if colchan == 255:
            colgr = False
    else:
        colchan -= m
        if colchan == 0:
            colgr = True

    if colchan > 255:
        colchan, colgr = 255, False
    if colchan < 0:
        colchan, colgr = 0, True

def Transition(corcol, p, max):

    tW = W/10
    dif = 0
    max = int(max/(1+full/1.5))

    for a in range(0, int(max*2)):
        if p == 'Z':
            win.fill(black)
        else:
            corcol = BG(p, corcol)

        pygame.draw.rect(win, black, (tW + dif, H / 10, W * 4 / 5 - dif * 2, H * 4 / 5))
        pygame.draw.rect(win, white, (tW+dif, H/10, W * 4 / 5 - dif * 2, H * 4 / 5), 10)

        if a < max:
            dif += W/(max*(3+(1/3))) * (1+full/100)
        else:
            dif -= W/(max * (3 + (1 / 3))) * (1+full/100)
        pygame.display.update()
    return corcol

decide = 0
def Decide(t, text, col, X, Y, RGB):
    TextC(t, f'{text}', col, X, Y)

    global decide
    if decide == 0:
        TextC(t, f'NO', RGB, W/3, (H * 2/3) - 30)
        TextC(t, f'YES', white, W * 2/3, H * 2 / 3)
    elif decide == 1:
        TextC(t, f'NO', white, W/3, H * 2/3)
        TextC(t, f'YES', RGB, W * 2/3, (H * 2 / 3) - 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_F4:
                Fullscreen()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                if decide == 0:
                    decide = 1
                else:
                    decide = 0
            elif event.key == pygame.K_RETURN:
                if decide == 0:
                    return False
                else:
                    return True

def Quan(text, quan):
    TextC(t50, f'{text}', white, W/2, H/3)
    TextC(t50, f'{quan}', white, W/2, H * 2/3)
    result = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_F4:
                Fullscreen()
            elif event.key == pygame.K_RETURN:
                result = True
                if quan == '':
                    quan = 0
                    result = True
            elif event.key == pygame.K_BACKSPACE:
                if len(quan) > 0:
                    quan = quan[:-1]
            key_name = pygame.key.name(event.key)
            if key_name.isdigit():
                if len(quan) < 5:
                    quan += key_name

    return result, quan

def Enter(a, b):
    fact = False
    Colchan(a, b)

    TextC(t30, 'press enter', (colchan, colchan, colchan), (W * 2 / 3), (H / 7) * 4.75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_F4:
                Fullscreen()
            elif event.key == pygame.K_RETURN:
                fact = True
    return fact

def Arise(gradcol, num):
    if gradcol < 255:
        gradcol += num
    return gradcol

def Spin(max):
    global vec, plx, ply
    if vec == 0:
        plx -= 0.25
        ply += 0.25
        if plx == -max:
            vec = 1
    elif vec == 1:
        plx += 0.5
        ply += 0.5
        if plx == 0:
            vec = 2
    elif vec == 2:
        plx += 1
        ply -= 1
        if plx == max:
            vec = 3
    else:
        plx -= 2
        ply -= 2
        if plx <= 0:
            plx, ply, vec = 0, 0, 0

def TextC(t, txt, C, X, Y):
    text = t.render(f'{txt}', 1, C)
    text1 = text.get_rect(center=(X, Y))
    win.blit(text, text1)

def Fullscreen():
    global W, H, win, full, addcl
    if full:
        W, H = 1000, 700
        win = pygame.display.set_mode((W, H))
        full = False
        addcl = 0
    else:
        W, H = WW, HH
        win = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
        full = True
        addcl = 50

players = Howmuch()
Names(players)
Game()
