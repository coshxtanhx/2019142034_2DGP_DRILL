from pico2d import *

class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir = 0 #정지 상태
        self.timer = 1111 #타이머 초기화
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1 #시간 감소
        if(self.timer == 0): #시간이 다 되면
            self.add_event(TIMER) #타이머 이벤트를 큐에 삽입

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        

class RUN:
    def enter(self, event):
        self.dir = 0
        #어떤 이벤트 때문에 RUN으로 들어왔는지 파악 후
        #그 이벤트에 따라서 실제 방향 결정하기
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self):
        # RUN 상태를 나갈 때 현재 방향을 저장해 놓기
        self.face_dir = self.dir

    def do(self):
        # 달리게 만들어 준다
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class ARUN:
    def enter(self, event):
        self.dir = self.face_dir
        pass
        #어떤 이벤트 때문에 RUN으로 들어왔는지 파악 후
        #그 이벤트에 따라서 실제 방향 결정하기
        # if event == RD:
        #     self.dir += 1
        # elif event == LD:
        #     self.dir -= 1
        # elif event == RU:
        #     self.dir -= 1
        # elif event == LU:
        #     self.dir += 1

    def exit(self):
        # RUN 상태를 나갈 때 현재 방향을 저장해 놓기
        self.face_dir = self.dir

    def do(self):
        # 달리게 만들어 준다
        self.frame = (self.frame + 1) % 8
        self.x += self.dir

        if(self.x < 0):
            self.x = 0
            self.dir *= -1
        elif(self.x > 800):
            self.x = 800
            self.dir *= -1

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    @staticmethod
    def enter(self, event):
        self.dir = 0 #정지 상태
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, \
                -3.141592/2, '', self.x+25, self.y-25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, \
                +3.141592/2, '',self.x-25, self.y-25, 100, 100)

RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_a): AD
}

next_state = {
    ARUN: {RU: ARUN, LU: ARUN, RD: RUN, LD: RUN, TIMER: ARUN, AD: IDLE},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: ARUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, TIMER: RUN, AD: ARUN}
}

class Boy:
    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        if(self.q):
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.q = []
        #초기 상태 설정과 entry 액션 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)