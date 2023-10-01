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

def cursor_point():
    global points

    cursor.draw(cursor_x, cursor_y)
    for n in points:
        cursor.draw(n[0], n[1])

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
frame2 = 0
cursor_x, cursor_y = 0, 0
points = []

def char_move_to_cursor():
    global frame, frame2
    global x, y

    if len(points) > 0:  
        cursor_x, cursor_y = points[0]
    else:
        cursor_x, cursor_y = TUK_WIDTH // 2, TUK_HEIGHT // 2

    t = 1 / 100
    x = (1 - t) * x + t * cursor_x
    y = (1 - t) * y + t * cursor_y

    if x > cursor_x:  # 왼쪽으로 이동할 때 char.clip_draw 함수 내의 y좌표 조정
            frame2 = 0
    else:
            frame2 = 1

    char.clip_draw(frame * 100, frame2 * 100, 100, 100, x, y)
    frame = (frame + 1) % 8
    frame2 = (frame2 + 1) % 8
    delay(0.05)


while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    char_move_to_cursor()
    cursor_point()
    update_canvas()
    frame = (frame + 1) % 8
    frame2 = (frame2 + 1) % 8
    handle_events()

close_canvas()