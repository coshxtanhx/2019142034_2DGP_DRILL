from pico2d import *
import logo_state
import play_state
import title_state

states = [logo_state, title_state, play_state]

for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        delay(0.05)
    state.exit()
    close_canvas()