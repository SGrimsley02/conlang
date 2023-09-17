import pygame
import sys

def inputGUI(inputType): ##Returns typed value when enter is pressed
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([600, 500])

    ##Font
    base_font = pygame.font.SysFont('Conscript', 32)
    user_text = ''

    input_rect = pygame.Rect(200, 200, 140, 32)

    pygame.display.set_caption(inputType)

    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive

    active = False
    running = True
    while running:
        for event in pygame.event.get():
            all_keys = pygame.key.get_pressed()
            shift_and_alt_key = (all_keys[pygame.K_LSHIFT] or all_keys[pygame.K_RSHIFT]) and (all_keys[pygame.K_RALT] or all_keys[pygame.K_LALT])
            shift_key = (all_keys[pygame.K_LSHIFT] or all_keys[pygame.K_RSHIFT])
            alt_key = (all_keys[pygame.K_RALT] or all_keys[pygame.K_LALT])
            ##Quit, can also press escape, or ends when returned
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            ##If click the box, light up
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            ##Typing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: ##Backspace
                    user_text = user_text[:-1]
                elif event.key == pygame.K_ESCAPE: ##Quit, should actually work
                    pygame.quit()
                    sys.exit()
                elif all_keys[pygame.K_a] and shift_and_alt_key: ##Doing each individually, should work better on different OS
                    user_text += '\u01D1'
                elif all_keys[pygame.K_b] and shift_and_alt_key: ##Currently goes to \u01E7, haven't done numbers
                    user_text += '\u01D2'
                elif all_keys[pygame.K_c] and shift_and_alt_key:
                    user_text += '\u01D3'
                elif all_keys[pygame.K_d] and shift_and_alt_key:
                    user_text += '\u01D4'
                elif all_keys[pygame.K_e] and shift_and_alt_key:
                    user_text += '\u01D5'
                elif all_keys[pygame.K_f] and shift_and_alt_key:
                    user_text += '\u01D6'
                elif all_keys[pygame.K_g] and shift_and_alt_key:
                    user_text += '\u01D7'
                elif all_keys[pygame.K_h] and shift_and_alt_key:
                    user_text += '\u01D8'
                elif all_keys[pygame.K_i] and shift_and_alt_key:
                    user_text += '\u01D9'
                elif all_keys[pygame.K_j] and shift_and_alt_key:
                    user_text += '\u01DA'
                elif all_keys[pygame.K_k] and shift_and_alt_key:
                    user_text += '\u01DB'
                elif all_keys[pygame.K_l] and shift_and_alt_key:
                    user_text += '\u01DC'
                elif all_keys[pygame.K_m] and shift_and_alt_key:
                    user_text += '\u01DD'
                elif all_keys[pygame.K_n] and shift_and_alt_key:
                    user_text += '\u01DE'
                elif all_keys[pygame.K_o] and shift_and_alt_key:
                    user_text += '\u01DF'
                elif all_keys[pygame.K_p] and shift_and_alt_key:
                    user_text += '\u01E0'
                elif all_keys[pygame.K_q] and shift_and_alt_key:
                    user_text += '\u01E1'
                elif all_keys[pygame.K_r] and shift_and_alt_key:
                    user_text += '\u01E2'
                elif all_keys[pygame.K_s] and shift_and_alt_key:
                    user_text += '\u01E3'
                elif all_keys[pygame.K_t] and shift_and_alt_key:
                    user_text += '\u01E4'
                elif all_keys[pygame.K_u] and shift_and_alt_key:
                    user_text += '\u01E5'
                elif all_keys[pygame.K_v] and shift_and_alt_key:
                    user_text += '\u01E6'
                elif all_keys[pygame.K_w] and shift_and_alt_key:
                    user_text += '\u01E7'
                elif all_keys[pygame.K_x] and shift_and_alt_key:
                    user_text += '\u01E8'
                elif all_keys[pygame.K_y] and shift_and_alt_key:
                    user_text += '\u01E9'
                elif all_keys[pygame.K_z] and shift_and_alt_key:
                    user_text += '\u01EA'
                elif all_keys[pygame.K_SEMICOLON] and shift_and_alt_key:
                    user_text += '\u01EB'
                elif all_keys[pygame.K_a] and shift_key:
                    user_text += '\u019B'
                elif all_keys[pygame.K_b] and shift_key:
                    user_text += '\u019C'
                elif all_keys[pygame.K_c] and shift_key:
                    user_text += '\u019D'
                elif all_keys[pygame.K_d] and shift_key:
                    user_text += '\u019E'
                elif all_keys[pygame.K_e] and shift_key:
                    user_text += '\u019F'
                elif all_keys[pygame.K_f] and shift_key:
                    user_text += '\u01A0'
                elif all_keys[pygame.K_g] and shift_key:
                    user_text += '\u01A1'
                elif all_keys[pygame.K_h] and shift_key:
                    user_text += '\u01A2'
                elif all_keys[pygame.K_i] and shift_key:
                    user_text += '\u01A3'
                elif all_keys[pygame.K_j] and shift_key:
                    user_text += '\u01A4'
                elif all_keys[pygame.K_k] and shift_key:
                    user_text += '\u01A5'
                elif all_keys[pygame.K_l] and shift_key:
                    user_text += '\u01A6'
                elif all_keys[pygame.K_m] and shift_key:
                    user_text += '\u01A7'
                elif all_keys[pygame.K_n] and shift_key:
                    user_text += '\u01A8'
                elif all_keys[pygame.K_o] and shift_key:
                    user_text += '\u01A9'
                elif all_keys[pygame.K_p] and shift_key:
                    user_text += '\u01AA'
                elif all_keys[pygame.K_q] and shift_key:
                    user_text += '\u01AB'
                elif all_keys[pygame.K_r] and shift_key:
                    user_text += '\u01AC'
                elif all_keys[pygame.K_s] and shift_key:
                    user_text += '\u01AD'
                elif all_keys[pygame.K_t] and shift_key:
                    user_text += '\u01AE'
                elif all_keys[pygame.K_u] and shift_key:
                    user_text += '\u01AF'
                elif all_keys[pygame.K_v] and shift_key:
                    user_text += '\u01B0'
                elif all_keys[pygame.K_w] and shift_key:
                    user_text += '\u01B1'
                elif all_keys[pygame.K_x] and shift_key:
                    user_text += '\u01B2'
                elif all_keys[pygame.K_y] and shift_key:
                    user_text += '\u01B3'
                elif all_keys[pygame.K_z] and shift_key:
                    user_text += '\u01B4'
                elif all_keys[pygame.K_SEMICOLON] and shift_key:
                    user_text += '\u01B5'
                elif all_keys[pygame.K_a] and alt_key:
                    user_text += '\u01B6'
                elif all_keys[pygame.K_b] and alt_key:
                    user_text += '\u01B7'
                elif all_keys[pygame.K_c] and alt_key:
                    user_text += '\u01B8'
                elif all_keys[pygame.K_d] and alt_key:
                    user_text += '\u01B9'
                elif all_keys[pygame.K_e] and alt_key:
                    user_text += '\u01BA'
                elif all_keys[pygame.K_f] and alt_key:
                    user_text += '\u01BB'
                elif all_keys[pygame.K_g] and alt_key:
                    user_text += '\u01BC'
                elif all_keys[pygame.K_h] and alt_key:
                    user_text += '\u01BD'
                elif all_keys[pygame.K_i] and alt_key:
                    user_text += '\u01BE'
                elif all_keys[pygame.K_j] and alt_key:
                    user_text += '\u01BF'
                elif all_keys[pygame.K_k] and alt_key:
                    user_text += '\u01C0'
                elif all_keys[pygame.K_l] and alt_key:
                    user_text += '\u01C1'
                elif all_keys[pygame.K_m] and alt_key:
                    user_text += '\u01C2'
                elif all_keys[pygame.K_n] and alt_key:
                    user_text += '\u01C3'
                elif all_keys[pygame.K_o] and alt_key:
                    user_text += '\u01C4'
                elif all_keys[pygame.K_p] and alt_key:
                    user_text += '\u01C5'
                elif all_keys[pygame.K_q] and alt_key:
                    user_text += '\u01C6'
                elif all_keys[pygame.K_r] and alt_key:
                    user_text += '\u01C7'
                elif all_keys[pygame.K_s] and alt_key:
                    user_text += '\u01C8'
                elif all_keys[pygame.K_t] and alt_key:
                    user_text += '\u01C9'
                elif all_keys[pygame.K_u] and alt_key:
                    user_text += '\u01CA'
                elif all_keys[pygame.K_v] and alt_key:
                    user_text += '\u01CB'
                elif all_keys[pygame.K_w] and alt_key:
                    user_text += '\u01CC'
                elif all_keys[pygame.K_x] and alt_key:
                    user_text += '\u01CD'
                elif all_keys[pygame.K_y] and alt_key:
                    user_text += '\u01CE'
                elif all_keys[pygame.K_z] and alt_key:
                    user_text += '\u01CF'
                elif all_keys[pygame.K_SEMICOLON] and alt_key:
                    user_text += '\u01D0'
                elif all_keys[pygame.K_a]:
                    user_text += '\u0180'
                elif all_keys[pygame.K_b]:
                    user_text += '\u0181'
                elif all_keys[pygame.K_c]:
                    user_text += '\u0182'
                elif all_keys[pygame.K_d]:
                    user_text += '\u0183'
                elif all_keys[pygame.K_e]:
                    user_text += '\u0184'
                elif all_keys[pygame.K_f]:
                    user_text += '\u0185'
                elif all_keys[pygame.K_g]:
                    user_text += '\u0186'
                elif all_keys[pygame.K_h]:
                    user_text += '\u0187'
                elif all_keys[pygame.K_i]:
                    user_text += '\u0188'
                elif all_keys[pygame.K_j]:
                    user_text += '\u0189'
                elif all_keys[pygame.K_k]:
                    user_text += '\u018A'
                elif all_keys[pygame.K_l]:
                    user_text += '\u018B'
                elif all_keys[pygame.K_m]:
                    user_text += '\u018C'
                elif all_keys[pygame.K_n]:
                    user_text += '\u018D'
                elif all_keys[pygame.K_o]:
                    user_text += '\u018E'
                elif all_keys[pygame.K_p]:
                    user_text += '\u018F'
                elif all_keys[pygame.K_q]:
                    user_text += '\u0190'
                elif all_keys[pygame.K_r]:
                    user_text += '\u0191'
                elif all_keys[pygame.K_s]:
                    user_text += '\u0192'
                elif all_keys[pygame.K_t]:
                    user_text += '\u0193'
                elif all_keys[pygame.K_u]:
                    user_text += '\u0194'
                elif all_keys[pygame.K_v]:
                    user_text += '\u0195'
                elif all_keys[pygame.K_w]:
                    user_text += '\u0196'
                elif all_keys[pygame.K_x]:
                    user_text += '\u0197'
                elif all_keys[pygame.K_y]:
                    user_text += '\u0198'
                elif all_keys[pygame.K_z]:
                    user_text += '\u0199'
                elif all_keys[pygame.K_SEMICOLON]:
                    user_text += '\u019A'
                elif all_keys[pygame.K_BACKQUOTE]: ##0
                    user_text += '\U000F0105'
                elif all_keys[pygame.K_1]: ##1
                    user_text += '\U000F0106'
                elif all_keys[pygame.K_2]: ##2
                    user_text += '\U000F0107'
                elif all_keys[pygame.K_3]: ##3
                    user_text += '\U000F0108'
                elif all_keys[pygame.K_4]: ##4
                    user_text += '\U000F0109'
                elif all_keys[pygame.K_5]: ##5
                    user_text += '\U000F0110'
                elif all_keys[pygame.K_6]: ##6
                    user_text += '\U000F0111'
                elif all_keys[pygame.K_7]: ##7
                    user_text += '\U000F0112'
                elif all_keys[pygame.K_8]: ##8
                    user_text += '\U000F0113'
                elif all_keys[pygame.K_9]: ##9
                    user_text += '\U000F0114'
                elif all_keys[pygame.K_0]: ##Number A
                    user_text += '\U000F0115'
                elif all_keys[pygame.K_MINUS]: ##Number B
                    user_text += '\U000F0116'
                ##### For all additional characters, start adding elif statements here
                elif all_keys[pygame.K_RETURN]:
                    return user_text
                
        
        ##Background
        screen.fill((255, 255, 255))

        ##Box color
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        ##Text
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        ##Box width
        input_rect.w = max(100, text_surface.get_width()+10)
        
        ##Updating display
        pygame.display.flip()
        
        ##FPS
        clock.tick(60)

def displayGUI(entry): ##Displays dictionary entries in native script
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1000, 1000])
    ##Font
    base_font = pygame.font.SysFont('Conscript', 32)
    text = entry
    ##Display
    displayBox = pygame.Rect(100, 100, 800, 800)
    color = pygame.Color('pink')
    pygame.display.set_caption("Display")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        screen.fill('purple')
        pygame.draw.rect(screen, color, displayBox)
        text_surface = base_font.render(text, True, 'white')
        screen.blit(text_surface, [displayBox.x + 10, displayBox.y + 10])

        pygame.display.flip()
        clock.tick(60)
##Pass in a Word object

