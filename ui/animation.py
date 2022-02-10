import threading
import time

BACKGROUND_COLOR = "#f6fbfe"
#CIRCLE_FILL = "#01a6ed"
CIRCLE_FILL = "#e6077d"
#CIRCLE_FILL = "#e94324"
#CIRCLE_FILL = "#00c1ff"
CIRCLE_FILL_NEG = "#00c1ff"
CIRCLE_INITIAL_RADIUS = 700 # or is it diameter (?)
CIRCLE_RADIUS_GROW_PER_FRAME = 8
ANIMATION_FPS = 60
ANIMATION_FRAME_COUNT = 175
END_POLL_SLEEP = 0.5

def get_circle_coords(x, y, r):
    return (
        x - r, # x1
        y - r, # y1
        x + r, # x2
        y + r  # y2
    )


def create_circle(x, y, r, canvas, **kwargs):
    x1, y1, x2, y2 = get_circle_coords(x, y, r) 

    return canvas.create_oval(x1, y1, x2, y2, **kwargs)

def update_circle(circle_id, canvas, x, y, initial_radius, bg_after):
    radius = initial_radius

    frame_count = 0
    while frame_count <= ANIMATION_FRAME_COUNT:
        should_sleep = (1 / ANIMATION_FPS) # not sure about the math
        time.sleep(should_sleep)

        x1, y1, x2, y2 = get_circle_coords(x, y, radius)
        canvas.coords(circle_id, x1, y1, x2, y2)

        if radius < 0:
            canvas.itemconfig(circle_id, fill=CIRCLE_FILL_NEG)

        radius -= CIRCLE_RADIUS_GROW_PER_FRAME
        frame_count += 1

    # Clear the circle once animation over
    canvas.delete(circle_id)

    # Reset the background color
    canvas.configure(bg=bg_after)

def start_update_loop(circle_id, canvas, x, y, r, bg_after):
    thread = threading.Thread(
        target=update_circle,
        args=(circle_id, canvas, x, y, r, bg_after)
    )
    thread.start()

    return thread

def start_end_poll_loop(draw_thread, execute_after):
    def poll():
        while True:
            time.sleep(END_POLL_SLEEP) # it still blocks; gotta switch to multiprocessing

            if not draw_thread.is_alive():
                break

        # It died; we may run the callback now
        execute_after()

    # Start the thread
    threading.Thread(target=poll).start()
    
def start_animation(canvas, window_width, window_height, execute_after=None, bg_after=None):
    x = window_width // 2
    y = window_height // 2
    r = CIRCLE_INITIAL_RADIUS

    canvas.configure(bg=BACKGROUND_COLOR)

    circle_id = create_circle(
        x,
        y,
        r,
        canvas,
        fill=CIRCLE_FILL,
        outline=BACKGROUND_COLOR
    )

    # Start a background update thread
    update_circle_thread = start_update_loop(
        circle_id,
        canvas,
        x,
        y,
        r,
        bg_after=bg_after or "white"
    )
    
    # Spawn another thread which waits until update thread has died (?);
    # Run the `execute_after` function after detected
    if execute_after:
        start_end_poll_loop(update_circle_thread, execute_after)
