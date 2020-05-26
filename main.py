from digu import *
from tkinter import *
import pygame
import random
from tkinter import messagebox

# tkinter preconditions

game_quit = False
check_for_quit = False


def quit_pi():
    global run, game_quit, check_for_quit
    initial_info.destroy()
    game_quit = True
    check_for_quit = True


player_information = []
Trumps = False


# Pregame information
# tkinter Functions


def get_info():
    global Trumps
    player_name = text_1.get()
    if player_name == '':
        messagebox.showerror('Error', 'Please Enter a valid Player Name')
    else:
        player_information.append(player_name)
        if coin_toss(call_trumps.get()):
            messagebox.showinfo('Call Trumps', 'Great, You get to call Trumps')
            Trumps = True
        else:
            messagebox.showinfo('Call Trumps', 'Sorry, the computer will call Trumps')
        initial_info.quit()
        initial_info.destroy()


initial_info = Tk()
initial_info.title('Digu Player Information')
frame_1 = Frame(initial_info)
frame_1.pack(side=LEFT)
label_1 = Label(frame_1, text='Player Name')
label_1.pack(side=TOP)
text_1 = Entry(frame_1)
text_1.pack(side=TOP)
label_2 = Label(frame_1, text='Call Heads or Tails for calling Trumps')
label_2.pack(side=TOP)
call_trumps = StringVar(initial_info)
call_trumps.set('Heads')
option = OptionMenu(frame_1, call_trumps, 'Heads', 'Tails')
option.pack(side=TOP)
button_1 = Button(frame_1, text='Confirm', command=get_info)
button_1.pack(side=BOTTOM)
initial_info.protocol("WM_DELETE_WINDOW", quit_pi)  # if 'x' on the window is pressed then the function is performed
initial_info.mainloop()

# Py_game Preconditions
if game_quit is False:
    pygame.init()
    win = pygame.display.set_mode((1000, 668))
    pygame.display.set_caption('DIGU')
    background = pygame.image.load('wooden_table.jpg')
    dhu = pygame.image.load('dhufun.png')
    icon = pygame.image.load('cards_icon.png')
    pygame.display.set_icon(icon)
    font = pygame.font.Font(None, 30)
    player_name = font.render(player_information[0].upper(), True, (0, 150, 255))
    player_teammate = font.render(player_information[0].upper() + " TEAMMATE", True, (0, 150, 255))
    computer = font.render('COMP', True, (255, 255, 255))
    computer = pygame.transform.rotate(computer, 90)
    comp_team_mate = font.render("COMP TEAMMATE", True, (255, 255, 255))
    comp_team_mate = pygame.transform.rotate(comp_team_mate, 270)
    main_deck = Deck()
    main_deck.shuffle()
    player_hand = main_deck.deal_hand(13)
    player_teammate_hand = main_deck.deal_hand(13)
    computer_hand = main_deck.deal_hand(13)
    computer_teammate_hand = main_deck.deal_hand(13)
    displayed_names = False
    player_teammate_X = 350
    player_trump_x = 750
    player_trump_change = 1
    player_trump_selected = False
    comp_trump_selected = False
    trump = ''
    stop_initialize = False
    player_round_done = False
    comp_round_done = False
    player_tm_round_done = False
    comp_tm_round_done = False
    comp_trumps = []
    comp_teammate_trumps = []
    player_teammate_trumps = []
    player_played_hands = []
    comp_played_hands = []
    player_teammate_played_hands = []
    comp_teammate_played_hands = []
    trump_list_chosen = False
    comp_won_hands = 0
    player_won_hands = 0
    comp_tm_won_hands = 0
    player_tm_won_hands = 0
    all_rounds_done = False
    # x1 = 90
    # y1 = 170
    # x2 = 250
    # y2 = 470
    # x3 = 850
    # y3 = 170
    # x4 = 250
    # y4 = 140
    round_status = dict(round1=False, round2=False, round3=False, round4=False, round5=False, round6=False, round7=False,
                        round8=False, round9=False, round10=False, round11=False, round12=False, round13=False)

deck_clubs = [pygame.image.load('Clubs 1.png'), pygame.image.load('Clubs 2.png'), pygame.image.load('Clubs 3.png'),
              pygame.image.load('Clubs 4.png'), pygame.image.load('Clubs 5.png'), pygame.image.load('Clubs 6.png'),
              pygame.image.load('Clubs 7.png'),
              pygame.image.load('Clubs 8.png'), pygame.image.load('Clubs 9.png'), pygame.image.load('Clubs 10.png'),
              pygame.image.load('Clubs 11.png'),
              pygame.image.load('Clubs 12.png'), pygame.image.load('Clubs 13.png')]
deck_diamonds = [pygame.image.load('Diamond 1.png'), pygame.image.load('Diamond 2.png'),
                 pygame.image.load('Diamond 3.png'), pygame.image.load('Diamond 4.png'),
                 pygame.image.load('Diamond 5.png'), pygame.image.load('Diamond 6.png'),
                 pygame.image.load('Diamond 7.png'), pygame.image.load('Diamond 8.png'),
                 pygame.image.load('Diamond 9.png'),
                 pygame.image.load('Diamond 10.png'), pygame.image.load('Diamond 11.png'),
                 pygame.image.load('Diamond 12.png'), pygame.image.load('Diamond 13.png')]
deck_hearts = [pygame.image.load('Hearts 1.png'), pygame.image.load('Hearts 2.png'), pygame.image.load('Hearts 3.png'),
               pygame.image.load('Hearts 4.png'), pygame.image.load('Hearts 5.png'), pygame.image.load('Hearts 6.png'),
               pygame.image.load('Hearts 7.png'),
               pygame.image.load('Hearts 8.png'), pygame.image.load('Hearts 9.png'), pygame.image.load('Hearts 10.png'),
               pygame.image.load('Hearts 11.png'), pygame.image.load('Hearts 12.png'),
               pygame.image.load('Hearts 13.png')]
deck_spades = [pygame.image.load('Spades 1.png'), pygame.image.load('Spades 2.png'), pygame.image.load('Spades 3.png'),
               pygame.image.load('Spades 4.png'), pygame.image.load('Spades 5.png'), pygame.image.load('Spades 6.png'),
               pygame.image.load('Spades 7.png'),
               pygame.image.load('Spades 8.png'), pygame.image.load('Spades 9.png'), pygame.image.load('Spades 10.png'),
               pygame.image.load('Spades 11.png'),
               pygame.image.load('Spades 12.png'), pygame.image.load('Spades 13.png')]
card_back = pygame.image.load('Back Red 1.png')
player_turn = pygame.image.load('player_turn.png')
player_trump = pygame.image.load('player_trump.png')
comp_turn = pygame.image.load('comp_turn.png')
comp_trump = pygame.image.load('comp_trump.png')
first = [num for num in range(20, 920 + 75, 75)]
second = [num for num in range(67, 967 + 75, 75)]
card_images = [deck_hearts, deck_clubs, deck_spades, deck_diamonds]
player_deck_rectangle = pygame.Rect(20, 540, 900, 100)
player_deck_bg = pygame.image.load('ply_deck_bg.jpg')
comp_deck_rectangle = pygame.Rect(40, 150, 50, 405)
comp_deck = pygame.image.load('comp_deck.jpg')
comp_tm_deck_rectangle = pygame.Rect(900, 150, 50, 405)
comp_tm_deck = pygame.image.load('comp_tm_deck.jpg')
player_tm_deck_rectangle = pygame.Rect(350, 60, 610, 65)
player_tm_deck = pygame.image.load('ply_tm_deck.jpg')
play_area_rectangle = pygame.Rect(430, 267, 62, 72)
play_area = pygame.image.load('play_area.jpg')


# py_game Functions

# Initialize_game functions


def display_player_names():
    win.blit(background, (0, 0))
    win.blit(player_name, (450, 630))
    win.blit(player_teammate, (400, 20))
    win.blit(computer, (10, 300))
    win.blit(comp_team_mate, (970, 220))


def player_deck_clear():
    win.blit(player_deck_bg, player_deck_rectangle)
    win.blit(player_name, (450, 630))


def comp_deck_clear():
    win.blit(comp_deck, comp_deck_rectangle)


def comp_tm_deck_clear():
    win.blit(comp_tm_deck, comp_tm_deck_rectangle)


def player_tm_deck_clear():
    win.blit(player_tm_deck, player_tm_deck_rectangle)


def play_area_clear():
    win.blit(play_area, play_area_rectangle)


def clear_all_decks():
    player_deck_clear()
    comp_deck_clear()
    comp_tm_deck_clear()
    player_tm_deck_clear()
    play_area_clear()


def start_new_round():
    global player_round_done, player_tm_round_done, comp_round_done, comp_tm_round_done
    if player_round_done and player_tm_round_done and comp_round_done and comp_tm_round_done:
        player_round_done = False
        player_tm_round_done = False
        comp_round_done = False
        comp_tm_round_done = False


def match_cards(i, x, y):
    k = 0
    j = 0
    for s in suits:
        if i.suit == s:
            for v in values:
                if i.value == v:
                    win.blit(card_images[j][k], (x, y))
                if k <= 12:
                    k += 1
        if j <= 3:
            j += 1


def card_assignment_for_players(x_limit, no_comp, no_comptm, no_plytm, comp_limit, comptm_limit, playertm_limit):
    global player_hand
    x = 20
    y = 550
    computer_y = 150
    computer_teammate_y = 150
    player_teammate_x = 350
    for i in player_hand:
        match_cards(i, x, y)
        x += 75
        if x > x_limit:
            x = 20
    for card in range(no_comp):
        win.blit(card_back, (40, computer_y))
        computer_y += 20
        if computer_y > comp_limit:
            computer_y = 150
    for card in range(no_comptm):
        win.blit(card_back, (900, computer_teammate_y))
        computer_teammate_y += 20
        if computer_teammate_y > comptm_limit:
            computer_teammate_y = 150
    for card in range(no_plytm):
        win.blit(card_back, (player_teammate_x, 60))
        player_teammate_x += 20
        if player_teammate_x > playertm_limit:
            player_teammate_x = 350


def player_select_trump():
    global player_trump_selected, trump, run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 550 <= event.pos[1] <= 612:
                    for i in range(len(first)):
                        if first[i] <= event.pos[0] <= second[i]:
                            trump = player_hand[i].suit
                            player_trump_selected = True
    show_trump = font.render('TRUMP IS ' + trump.upper(), True, (0, 150, 255))
    win.blit(show_trump, (20, 60))
    win.blit(player_turn, (700, 480))


def comp_select_trump():
    global comp_trump_selected, trump
    hearts = 0
    spades = 0
    diamonds = 0
    clubs = 0
    for i in computer_hand:
        if i.suit == 'hearts':
            hearts += 1
        if i.suit == 'spades':
            spades += 1
        if i.suit == 'clubs':
            clubs += 1
        if i.suit == 'diamonds':
            diamonds += 1
    if hearts >= spades and hearts >= clubs and hearts >= diamonds:
        trump = 'hearts'
    if spades >= hearts and spades >= clubs and spades >= diamonds:
        trump = 'spades'
    if clubs >= hearts and clubs >= spades and clubs >= diamonds:
        trump = 'clubs'
    if diamonds >= hearts and diamonds >= spades and diamonds >= clubs:
        trump = 'diamonds'
    show_trump = font.render('TRUMP IS ' + trump.upper(), True, (255, 255, 255))
    win.blit(show_trump, (20, 60))
    win.blit(comp_turn, (90, 180))
    comp_trump_selected = True


def trump_movement():
    global player_trump_x, player_trump_change
    win.blit(player_trump, (player_trump_x, 480))
    player_trump_x += player_trump_change
    if player_trump_x > 800:
        player_trump_change = -1
    elif player_trump_x < 750:
        player_trump_change = 1


def determine_trumps():
    if Trumps:
        win.blit(player_turn, (700, 480))
        trump_movement()
        player_select_trump()
    elif Trumps is False:
        comp_select_trump()
        card_assignment_for_players(920, 13, 13, 13, 390, 390, 590)


def initialize_game():
    if player_trump_selected is False and comp_trump_selected is False:
        display_player_names()
        card_assignment_for_players(920, 13, 13, 13, 390, 390, 590)
        determine_trumps()


#  Round Functions

def initial_layout():
    display_player_names()
    show_trump = font.render('TRUMP IS ' + trump.upper(), True, (255, 255, 255))
    win.blit(show_trump, (20, 60))


def trump_list():
    global trump_list_chosen
    if player_trump_selected or comp_trump_selected:
        for i in computer_hand:
            if i.suit == trump:
                comp_trumps.append(i)
                computer_hand.remove(i)
        for j in computer_teammate_hand:
            if j.suit == trump:
                comp_teammate_trumps.append(j)
                computer_teammate_hand.remove(j)
        for k in player_teammate_hand:
            if k.suit == trump:
                player_teammate_trumps.append(k)
                player_teammate_hand.remove(k)
        trump_list_chosen = True


def check_cheat(rnd, card):
    if comp_trump_selected:
        for j in player_hand:
            if j.suit == comp_played_hands[rnd].suit:
                if card.suit != comp_played_hands[rnd].suit:
                    return True
        return False
    if player_trump_selected:
        return False


def player_play(cl, rnd, turn, a, b, c, d, e, f, g):
    global player_round_done, run
    rnd -= 1
    # event = pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 550 <= event.pos[1] <= 612:
                    for i in range(turn):
                        if first[i] <= event.pos[0] <= second[i]:
                            if cl:
                                clear_all_decks()
                            win.blit(player_turn, (700, 480))
                            if check_cheat(rnd, player_hand[i]):
                                player_play(cl, rnd, turn, a, b, c, d, e, f, g)
                            elif check_cheat(rnd, player_hand[i]) is False:
                                match_cards(player_hand[i], 450, 330)
                                player_played_hands.append(player_hand.pop(i))
                                player_deck_clear()
                                card_assignment_for_players(a, b, c, d, e, f, g)
                                player_round_done = True


def have_suits(hand, s):
    for i in hand:
        if i.suit == s:
            return True
    return False


def check_least_high_card(c, hand):
    n = 0
    for s in suits:
        for m in range(13):
            if c.suit == s and c.value == values[n]:
                for k in range(13):
                    for i in hand:
                        if n == 0:
                            return None
                        elif n == 12:
                            if i.suit == s and i.value == 'A':
                                return i
                        elif 0 < n < 12:
                            if i.suit == s and i.value == values[n + 1]:
                                return i
                    if n == 12:
                        break
                    n += 1
                    if n > 12:
                        n = 0
                        break
            if n == 12:
                break
            n += 1
        n = 0


def check_lowest_value_card_of_suit(hand, s):
    n = 0
    for k in range(13):

        for i in hand:
            if i.suit == s:
                if i.value == values[n + 1]:
                    return i
        n += 1
        if n == 12:
            for j in hand:
                if j.suit == s:
                    if j.value == 'A':
                        return j
        if n > 12:
            return None


def check_lowest_value_card(hand):
    n = 0
    for k in range(13):
        for i in hand:
            if i.value == values[n + 1]:
                return i
        n += 1
        if n == 12:
            for j in hand:
                if j.value == 'A':
                    return j
        if n > 12:
            return None


def check_highest_value_card_of_suit(hand, s):
    n = 13
    for j in hand:
        if j.suit == s:
            if j.value == "A":
                return j
    for k in range(13):

        for i in hand:
            if i.suit == s:
                if i.value == values[n - 1]:
                    return i
        n -= 1
        if n < 2:
            return None


def check_highest_value_card(hand):
    n = 13
    for j in hand:
        if j.value == "A":
            return j
    for k in range(13):
        for i in hand:
            if i.value == values[n-1]:
                return i
        n -= 1
        if n < 2:
            return None


def comp_tm_set_play(played_trumps, card, a, b, c, d, e, f, g):
    global comp_tm_round_done
    if played_trumps is False:
        match_cards(card, 470, 300)
        comp_teammate_played_hands.append(computer_teammate_hand.pop(computer_teammate_hand.index(card)))
        comp_tm_deck_clear()
        card_assignment_for_players(a, b, c, d, e, f, g)
        comp_tm_round_done = True
    elif played_trumps:
        match_cards(card, 470, 300)
        comp_teammate_played_hands.append(comp_teammate_trumps.pop(comp_teammate_trumps.index(card)))
        comp_tm_deck_clear()
        card_assignment_for_players(a, b, c, d, e, f, g)
        comp_tm_round_done = True


def player_tm_set_play(played_trumps, card, a, b, c, d, e, f, g):
    global player_tm_round_done
    if played_trumps is False:
        match_cards(card, 450, 270)
        player_teammate_played_hands.append(player_teammate_hand.pop(player_teammate_hand.index(card)))
        player_tm_deck_clear()
        card_assignment_for_players(a, b, c, d, e, f, g)
        player_tm_round_done = True
    elif played_trumps:
        match_cards(card, 450, 270)
        player_teammate_played_hands.append(player_teammate_trumps.pop(player_teammate_trumps.index(card)))
        player_tm_deck_clear()
        card_assignment_for_players(a, b, c, d, e, f, g)
        player_tm_round_done = True


def comp_set_play(played_trumps, card, a, b, c, d, e, f, g):
    global comp_round_done
    if played_trumps is False:
        match_cards(card, 430, 300)
        comp_played_hands.append(computer_hand.pop(computer_hand.index(card)))
        comp_deck_clear()
        card_assignment_for_players(a, b, c, d, e, f, g)
        comp_round_done = True
    elif played_trumps:
        match_cards(card, 430, 300)
        comp_played_hands.append(comp_trumps.pop(comp_trumps.index(card)))
        comp_deck_clear()
        card_assignment_for_players(a, b, c, d, e, f, g)
        comp_round_done = True


def comp_tm_play(comp_played, rnd, ply_tm_card_pos):
    x_limit = 920 - (75 * rnd)
    cards = 13 - rnd
    card_pos = 390 - (20 * rnd)
    rnd -= 1
    if comp_played:
        a = comp_played_hands[rnd]
        b = player_played_hands[rnd]
        if a.suit != trump and b.suit != trump:
            if a.suit == b.suit:
                if have_suits(computer_teammate_hand, a.suit):
                    c = compare_cards(a, b)
                    d = check_least_high_card(c, computer_teammate_hand)
                    if d is not None:
                        comp_tm_set_play(False, d, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                    elif d is None:
                        e = check_lowest_value_card_of_suit(computer_teammate_hand, a.suit)
                        comp_tm_set_play(False, e, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                elif have_suits(computer_teammate_hand, a.suit) is False:
                    if len(comp_teammate_trumps) > 0:
                        a1 = check_lowest_value_card(comp_teammate_trumps)
                        comp_tm_set_play(True, a1, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                    elif len(comp_teammate_trumps) == 0:
                        z1 = check_lowest_value_card(computer_teammate_hand)
                        comp_tm_set_play(False, z1, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
            elif a.suit != b.suit:
                if have_suits(computer_teammate_hand, a.suit):
                    b1 = check_least_high_card(a, computer_teammate_hand)
                    if b1 is not None:
                        comp_tm_set_play(False, b1, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                    elif b1 is None:
                        b2 = check_lowest_value_card_of_suit(computer_teammate_hand, a.suit)
                        comp_tm_set_play(False, b2, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                elif have_suits(computer_teammate_hand, a.suit) is False:
                    if len(comp_teammate_trumps) > 0:
                        b3 = check_lowest_value_card(comp_teammate_trumps)
                        comp_tm_set_play(True, b3, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                    elif len(comp_teammate_trumps) == 0:
                        b4 = check_lowest_value_card(computer_teammate_hand)
                        comp_tm_set_play(False, b4, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
        elif a.suit != trump and b.suit == trump:
            if have_suits(computer_teammate_hand, a.suit):
                g = check_lowest_value_card_of_suit(computer_teammate_hand, a.suit)
                comp_tm_set_play(False, g, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
            elif have_suits(computer_teammate_hand, a.suit) is False:
                if len(comp_teammate_trumps) > 0:
                    h = check_least_high_card(b, comp_teammate_trumps)
                    if h is not None:
                        comp_tm_set_play(True, h, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
                    elif h is None:
                        i = check_lowest_value_card(computer_teammate_hand)
                        comp_tm_set_play(False, i, x_limit, cards, cards, cards + 1, card_pos, card_pos,
                                         ply_tm_card_pos)
                elif len(comp_teammate_trumps) == 0:
                    j = check_lowest_value_card(computer_teammate_hand)
                    comp_tm_set_play(False, j, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
        elif a.suit == trump and b.suit != trump:
            if len(comp_teammate_trumps) > 0:
                k = check_least_high_card(a, comp_teammate_trumps)
                if k is not None:
                    comp_tm_set_play(True, k, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
                elif k is None:
                    m = check_lowest_value_card(comp_teammate_trumps)
                    comp_tm_set_play(True, m, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_teammate_trumps) == 0:
                n = check_lowest_value_card(computer_teammate_hand)
                comp_tm_set_play(False, n, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
        elif a.suit == trump and b.suit == trump:
            if len(comp_teammate_trumps) > 0:
                p = check_least_high_card(compare_cards(a, b), comp_teammate_trumps)
                if p is not None:
                    comp_tm_set_play(True, p, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
                elif p is None:
                    q = check_lowest_value_card(comp_teammate_trumps)
                    comp_tm_set_play(True, q, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_teammate_trumps) == 0:
                r = check_lowest_value_card(computer_teammate_hand)
                comp_tm_set_play(False, r, x_limit, cards, cards, cards + 1, card_pos, card_pos, ply_tm_card_pos)

    if comp_played is False:
        s = player_played_hands[rnd]
        if s.suit != trump:
            if have_suits(computer_teammate_hand, s.suit):
                t = check_least_high_card(s, computer_teammate_hand)
                if t is not None:
                    comp_tm_set_play(False, t, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                     ply_tm_card_pos)
                elif t is None:
                    t1 = check_lowest_value_card_of_suit(computer_teammate_hand, s.suit)
                    comp_tm_set_play(False, t1, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                     ply_tm_card_pos)
            elif have_suits(computer_teammate_hand, s.suit) is False:
                if len(comp_teammate_trumps) > 0:
                    u = check_lowest_value_card(comp_teammate_trumps)
                    comp_tm_set_play(True, u, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                     ply_tm_card_pos)
                elif len(comp_teammate_trumps) == 0:
                    v = check_lowest_value_card(computer_teammate_hand)
                    comp_tm_set_play(False, v, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                     ply_tm_card_pos)
        elif s.suit == trump:
            if len(comp_teammate_trumps) > 0:
                w = check_least_high_card(s, comp_teammate_trumps)
                if w is not None:
                    comp_tm_set_play(True, w, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                     ply_tm_card_pos)
                if w is None:
                    x = check_lowest_value_card(comp_teammate_trumps)
                    comp_tm_set_play(True, x, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                     ply_tm_card_pos)
            elif len(comp_teammate_trumps) == 0:
                y = check_lowest_value_card(computer_teammate_hand)
                comp_tm_set_play(False, y, x_limit, cards + 1, cards, cards + 1, card_pos + 20, card_pos,
                                 ply_tm_card_pos)


def player_tm_play(comp_played, rnd, ply_tm_card_pos):
    x_limit = 920 - (75 * rnd)
    cards = 13 - rnd
    card_pos = 390 - (20 * rnd)
    rnd -= 1
    if comp_played:
        a = comp_played_hands[rnd]
        b = player_played_hands[rnd]
        c = comp_teammate_played_hands[rnd]
        if a.suit != trump and b.suit != trump and c.suit != trump:
            if a.suit == b.suit == c.suit:
                if have_suits(player_teammate_hand, a.suit):
                    d = compare_cards(compare_cards(a, b), c)
                    d0 = check_least_high_card(d, player_teammate_hand)
                    if d0 is not None:
                        player_tm_set_play(False, d0, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d0 is None:
                        d1 = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                        player_tm_set_play(False, d1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(player_teammate_hand, a.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        d2 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, d2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        d3 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, d3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif a.suit == b.suit and b.suit != c.suit:
                if have_suits(player_teammate_hand, a.suit):
                    d4 = check_least_high_card(compare_cards(a, b), player_teammate_hand)
                    if d4 is not None:
                        player_tm_set_play(False, d4, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d4 is None:
                        d5 = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                        player_tm_set_play(False, d5, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(player_teammate_hand, a.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        d6 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, d6, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        d7 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, d7, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif a.suit == c.suit and c.suit != b.suit:
                if have_suits(player_teammate_hand, a.suit):
                    d8 = check_least_high_card(compare_cards(a, c), player_teammate_hand)
                    if d8 is not None:
                        player_tm_set_play(False, d8, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d8 is None:
                        d9 = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                        player_tm_set_play(False, d9, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(player_teammate_hand, a.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        d10 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, d10, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        d11 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, d11, x_limit, cards, cards, cards, card_pos, card_pos,
                                           ply_tm_card_pos)
            elif a.suit != b.suit and b.suit == c.suit:
                if have_suits(player_teammate_hand, a.suit):
                    w = check_least_high_card(a, player_teammate_hand)
                    if w is not None:
                        player_tm_set_play(False, w, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif w is None:
                        w1 = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                        player_tm_set_play(False, w1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(player_teammate_hand, a.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        w2 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, w2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        w3 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, w3, x_limit, cards, cards, cards, card_pos, card_pos,
                                           ply_tm_card_pos)
            elif a.suit != b.suit != c.suit:
                if have_suits(player_teammate_hand, a.suit):
                    d12 = check_least_high_card(a, player_teammate_hand)
                    if d12 is not None:
                        player_tm_set_play(False, d12, x_limit, cards, cards, cards, card_pos, card_pos,
                                           ply_tm_card_pos)
                    elif d12 is None:
                        d13 = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                        player_tm_set_play(False, d13, x_limit, cards, cards, cards, card_pos, card_pos,
                                           ply_tm_card_pos)
                elif have_suits(player_teammate_hand, a.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        d14 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, d14, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        d15 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, d15, x_limit, cards, cards, cards, card_pos, card_pos,
                                           ply_tm_card_pos)
        if a.suit != trump and b.suit != trump and c.suit == trump:
            if have_suits(player_teammate_hand, a.suit):
                e = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                player_tm_set_play(False, e, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif have_suits(player_teammate_hand, a.suit) is False:
                if len(player_teammate_trumps) > 0:
                    e1 = check_least_high_card(c, player_teammate_trumps)
                    if e1 is not None:
                        player_tm_set_play(True, e1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif e1 is None:
                        e2 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, e2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif len(player_teammate_trumps) == 0:
                    e3 = check_lowest_value_card(player_teammate_hand)
                    player_tm_set_play(False, e3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit != trump and b.suit == trump and c.suit != trump:
            if have_suits(player_teammate_hand, a.suit):
                f = check_lowest_value_card_of_suit(player_teammate_hand, a.suit)
                player_tm_set_play(False, f, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif have_suits(player_teammate_hand, a.suit) is False:
                if len(player_teammate_trumps) > 0:
                    f1 = check_least_high_card(b, player_teammate_trumps)
                    if f1 is not None:
                        player_tm_set_play(True, f1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif f1 is None:
                        f2 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, f2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif len(player_teammate_trumps) == 0:
                    f3 = check_lowest_value_card(player_teammate_hand)
                    player_tm_set_play(False, f3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit != trump and c.suit != trump:
            if len(player_teammate_trumps) > 0:
                g = check_least_high_card(a, player_teammate_trumps)
                if g is not None:
                    player_tm_set_play(True, g, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif g is None:
                    g1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, g1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                g2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, g2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit == trump and c.suit != trump:
            if len(player_teammate_trumps) > 0:
                h = check_least_high_card(compare_cards(a, b), player_teammate_trumps)
                if h is not None:
                    player_tm_set_play(True, h, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if h is None:
                    h1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, h1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                h2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, h2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit != trump and c.suit == trump:
            if len(player_teammate_trumps) > 0:
                i = check_least_high_card(compare_cards(a, c), player_teammate_trumps)
                if i is not None:
                    player_tm_set_play(True, i, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if i is None:
                    i1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, i1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                i2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, i2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit != trump and b.suit == trump and c.suit == trump:
            if len(player_teammate_trumps) > 0:
                j = check_least_high_card(compare_cards(b, c), player_teammate_trumps)
                if j is not None:
                    player_tm_set_play(True, j, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if j is None:
                    j1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, j1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                j2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, j2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit == trump and c.suit == trump:
            if len(player_teammate_trumps) > 0:
                k = check_least_high_card(compare_cards(compare_cards(a, b), c), player_teammate_trumps)
                if k is not None:
                    player_tm_set_play(True, k, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if k is None:
                    k1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, k1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                k2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, k2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
    if comp_played is False:
        s = player_played_hands[rnd]
        h = comp_teammate_played_hands[rnd]
        if s.suit != trump and h.suit != trump:
            if s.suit == h.suit:
                if have_suits(player_teammate_hand, s.suit):
                    m = check_least_high_card(compare_cards(s, h), player_teammate_hand)
                    if m is not None:
                        player_tm_set_play(False, m, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                    elif m is None:
                        m1 = check_lowest_value_card_of_suit(player_teammate_hand, s.suit)
                        player_tm_set_play(False, m1, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                elif have_suits(player_teammate_hand, s.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        m2 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, m2, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        m3 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, m3, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
            elif s.suit != h.suit:
                if have_suits(player_teammate_hand, s.suit):
                    m4 = check_least_high_card(s, player_teammate_hand)
                    if m4 is not None:
                        player_tm_set_play(False, m4, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                    if m4 is None:
                        m5 = check_lowest_value_card_of_suit(player_teammate_hand, s.suit)
                        player_tm_set_play(False, m5, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                elif have_suits(player_teammate_hand, s.suit) is False:
                    if len(player_teammate_trumps) > 0:
                        m6 = check_lowest_value_card(player_teammate_trumps)
                        player_tm_set_play(True, m6, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                    elif len(player_teammate_trumps) == 0:
                        m7 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, m7, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
        if s.suit != trump and h.suit == trump:
            if have_suits(player_teammate_hand, s.suit):
                n = check_lowest_value_card_of_suit(player_teammate_hand, s.suit)
                player_tm_set_play(False, n, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos, ply_tm_card_pos)
            elif have_suits(player_teammate_hand, s.suit) is False:
                if len(player_teammate_trumps) > 0:
                    n1 = check_least_high_card(h, player_teammate_trumps)
                    if n1 is not None:
                        player_tm_set_play(True, n1, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                    if n1 is None:
                        n2 = check_lowest_value_card(player_teammate_hand)
                        player_tm_set_play(False, n2, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                           ply_tm_card_pos)
                elif len(player_teammate_trumps) == 0:
                    n3 = check_lowest_value_card(player_teammate_hand)
                    player_tm_set_play(False, n3, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                       ply_tm_card_pos)
        if s.suit == trump and h.suit != trump:
            if len(player_teammate_trumps) > 0:
                o = check_least_high_card(s, player_teammate_trumps)
                if o is not None:
                    player_tm_set_play(True, o, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                       ply_tm_card_pos)
                elif o is None:
                    o1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, o1, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                       ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                o2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, o2, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                   ply_tm_card_pos)
        if s.suit == trump and h.suit == trump:
            if len(player_teammate_trumps) > 0:
                p = check_least_high_card(compare_cards(s, h), player_teammate_trumps)
                if p is not None:
                    player_tm_set_play(True, p, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                       ply_tm_card_pos)
                elif p is None:
                    p1 = check_lowest_value_card(player_teammate_trumps)
                    player_tm_set_play(True, p1, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                       ply_tm_card_pos)
            elif len(player_teammate_trumps) == 0:
                p2 = check_lowest_value_card(player_teammate_hand)
                player_tm_set_play(False, p2, x_limit, cards + 1, cards, cards, card_pos + 20, card_pos,
                                   ply_tm_card_pos)


def comp_play(first_play, rnd, ply_tm_card_pos):
    global comp_round_done
    x_limit = 920 - (75 * rnd)
    cards = 13 - rnd
    card_pos = 390 - (20 * rnd)
    rnd -= 1
    if first_play:
        clear_all_decks()
        if len(computer_hand) == 0:
            kk_1 = random.choice(comp_trumps)
            comp_set_play(True, kk_1, x_limit + 75, cards, cards+1, cards+1, card_pos, card_pos+20, ply_tm_card_pos)
        if len(computer_hand) > 0:
            k = random.choice(computer_hand)
            comp_set_play(False, k, x_limit + 75, cards, cards + 1, cards + 1, card_pos, card_pos + 20, ply_tm_card_pos)
    elif not first_play:
        a = player_played_hands[rnd]
        b = comp_teammate_played_hands[rnd]
        c = player_teammate_played_hands[rnd]
        if a.suit != trump and b.suit != trump and c.suit != trump:
            if a.suit == b.suit == c.suit:
                if have_suits(computer_hand, a.suit):
                    d = compare_cards(compare_cards(a, b), c)
                    d0 = check_least_high_card(d, computer_hand)
                    if d0 is not None:
                        comp_set_play(False, d0, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d0 is None:
                        d1 = check_lowest_value_card_of_suit(computer_hand, a.suit)
                        comp_set_play(False, d1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(computer_hand, a.suit) is False:
                    if len(comp_trumps) > 0:
                        d2 = check_lowest_value_card(comp_trumps)
                        comp_set_play(True, d2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(comp_trumps) == 0:
                        d3 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, d3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif a.suit == b.suit and b.suit != c.suit:
                if have_suits(computer_hand, a.suit):
                    d4 = check_least_high_card(compare_cards(a, b), computer_hand)
                    if d4 is not None:
                        comp_set_play(False, d4, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d4 is None:
                        d5 = check_lowest_value_card_of_suit(computer_hand, a.suit)
                        comp_set_play(False, d5, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(computer_hand, a.suit) is False:
                    if len(comp_trumps) > 0:
                        d6 = check_lowest_value_card(comp_trumps)
                        comp_set_play(True, d6, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(comp_trumps) == 0:
                        d7 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, d7, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif a.suit == c.suit and c.suit != b.suit:
                if have_suits(computer_hand, a.suit):
                    d8 = check_least_high_card(compare_cards(a, c), computer_hand)
                    if d8 is not None:
                        comp_set_play(False, d8, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d8 is None:
                        d9 = check_lowest_value_card_of_suit(computer_hand, a.suit)
                        comp_set_play(False, d9, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(computer_hand, a.suit) is False:
                    if len(comp_trumps) > 0:
                        d10 = check_lowest_value_card(comp_trumps)
                        comp_set_play(True, d10, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(comp_trumps) == 0:
                        d11 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, d11, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif a.suit != b.suit and b.suit == c.suit:
                if have_suits(computer_hand, a.suit):
                    m = check_least_high_card(a, computer_hand)
                    if m is not None:
                        comp_set_play(False, m, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif m is None:
                        m1 = check_lowest_value_card_of_suit(computer_hand, a.suit)
                        comp_set_play(False, m1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(computer_hand, a.suit) is False:
                    if len(comp_trumps) > 0:
                        m2 = check_lowest_value_card(comp_trumps)
                        comp_set_play(True, m2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(comp_trumps) == 0:
                        m3 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, m3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif a.suit != b.suit != c.suit:
                if have_suits(computer_hand, a.suit):
                    d12 = check_least_high_card(a, computer_hand)
                    if d12 is not None:
                        comp_set_play(False, d12, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif d12 is None:
                        d13 = check_lowest_value_card_of_suit(computer_hand, a.suit)
                        comp_set_play(False, d13, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif have_suits(computer_hand, a.suit) is False:
                    if len(comp_trumps) > 0:
                        d14 = check_lowest_value_card(comp_trumps)
                        comp_set_play(True, d14, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif len(comp_trumps) == 0:
                        d15 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, d15, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit != trump and b.suit != trump and c.suit == trump:
            if have_suits(computer_hand, a.suit):
                e = check_lowest_value_card_of_suit(computer_hand, a.suit)
                comp_set_play(False, e, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif have_suits(computer_hand, a.suit) is False:
                if len(comp_trumps) > 0:
                    e1 = check_least_high_card(c, comp_trumps)
                    if e1 is not None:
                        comp_set_play(True, e1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif e1 is None:
                        e2 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, e2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif len(comp_trumps) == 0:
                    e3 = check_lowest_value_card(computer_hand)
                    comp_set_play(False, e3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit != trump and b.suit == trump and c.suit != trump:
            if have_suits(computer_hand, a.suit):
                f = check_lowest_value_card_of_suit(computer_hand, a.suit)
                comp_set_play(False, f, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif have_suits(computer_hand, a.suit) is False:
                if len(comp_trumps) > 0:
                    f1 = check_least_high_card(b, comp_trumps)
                    if f1 is not None:
                        comp_set_play(True, f1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                    elif f1 is None:
                        f2 = check_lowest_value_card(computer_hand)
                        comp_set_play(False, f2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif len(comp_trumps) == 0:
                    f3 = check_lowest_value_card(computer_hand)
                    comp_set_play(False, f3, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit != trump and c.suit != trump:
            if len(comp_trumps) > 0:
                g = check_least_high_card(a, comp_trumps)
                if g is not None:
                    comp_set_play(True, g, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                elif g is None:
                    g1 = check_lowest_value_card(comp_trumps)
                    comp_set_play(True, g1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_trumps) == 0:
                g2 = check_lowest_value_card(computer_hand)
                comp_set_play(False, g2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit == trump and c.suit != trump:
            if len(comp_trumps) > 0:
                h = check_least_high_card(compare_cards(a, b), comp_trumps)
                if h is not None:
                    comp_set_play(True, h, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if h is None:
                    h1 = check_lowest_value_card(comp_trumps)
                    comp_set_play(True, h1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_trumps) == 0:
                h2 = check_lowest_value_card(computer_hand)
                comp_set_play(False, h2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit != trump and c.suit == trump:
            if len(comp_trumps) > 0:
                i = check_least_high_card(compare_cards(a, c), comp_trumps)
                if i is not None:
                    comp_set_play(True, i, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if i is None:
                    i1 = check_lowest_value_card(comp_trumps)
                    comp_set_play(True, i1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_trumps) == 0:
                i2 = check_lowest_value_card(computer_hand)
                comp_set_play(False, i2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit != trump and b.suit == trump and c.suit == trump:
            if len(comp_trumps) > 0:
                j = check_least_high_card(compare_cards(b, c), comp_trumps)
                if j is not None:
                    comp_set_play(True, j, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if j is None:
                    j1 = check_lowest_value_card(comp_trumps)
                    comp_set_play(True, j1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_trumps) == 0:
                j2 = check_lowest_value_card(computer_hand)
                comp_set_play(False, j2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
        if a.suit == trump and b.suit == trump and c.suit == trump:
            if len(comp_trumps) > 0:
                k = check_least_high_card(compare_cards(compare_cards(a, b), c), comp_trumps)
                if k is not None:
                    comp_set_play(True, k, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
                if k is None:
                    k1 = check_lowest_value_card(comp_trumps)
                    comp_set_play(True, k1, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)
            elif len(comp_trumps) == 0:
                k2 = check_lowest_value_card(computer_hand)
                comp_set_play(False, k2, x_limit, cards, cards, cards, card_pos, card_pos, ply_tm_card_pos)


def check_won_hand(rnd):
    global comp_won_hands, player_won_hands, comp_tm_won_hands, player_tm_won_hands
    rnd -= 1
    compare_list = []
    a = comp_played_hands[rnd]
    compare_list.append(a)
    b = player_played_hands[rnd]
    compare_list.append(b)
    c = comp_teammate_played_hands[rnd]
    compare_list.append(c)
    d = player_teammate_played_hands[rnd]
    compare_list.append(d)
    # if comp_round_done and player_round_done and comp_tm_round_done and player_tm_round_done:
    if comp_trump_selected:
        if a.suit != trump and b.suit != trump and c.suit != trump and d.suit != trump:
            e = check_highest_value_card_of_suit(compare_list, a.suit)
            if e == a:
                comp_won_hands += 1
                return 'comp'
            elif e == b:
                player_won_hands += 1
                return 'player'
            elif e == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif e == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit != trump and c.suit != trump and d.suit == trump:
            player_tm_won_hands += 1
            return 'player_tm'
        elif a.suit != trump and b.suit != trump and c.suit == trump and d.suit != trump:
            comp_tm_won_hands += 1
            return 'comp_tm'
        elif a.suit != trump and b.suit == trump and c.suit != trump and d.suit != trump:
            player_won_hands += 1
            return 'player'
        elif a.suit == trump and b.suit != trump and c.suit != trump and d.suit != trump:
            comp_won_hands += 1
            return 'comp'
        elif a.suit == trump and b.suit == trump and c.suit != trump and d.suit != trump:
            e1 = compare_cards(a, b)
            if e1 == a:
                comp_won_hands += 1
                return 'comp'
            elif e1 == b:
                player_won_hands += 1
                return 'player'
        elif a.suit == trump and b.suit != trump and c.suit == trump and d.suit != trump:
            e2 = compare_cards(a, c)
            if e2 == a:
                comp_won_hands += 1
                return 'comp'
            elif e2 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
        elif a.suit == trump and b.suit != trump and c.suit != trump and d.suit == trump:
            e3 = compare_cards(a, d)
            if e3 == a:
                comp_won_hands += 1
                return 'comp'
            elif e3 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit == trump and c.suit == trump and d.suit != trump:
            e4 = compare_cards(b, c)
            if e4 == b:
                player_won_hands += 1
                return 'player'
            elif e4 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
        elif a.suit != trump and b.suit == trump and c.suit != trump and d.suit == trump:
            e5 = compare_cards(b, d)
            if e5 == b:
                player_won_hands += 1
                return 'player'
            elif e5 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit != trump and c.suit == trump and d.suit == trump:
            e6 = compare_cards(c, d)
            if e6 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif e6 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit == trump and b.suit == trump and c.suit == trump and d.suit != trump:
            f = compare_cards(compare_cards(a, b), c)
            if f == a:
                comp_won_hands += 1
                return 'comp'
            elif f == b:
                player_won_hands += 1
                return 'player'
            elif f == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
        elif a.suit == trump and b.suit == trump and c.suit != trump and d.suit == trump:
            f1 = compare_cards(compare_cards(a, b), d)
            if f1 == a:
                comp_won_hands += 1
                return 'comp'
            elif f1 == b:
                player_won_hands += 1
                return 'player'
            elif f1 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit == trump and b.suit != trump and c.suit == trump and d.suit == trump:
            f2 = compare_cards(compare_cards(a, c), d)
            if f2 == a:
                comp_won_hands += 1
                return 'comp'
            elif f2 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif f2 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit == trump and c.suit == trump and d.suit == trump:
            f3 = compare_cards(compare_cards(b, c), d)
            if f3 == b:
                player_won_hands += 1
                return 'player'
            elif f3 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif f3 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit == trump and b.suit == trump and c.suit == trump and d.suit == trump:
            f4 = check_highest_value_card(compare_list)
            if f4 == a:
                comp_won_hands += 1
                return 'comp'
            elif f4 == b:
                player_won_hands += 1
                return 'player'
            elif f4 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif f4 == d:
                player_tm_won_hands += 1
                return 'player_tm'
    elif player_trump_selected:
        if a.suit != trump and b.suit != trump and c.suit != trump and d.suit != trump:
            e = check_highest_value_card_of_suit(compare_list, b.suit)
            if e == a:
                comp_won_hands += 1
                return 'comp'
            elif e == b:
                player_won_hands += 1
                return 'player'
            elif e == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif e == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit != trump and c.suit != trump and d.suit == trump:
            player_tm_won_hands += 1
            return 'player_tm'
        elif a.suit != trump and b.suit != trump and c.suit == trump and d.suit != trump:
            comp_tm_won_hands += 1
            return 'comp_tm'
        elif a.suit != trump and b.suit == trump and c.suit != trump and d.suit != trump:
            player_won_hands += 1
            return 'player'
        elif a.suit == trump and b.suit != trump and c.suit != trump and d.suit != trump:
            comp_won_hands += 1
            return 'comp'
        elif a.suit == trump and b.suit == trump and c.suit != trump and d.suit != trump:
            e1 = compare_cards(a, b)
            if e1 == a:
                comp_won_hands += 1
                return 'comp'
            elif e1 == b:
                player_won_hands += 1
                return 'player'
        elif a.suit == trump and b.suit != trump and c.suit == trump and d.suit != trump:
            e2 = compare_cards(a, c)
            if e2 == a:
                comp_won_hands += 1
                return 'comp'
            elif e2 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
        elif a.suit == trump and b.suit != trump and c.suit != trump and d.suit == trump:
            e3 = compare_cards(a, d)
            if e3 == a:
                comp_won_hands += 1
                return 'comp'
            elif e3 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit == trump and c.suit == trump and d.suit != trump:
            e4 = compare_cards(b, c)
            if e4 == b:
                player_won_hands += 1
                return 'player'
            elif e4 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
        elif a.suit != trump and b.suit == trump and c.suit != trump and d.suit == trump:
            e5 = compare_cards(b, d)
            if e5 == b:
                player_won_hands += 1
                return 'player'
            elif e5 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit != trump and c.suit == trump and d.suit == trump:
            e6 = compare_cards(c, d)
            if e6 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif e6 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit == trump and b.suit == trump and c.suit == trump and d.suit != trump:
            f = compare_cards(compare_cards(a, b), c)
            if f == a:
                comp_won_hands += 1
                return 'comp'
            elif f == b:
                player_won_hands += 1
                return 'player'
            elif f == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
        elif a.suit == trump and b.suit == trump and c.suit != trump and d.suit == trump:
            f1 = compare_cards(compare_cards(a, b), d)
            if f1 == a:
                comp_won_hands += 1
                return 'comp'
            elif f1 == b:
                player_won_hands += 1
                return 'player'
            elif f1 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit == trump and b.suit != trump and c.suit == trump and d.suit == trump:
            f2 = compare_cards(compare_cards(a, c), d)
            if f2 == a:
                comp_won_hands += 1
                return 'comp'
            elif f2 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif f2 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit != trump and b.suit == trump and c.suit == trump and d.suit == trump:
            f3 = compare_cards(compare_cards(b, c), d)
            if f3 == b:
                player_won_hands += 1
                return 'player'
            elif f3 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif f3 == d:
                player_tm_won_hands += 1
                return 'player_tm'
        elif a.suit == trump and b.suit == trump and c.suit == trump and d.suit == trump:
            f4 = check_highest_value_card(compare_list)
            if f4 == a:
                comp_won_hands += 1
                return 'comp'
            elif f4 == b:
                player_won_hands += 1
                return 'player'
            elif f4 == c:
                comp_tm_won_hands += 1
                return 'comp_tm'
            elif f4 == d:
                player_tm_won_hands += 1
                return 'player_tm'


x1 = 90
y1 = 260
x2 = 250
y2 = 480
x3 = 820
y3 = 260
x4 = 250
y4 = 130


def comp_win_cords():
    global x1, y1
    x1 += 80
    if x1 > 330:
        x1 = 90
        y1 = 325
    elif x1 > 330 and y1 == 315:
        x1 = 90
        y1 = 395
    elif x1 > 330 and y1 == 385:
        x1 = 90
        y1 = 465
    elif x1 > 330 and y1 == 455:
        x1 = 90
        y1 = 535


def comp_tm_win_cords():
    global x3, y3
    x3 -= 80
    if x3 < 580:
        x3 = 820
        y3 = 325
    elif x3 < 580 and y3 == 315:
        x3 = 820
        y3 = 395
    elif x3 < 580 and y3 == 385:
        x3 = 820
        y3 = 465
    elif x3 < 580 and y3 == 455:
        x3 = 820
        y3 = 535


def player_win_cord():
    global x2, y2
    x2 += 80
    if x2 > 570:
        x2 = 250
        y2 = 415
    elif x2 > 570 and y2 == 415:
        x2 = 250
        y2 = 345


def player_tm_win_cord():
    global x4, y4
    x4 += 80
    if x4 > 570:
        x4 = 250
        y4 = 195
    elif x4 > 410 and y4 == 200:
        x4 = 250
        y4 = 265


def set_won_hand(rnd, hand_winner):
    global x1, y1, x2, y2, x3, y3, x4, y4
    rnd -= 1
    if comp_trump_selected:
        if hand_winner == 'comp':
            match_cards(comp_played_hands[rnd], x1, y1)
            match_cards(player_played_hands[rnd], x1+10, y1)
            match_cards(comp_teammate_played_hands[rnd], x1+20, y1)
            match_cards(player_teammate_played_hands[rnd], x1+30, y1)
            comp_win_cords()
        elif hand_winner == 'player':
            match_cards(comp_played_hands[rnd], x2, y2)
            match_cards(player_played_hands[rnd], x2+10, y2)
            match_cards(comp_teammate_played_hands[rnd], x2+20, y2)
            match_cards(player_teammate_played_hands[rnd], x2+30, y2)
            player_win_cord()
        elif hand_winner == 'comp_tm':
            match_cards(comp_played_hands[rnd], x3, y3)
            match_cards(player_played_hands[rnd], x3+10, y3)
            match_cards(comp_teammate_played_hands[rnd], x3+20, y3)
            match_cards(player_teammate_played_hands[rnd], x3+30, y3)
            comp_tm_win_cords()
        elif hand_winner == 'player_tm':
            match_cards(comp_played_hands[rnd], x4, y4)
            match_cards(player_played_hands[rnd], x4+10, y4)
            match_cards(comp_teammate_played_hands[rnd], x4+20, y4)
            match_cards(player_teammate_played_hands[rnd], x4+30, y4)
            player_tm_win_cord()
    elif player_trump_selected:
        if hand_winner == 'comp':
            match_cards(player_played_hands[rnd], x1, y1)
            match_cards(comp_teammate_played_hands[rnd], x1+10, y1)
            match_cards(player_teammate_played_hands[rnd], x1+20, y1)
            match_cards(comp_played_hands[rnd], x1+30, y1)
            comp_win_cords()
        elif hand_winner == 'player':
            match_cards(player_played_hands[rnd], x2, y2)
            match_cards(comp_teammate_played_hands[rnd], x2+10, y2)
            match_cards(player_teammate_played_hands[rnd], x2+20, y2)
            match_cards(comp_played_hands[rnd], x2+30, y2)
            player_win_cord()
        elif hand_winner == 'comp_tm':
            match_cards(player_played_hands[rnd], x3, y3)
            match_cards(comp_teammate_played_hands[rnd], x3+10, y3)
            match_cards(player_teammate_played_hands[rnd], x3+20, y3)
            match_cards(comp_played_hands[rnd], x3+30, y3)
            comp_tm_win_cords()
        elif hand_winner == 'player_tm':
            match_cards(player_played_hands[rnd], x4, y4)
            match_cards(comp_teammate_played_hands[rnd], x4+10, y4)
            match_cards(player_teammate_played_hands[rnd], x4+20, y4)
            match_cards(comp_played_hands[rnd], x4+30, y4)
            player_tm_win_cord()


def play_round(rnd):
    global round_status
    x_limit = 920 - (75*rnd)
    turn = 14 - rnd
    c1 = 14 - rnd
    c2 = 14 - rnd
    c3 = 14 - rnd
    c1_pos = 410 - (20*rnd)
    c2_pos = 410 - (20*rnd)
    c3_pos = 610 - (20*rnd)
    if comp_trump_selected and comp_round_done is False:
        comp_play(True, rnd, c3_pos)
    if player_trump_selected and player_round_done is False:
        player_play(True, rnd, turn, x_limit, c1, c2, c3,  c1_pos, c2_pos, c3_pos)
    if comp_round_done and player_round_done is False:
        player_play(False, rnd, turn, x_limit, c1-1, c2, c3, c1_pos-20, c2_pos, c3_pos)
        if player_round_done:
            comp_tm_play(True, rnd, c3_pos)
            if comp_tm_round_done:
                player_tm_play(True, rnd, c3_pos-20)
    if player_round_done and comp_round_done is False:
        if comp_tm_round_done is False:
            comp_tm_play(False, rnd, c3_pos)
            if comp_tm_round_done:
                player_tm_play(False, rnd, c3_pos-20)
                if player_tm_round_done:
                    comp_play(False, rnd, c3_pos-20)
    if player_tm_round_done and player_round_done and comp_round_done and comp_tm_round_done:
        winner = check_won_hand(rnd)
        set_won_hand(rnd, winner)
        round_status['round'+str(rnd)] = True


def check_rounds_completed():
    global all_rounds_done
    for j in range(1, 14):
        if round_status['round'+str(j)] is True:
            all_rounds_done = True
        else:
            all_rounds_done = False
            break


def declare_won_hands():
    declare_comp_hands = font.render("Computer has won " + str(comp_won_hands) + " hands", True, (255, 255, 255))
    declare_comp_hands = pygame.transform.rotate(declare_comp_hands, 90)
    declare_player_hands = font.render(player_information[0].upper() + " has won " + str(player_won_hands) + " hands",
                                       True, (0, 150, 255))
    declare_comp_tm_hands = font.render("Computer teammate has won " + str(comp_tm_won_hands) + " hands", True,
                                        (255, 255, 255))
    declare_comp_tm_hands = pygame.transform.rotate(declare_comp_tm_hands, 270)
    declare_player_tm_hands = font.render(player_information[0].upper() + " teammate has won " +
                                          str(player_tm_won_hands) + " hands", True, (0, 150, 255))
    win.blit(declare_player_hands, (370, 580))
    win.blit(declare_player_tm_hands, (370, 60))
    win.blit(declare_comp_hands, (40, 180))
    win.blit(declare_comp_tm_hands, (930, 160))


def show_winner():
    a = comp_won_hands
    b = player_won_hands
    c = comp_tm_won_hands
    d = player_tm_won_hands
    total_player_won = b + d
    total_comp_won = a + c
    winner_player = font.render(player_information[0].upper() + " HAS WON WITH A TOTAL HANDS OF " + str(total_player_won), True, (0, 150, 255))
    winner_comp = font.render("COMP HAS WON WITH A TOTAL HANDS OF " + str(total_comp_won), True, (255, 255, 255))
    match_draw = font.render("ITS A DRAW", True, (255, 255, 255))
    if total_player_won > total_comp_won:
        win.blit(winner_player, (250, 400))
    elif total_player_won < total_comp_won:
        win.blit(winner_comp, (250, 400))
    elif total_comp_won == total_player_won:
        win.blit(match_draw, (300, 400))


def start_play():
    global all_rounds_done
    if trump_list_chosen is False:
        trump_list()
    if round_status['round1'] is False:
        play_round(1)
        start_new_round()
    for i in range(2, 13):
        if round_status['round' + str(i)] is False and round_status['round' + str(i - 1)]:
            play_round(i)
            start_new_round()
    if round_status['round13'] is False and round_status['round12']:
        play_round(13)
    check_rounds_completed()
    if all_rounds_done:
        play_area_clear()
        declare_won_hands()
        show_winner()







    # if round_status['round2'] is False and round_status['round1']:
    #     play_round(2)
    #     start_new_round()
    # if round_status['round3'] is False and round_status['round2']:
    #     play_round(3)
    #     start_new_round()
    # if round_status['round4'] is False and round_status['round3']:
    #     play_round(4)
    #     start_new_round()
    # if round_status['round5'] is False and round_status['round4']:
    #     play_round(5)
    #     start_new_round()
    # if round_status['round6'] is False and round_status['round5']:
    #     play_round(6)
    #     start_new_round()
    # if round_status['round7'] is False and round_status['round6']:
    #     play_round(7)
    #     start_new_round()
    # if round_status['round8'] is False and round_status['round7']:
    #     play_round(8)
    #     start_new_round()
    # if round_status['round9'] is False and round_status['round8']:
    #     play_round(9)
    #     start_new_round()
    # if round_status['round10'] is False and round_status['round9']:
    #     play_round(10)
    #     start_new_round()
    # if round_status['round11'] is False and round_status['round10']:
    #     play_round(11)
    #     start_new_round()
    # if round_status['round12'] is False and round_status['round11']:
    #     play_round(12)
    #     start_new_round()
    # if round_status['round13'] is False and round_status['round12']:
    #     play_round(13)
    #     print(comp_won_hands, player_won_hands, comp_tm_won_hands, player_tm_won_hands)


if check_for_quit:
    run = False
else:
    run = True

while run:
    initialize_game()
    start_play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


