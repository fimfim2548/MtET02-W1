import pygame
import sys
import random
import math

# เริ่มต้นระบบ Pygame
pygame.init()

# ตั้งค่าหน้าจอเกม
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("เกมปาโป่งสุดสนุก (Balloon Popping Game)")
clock = pygame.time.Clock()

# กำหนดสี (RGB)
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# รายชื่อสีของลูกโป่งที่จะสุ่ม
BALLOON_COLORS = [
    (255, 51, 51),   # แดง
    (51, 153, 255),  # น้ำเงิน
    (255, 204, 0),   # เหลือง
    (51, 204, 51),   # เขียว
    (255, 102, 255)  # ชมพู
]

# ฟังก์ชันสร้างลูกโป่งใหม่
def create_balloon():
    return {
        "x": random.randint(50, SCREEN_WIDTH - 50),
        "y": random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 200),
        "radius": random.randint(25, 35),
        "speed": random.uniform(2, 4.5),
        "color": random.choice(BALLOON_COLORS)
    }

# สร้างชุดลูกโป่งเริ่มต้น 6 ลูก
balloons = [create_balloon() for _ in range(6)]

score = 0
missed = 0
font = pygame.font.SysFont("Arial", 26)
game_over = False

# Game Loop
running = True
while running:
    # พื้นหลังสีฟ้าสดใส
    screen.fill(SKY_BLUE)

    # ตรวจจับเหตุการณ์ (Event Handling)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # เมื่อผู้เล่นคลิกเมาส์ซ้าย
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game_over:
                # ถ้าเกมจบแล้วคลิกเมาส์ จะเป็นการเริ่มเกมใหม่
                balloons = [create_balloon() for _ in range(6)]
                score = 0
                missed = 0
                game_over = False
            else:
                mouse_x, mouse_x_pos = pygame.mouse.get_pos()
                # ตรวจสอบว่าคลิกโดนลูกโป่งลูกไหนไหม
                for b in balloons:
                    # คำนวณระยะห่างระหว่างจุดคลิกกับศูนย์กลางลูกโป่ง (สูตรระยะทาง Pythagoras)
                    distance = math.sqrt((mouse_x - b["x"])**2 + (mouse_x_pos - b["y"])**2)
                    if distance < b["radius"]:
                        score += 1
                        # รีเซ็ตลูกโป่งที่โดนจิ้มให้กลับไปเริ่มต้นใหม่ด้านล่าง
                        balloons.remove(b)
                        balloons.append(create_balloon())
                        break

    if not game_over:
        # อัปเดตและวาดลูกโป่ง
        for b in balloons:
            b["y"] -= b["speed"]  # ให้ลูกโป่งลอยขึ้นด้านบน

            # ถ้าลอยทะลุขอบบนหน้าจอไป (ผู้เล่นจิ้มไม่ทัน)
            if b["y"] < -b["radius"]:
                missed += 1
                balloons.remove(b)
                balloons.append(create_balloon())

            # วาดตัวลูกโป่ง (วงกลม)
            pygame.draw.circle(screen, b["color"], (int(b["x"]), int(b["y"])), b["radius"])
            # วาดเชือกลูกโป่ง (เส้นตรงลากลงมา)
            pygame.draw.line(screen, BLACK, (int(b["x"]), int(b["y"] + b["radius"])), (int(b["x"]), int(b["y"] + b["radius"] + 20)), 1)

        # เงื่อนไขสิ้นสุดเกม: ปล่อยหลุดมือเกิน 10 ลูก
        if missed >= 10:
            game_over = True

        # แสดงคะแนนและจำนวนที่พลาด
        score_text = font.render(f"Score: {score}", True, BLACK)
        missed_text = font.render(f"Missed: {missed}/10", True, (200, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(missed_text, (10, 40))

    else:
        # หน้าจอตอน Game Over
        go_font = pygame.font.SysFont("Arial", 40, bold=True)
        hint_font = pygame.font.SysFont("Arial", 20)
        
        go_text = go_font.render("GAME OVER", True, (255, 0, 0))
        final_score = go_font.render(f"Total Score: {score}", True, BLACK)
        restart_text = hint_font.render("Click anywhere to Restart", True, BLACK)
        
        screen.blit(go_text, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 - 60))
        screen.blit(final_score, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 95, SCREEN_HEIGHT // 2 + 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()