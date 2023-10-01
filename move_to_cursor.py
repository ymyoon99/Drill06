from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
char = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def handle_events():
    global running, cursor_x, cursor_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            exit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            points.append((event.x, TUK_HEIGHT - 1 - event.y))

def cursor_move(x, y):
    global points

    cursor.draw(cursor_x, cursor_y)
    for n in points:
        cursor.draw(n[0], n[1])

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
cursor_x, cursor_y = 0, 0
points = []

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    char.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    cursor_move(cursor_x, cursor_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()