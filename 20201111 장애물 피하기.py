#장애물 피하기
import pygame as p

p.init() # 라이브러리 초기화
size = (600,300) 
white = (255,255,255) # (R,G,B)
green = (0,255,0)
sc = p.display.set_mode(size) #해상도 설정
p.display.set_caption("image") #창이름 변경 
playing = True
#공룡 이미지
gong = p.image.load("gong.png")
cc = p.image.load("cc.png") 
cc_rect = cc.get_rect(left = 549, top = 223)
g_rect = gong.get_rect(left =15 ,top =180)
g_y = 0 #점프 관련 변수 
jumping = False
#배경
bg =  p.image.load("bg111.png")
bg_rect = bg.get_rect(left =0 ,top =0)
bg1 =p.image.load("bg111.png")
bg1_rect = bg.get_rect(left =600 ,top =0)
#프레임 설정
clock = p.time.Clock()
sp = 3
font = p.font.SysFont("malgungothic",25)
score = 0
font2 = p.font.SysFont("malgungothic",80)
while playing:
    clock.tick(60)
    for event in p.event.get(): #우리가 누르는것 감지
        if event.type == p.QUIT: #게임창 x버튼 누르면
            playing = True # 게속반복 종
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_SPACE:
                if jumping:
                    g_y = -15
                    jumping = False  
                
                
                

    sc.fill(white) #배경화면 색깔
    #배경 업로드 
    sc.blit(bg,bg_rect)
    sc.blit(bg1,bg1_rect)

    bg_rect.left -= 3
    bg1_rect.left -= 3
    cc_rect.left -= sp

    #배경 움직이기
    if bg_rect.left <= -600:
        bg_rect.left = 600
    if bg1_rect.left <= -600:
        bg1_rect.left = 600
    sc.blit(gong,g_rect)
    if cc_rect.left <= 0:
        cc_rect.left = 549

    if score%100 <= 0:
        sp += 0.3 
        
    #공룡 중력 만들기
    g_rect.top += g_y # g_rect.top = g_rect.top + g_y
    g_y += 1
    if g_rect.top >= 230:
        g_rect.top = 230
        jumping = True
    sc.blit(cc,cc_rect)

    text = font.render("점수 {}".format(score),True,(255,25,155))
    sc.blit(text,(300,0))      
    score += 1

    text2 = font2.render("게임오버".format(score),True,(255,0,0))
                      
#충돌
    if g_rect.colliderect(cc_rect):
        sc.blit(text2,(250,100))
        playing = False

        
        


                    
    p.display.flip() #화면 업데이트 
        
