from pygame.locals import *
import sys
import pygame
import random
import time


WIDTH  = 640        # 幅
HEIGHT = 400        # 高さ

WALL_COUNT = 2
BALL_COUNT = 10
TARGET_COUNT = 10

class top_app():

    def __init__(self):
        pygame.init()
        self.main_surface = pygame.display.set_mode((500, 500)) 
        self.by0 =400
        self.by1 =400
        self.by2 =400
        self.x3=300
        self.y3 =400
        self.target_size=8
        self.wall_size=40
        self.xy0state=0    
        self.khit=0
        self.state = 0
        self.hit_count=0
        self.stop=1
        self.hit=[0,1,2,3,4,5,6,7,8,9]
        self.state = 0
        self.kstate = 0
        self.xstate=[0,1,2,3,4,5,6,7,8,9]
        self.ystate=[0,1,2,3,4,5,6,7,8,9]
        self.x_wall=100
        self.y_wall=100
        self.xwall_state=0
        self.wall_hit = 0
        self.dummy_hit = 0

        self.bxt=[0,1,2,3,4,5,6,7,8,9]
        self.byt=[0,1,2,3,4,5,6,7,8,9]
        self.xk=[0,1,2,3,4,5,6,7,8,9]
        self.yk=[0,1,2,3,4,5,6,7,8,9]
        self.x=[0,1,2,3,4,5,6,7,8,9]
        self.y=[0,1,2,3,4,5,6,7,8,9]
        self.dummy_x=[0,1,2,3,4,5,6,7,8,9]
        self.dummy_y=[0,1,2,3,4,5,6,7,8,9]
        self.xkstate=[0,1,2,3,4,5,6,7,8,9]
        self.ykstate=[0,1,2,3,4,5,6,7,8,9]
        self.scenario_state=0
        self.timeout=0

        self.loop_count=0

        for i in range(BALL_COUNT):
            self.bxt[i]=300
            self.byt[i]=400
            self.xk[i]=150
            self.yk[i]=30
            self.x[i]=150
            self.y[i]=30
            self.dummy_x[i]=150
            self.dummy_y[i]=100
            self.xkstate[i]=0    
            self.ykstate[i]=0    
            self.xstate[i]=0    
            self.ystate[i]=0    
            self.hit[i]=0
            self.dummy_x[i]=self.x_wall
            self.dummy_y[i]=self.y_wall


    def main(self):
        
        self.game_loop()

        pygame.quit()
        sys.exit()

    def hit_check(self):
        for j in range(BALL_COUNT):
            for i in range(TARGET_COUNT):
                if(((self.bxt[j]>(self.x[i]-self.target_size-10))and(self.bxt[j]<(self.x[i]+self.target_size+10)))
                and((self.byt[j]>(self.y[i]-10))and(self.byt[j]<(self.y[i]+10)))):
                    self.hit[i]=1

    def wall_col_check(self):
        for j in range(BALL_COUNT):
            if(((self.bxt[j]>(self.x_wall-self.target_size))and(self.bxt[j]<(self.x_wall+self.target_size+50)))
                and((self.byt[j]>(self.y_wall-10))and(self.byt[j]<(self.y_wall+10)))):
               self.wall_hit = 1

    def dummy_col_check(self):
        for j in range(BALL_COUNT):
            if(((self.dummy_x[j]>(self.x3-50))and(self.dummy_x[j]<(self.x3)))
                and((self.dummy_y[j]>(400-10))and(self.dummy_y[j]<(400+10)))):
               self.dummy_hit = 1

    def all_hit(self):
        for i in range(TARGET_COUNT):
            if (self.hit[i]==0):
                return 0       
            else:
                pass
        return 1

    def make_wall(self):
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+10, self.y_wall-10,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+20, self.y_wall-20,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+20, self.y_wall-10,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+30, self.y_wall-10,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall, self.y_wall,50,10))
            
    def make_target(self):
        for i in range(TARGET_COUNT):
            if(self.hit[i]==0):
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i], self.y[i]), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]-8, self.y[i]-8), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]-8, self.y[i]+8), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]+8, self.y[i]-8), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]+8, self.y[i]+8), self.target_size)
                pygame.draw.circle(self.main_surface, (0,0,0), (self.x[i], self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]+8, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]-8, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]+16, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]-16, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]+24, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]-24, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,0,0), (self.x[i], self.y[i]+24), self.target_size)
                pygame.draw.circle(self.main_surface, (0,0,0), (self.x[i], self.y[i]+32), self.target_size)
            else:
                pass
                

    def make_target2(self):
        for i in range(TARGET_COUNT):
            if(self.hit[i]==0):
                pygame.draw.rect(self.main_surface,(247, 247, 247) , (self.x[i]+0*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(246, 247, 249) , (self.x[i]+1*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(255, 243, 253) , (self.x[i]+2*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(235, 195, 46) , (self.x[i]+3*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(240, 219, 68) , (self.x[i]+4*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(243, 213, 67) , (self.x[i]+5*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(245, 210, 64) , (self.x[i]+6*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(227, 181, 36) , (self.x[i]+7*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(233, 218, 161) , (self.x[i]+8*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(246, 246, 244) , (self.x[i]+9*5, self.y[i],5,5))
                pygame.draw.rect(self.main_surface,(248, 246, 247) , (self.x[i]+0*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(245, 245, 243) , (self.x[i]+1*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(234, 191, 50) , (self.x[i]+2*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(239, 218, 67) , (self.x[i]+3*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(239, 213, 64) , (self.x[i]+4*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 206, 60) , (self.x[i]+5*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 203, 58) , (self.x[i]+6*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(231, 200, 57) , (self.x[i]+7*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(248, 238, 106) , (self.x[i]+8*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(244, 231, 179) , (self.x[i]+9*5, self.y[i]+10/2,5,5))
                pygame.draw.rect(self.main_surface,(244, 250, 240) , (self.x[i]+0*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(236, 197, 60) , (self.x[i]+1*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(239, 215, 67) , (self.x[i]+2*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(240, 213, 64) , (self.x[i]+3*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 210, 60) , (self.x[i]+4*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(238, 202, 54) , (self.x[i]+5*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 201, 54) , (self.x[i]+6*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(238, 198, 51) , (self.x[i]+7*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(237, 194, 56) , (self.x[i]+8*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 208, 92) , (self.x[i]+9*5, self.y[i]+20/2,5,5))
                pygame.draw.rect(self.main_surface,(255, 244, 248) , (self.x[i]+0*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(239, 201, 54) , (self.x[i]+1*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(238, 211, 62) , (self.x[i]+2*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(240, 205, 59) , (self.x[i]+3*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 201, 54) , (self.x[i]+4*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(240, 200, 50) , (self.x[i]+5*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(239, 201, 56) , (self.x[i]+6*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(233, 192, 48) , (self.x[i]+7*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(234, 191, 50) , (self.x[i]+8*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(252, 241, 100) , (self.x[i]+9*5, self.y[i]+30/2,5,5))
                pygame.draw.rect(self.main_surface,(242, 249, 242) , (self.x[i]+0*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(239, 211, 65) , (self.x[i]+1*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(240, 205, 59) , (self.x[i]+2*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(238, 200, 53) , (self.x[i]+3*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 199, 51) , (self.x[i]+4*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(242, 201, 57) , (self.x[i]+5*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(232, 191, 47) , (self.x[i]+6*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(233, 188, 45) , (self.x[i]+7*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(228, 185, 44) , (self.x[i]+8*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(230, 183, 41) , (self.x[i]+9*5, self.y[i]+40/2,5,5))
                pygame.draw.rect(self.main_surface,(242, 246, 255) , (self.x[i]+0*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(236, 191, 46) , (self.x[i]+1*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(242, 201, 51) , (self.x[i]+2*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(242, 197, 52) , (self.x[i]+3*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(238, 196, 52) , (self.x[i]+4*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(231, 189, 45) , (self.x[i]+5*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(230, 185, 42) , (self.x[i]+6*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(230, 183, 41) , (self.x[i]+7*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(229, 182, 42) , (self.x[i]+8*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(225, 178, 36) , (self.x[i]+9*5, self.y[i]+50/2,5,5))
                pygame.draw.rect(self.main_surface,(255, 245, 233) , (self.x[i]+0*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(234, 189, 44) , (self.x[i]+1*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(216, 188, 44) , (self.x[i]+2*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(231, 186, 43) , (self.x[i]+3*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(231, 184, 44) , (self.x[i]+4*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(231, 184, 44) , (self.x[i]+5*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(228, 181, 41) , (self.x[i]+6*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(227, 178, 37) , (self.x[i]+7*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(229, 178, 37) , (self.x[i]+8*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(234, 196, 53) , (self.x[i]+9*5, self.y[i]+60/2,5,5))
                pygame.draw.rect(self.main_surface,(247, 246, 244) , (self.x[i]+0*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(252, 244, 208) , (self.x[i]+1*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(226, 193, 52) , (self.x[i]+2*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(226, 179, 39) , (self.x[i]+3*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(227, 178, 37) , (self.x[i]+4*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(229, 178, 37) , (self.x[i]+5*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(227, 176, 35) , (self.x[i]+6*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(228, 174, 39) , (self.x[i]+7*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(225, 173, 38) , (self.x[i]+8*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(221, 172, 31) , (self.x[i]+9*5, self.y[i]+70/2,5,5))
                pygame.draw.rect(self.main_surface,(247, 247, 247) , (self.x[i]+0*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(250, 246, 243) , (self.x[i]+1*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(227, 204, 136) , (self.x[i]+2*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(223, 185, 58) , (self.x[i]+3*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(228, 175, 35) , (self.x[i]+4*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(227, 173, 38) , (self.x[i]+5*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(225, 171, 37) , (self.x[i]+6*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(226, 170, 33) , (self.x[i]+7*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(224, 163, 13) , (self.x[i]+8*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(245, 246, 241) , (self.x[i]+9*5, self.y[i]+80/2,5,5))
                pygame.draw.rect(self.main_surface,(247, 247, 247) , (self.x[i]+0*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(247, 247, 247) , (self.x[i]+1*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(247, 248, 243) , (self.x[i]+2*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(241, 242, 255) , (self.x[i]+3*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(228, 177, 49) , (self.x[i]+4*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(234, 173, 22) , (self.x[i]+5*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(227, 171, 16) , (self.x[i]+6*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(249, 244, 240) , (self.x[i]+7*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(250, 246, 245) , (self.x[i]+8*5, self.y[i]+90/2,5,5))
                pygame.draw.rect(self.main_surface,(247, 247, 247) , (self.x[i]+9*5, self.y[i]+90/2,5,5))
            else:
                pass
                

    def make_dummy(self):
        for i in range(TARGET_COUNT):
            pygame.draw.circle(self.main_surface, (255,0,0), (self.dummy_x[i]+25, self.dummy_y[i]), self.target_size)
            pygame.draw.circle(self.main_surface, (0,0,0), (self.dummy_x[i]+25, self.dummy_y[i]+8), self.target_size)
                

    def make_gun(self):
        pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-10, self.y3-10,20,20))
        pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-25, self.y3,50,20))

    def make_gun_out(self):
        pygame.draw.rect(self.main_surface, (200,200,200), (self.x3-10, self.y3-10,20,20))
        pygame.draw.rect(self.main_surface, (200,200,200), (self.x3-25, self.y3,50,20))

    def make_ball(self):
        for i in range(TARGET_COUNT):
            pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.bxt[i], self.byt[i]), 10)
    
    
    def target_move(self):
        #的移動
        for i in range(TARGET_COUNT):
            if(self.xstate[i]==0):
                self.x[i] += (1 +i)
                if(self.x[i]>400):
                    self.xstate[i]=1
            if(self.xstate[i]==1):
                self.x[i] -= (1 +i)
                if(self.x[i]<150):
                    self.xstate[i]=0    


            if(self.ystate[i]==0):
                self.y[i] += (1 +i)
                if(self.y[i]>300):
                    self.ystate[i]=1
            if(self.ystate[i]==1):
                self.y[i] -= (1 +i)
                if(self.y[i]<150):
                    self.ystate[i]=0 
                       
    def dummy_move(self):
        for i in range(TARGET_COUNT):

            if(self.xwall_state ==0):
                self.dummy_x[i] += (1+self.scenario_state)
            if(self.xwall_state==1):
                self.dummy_x[i] -= (1+self.scenario_state)

            
            self.dummy_y[i] += (10)
            if(self.dummy_y[i] >400):
                self.dummy_y[i]=100
        
    def wall_move(self):
        if(self.xwall_state ==0):
            self.x_wall += (1+self.scenario_state)
            if(self.x_wall>400):
                self.xwall_state=1
        if(self.xwall_state==1):
            self.x_wall -= (1+self.scenario_state)
            if(self.x_wall<150):
                self.xwall_state=0    



    def game_loop(self):
        pygame.display.set_caption("SHOOTING TEST")
        clock = pygame.time.Clock()
        stop_button = pygame.Rect(30, 30, 80, 50)  
        start_button = pygame.Rect(30, 130, 80, 50)  
        reset_button = pygame.Rect(30, 230, 80, 50)  
        font = pygame.font.SysFont(None, 25)
        text1 = font.render("STOP", True, (0,0,0))
        text2 = font.render("START", True, (0,0,0))
        text3 = font.render("SHOOT", True, (0,0,0))
        text4 = font.render("CURSOL:SHOOTER MOVE /  SPACE ball start   ", True, (0,0,0))
        texthit = font.render("  ", True, (0,0,0))
        start = time.time()
        
        going = True
        while going:
            if (self.stop==1):
                start = time.time()
                
            t = time.time() - start
            if(t>15):
                self.timeout=1

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                #大砲移動　左
                self.x3=self.x3-10        
            if pressed[pygame.K_RIGHT]:
                #大砲移動　右
                self.x3=self.x3+10        
    
    
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    going = False
    
    
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                       #大砲移動　左
                        self.x3=self.x3-10        
                    if event.key == K_RIGHT:
                       #大砲移動　右
                        self.x3=self.x3+10        
                    if event.key == K_SPACE:
                        #弾発射
                        self.bxt[self.xy0state]=self.x3
                        self.byt[self.xy0state]=400
                        self.xy0state += 1
                        if(self.xy0state==9):
                            self.xy0state=0    
                        self.stop=0
    
    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if stop_button.collidepoint(event.pos):
                        self.stop=1
                    if start_button.collidepoint(event.pos):
                        self.stop=0
                    if reset_button.collidepoint(event.pos):
                        #弾発射
                        self.bxt[self.xy0state]=self.x3
                        self.byt[self.xy0state]=400
                        self.xy0state += 1
                        if(self.xy0state==9):
                            self.xy0state=0    
                        self.stop=0
    
            #的衝突 
            self.hit_check()            
            #self.wall_col_check()    
            self.dummy_col_check()    
    
            self.main_surface.fill((220, 220, 220))
            pygame.draw.rect(self.main_surface, (255, 0, 0), stop_button)
            pygame.draw.rect(self.main_surface, (255, 255, 0), start_button)
            pygame.draw.rect(self.main_surface, (0, 0, 255), reset_button)
    
            self.by0 -=10
            self.by1 -=10
            self.by2 -=10
    
            if(self.stop==1):
                pass
            else: 
                for i in range(BALL_COUNT):
                    self.byt[i]-=10
    
                #的移動
                self.target_move()	    
    
                self.make_wall()     
                self.wall_move()     
                
                #弾             
                self.make_ball()
                
                #大砲             
                self.make_gun()
                self.make_dummy()
                self.dummy_move()
    
                        
                        
            #的 

            if(self.scenario_state==0):            
                texthit = font.render("STAGE1", True, (0,0,0))
                self.make_target()
                if (self.all_hit()==1):
                    self.scenario_state = 1
                    for i in range(BALL_COUNT):
                       self.hit[i]=0
                    
            if(self.scenario_state==1):            
                texthit = font.render("STAGE2", True, (0,0,0))
                self.make_target2()
                if (self.all_hit()==1):
                    self.scenario_state = 2
                    for i in range(BALL_COUNT):
                           self.hit[i]=0
            if(self.scenario_state==2):            
                texthit = font.render("GAME CLEAR !", True, (0,0,0))
                self.stop=1                            
                    
            
            
                
            self.main_surface.blit(text1, (40, 45))
            self.main_surface.blit(text2, (40,145))
            self.main_surface.blit(text3, (40,245))
            self.main_surface.blit(text4, (40,430))
            if(self.dummy_hit==1):        
                self.make_gun_out()
                texthit = font.render("BALL HIT TO GUN GAME OVER!", True, (255,0,0))
                self.stop=1                    
            if(self.wall_hit==1):        
                texthit = font.render("WALL HIT GAME OVER!", True, (255,0,0))
                self.stop=1                    
            
            if(self.timeout==1):        
                texthit = font.render("TIMEOUT!", True, (255,0,0))
                self.stop=1                    
            if(self.khit==1):        
                texthit = font.render("game over count="+str(self.hit_count), True, (0,0,0))
            else:
                pass
            self.main_surface.blit(texthit, (200,45))
            pygame.display.update()
            clock.tick(50)
            self.loop_count+=1
if __name__ == '__main__':
    app = top_app()
    app.main()