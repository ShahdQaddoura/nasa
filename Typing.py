import pygame

def Typing(text, dummy): # handles typing while the program is running
    keys_pressed = pygame.key.get_pressed()
    capslock = pygame.key.get_mods() & pygame.KMOD_CAPS
    if len(dummy) == 0:
        if keys_pressed[pygame.K_BACKSPACE]:
            text = text[:-1]
            dummy.append(1)
        if keys_pressed[pygame.K_SPACE]:
            text += ' '
            dummy.append(1)
        if keys_pressed[pygame.K_SLASH]:
            text += '/'
            dummy.append(1)
        if keys_pressed[pygame.K_ASTERISK]:
            text += '*'
            dummy.append(1)
        if not capslock and not keys_pressed[pygame.K_LSHIFT] and not keys_pressed[pygame.K_RSHIFT]:
            if keys_pressed[pygame.K_0] or keys_pressed[pygame.K_KP_0]:
                text += '0'
                dummy.append(1)
            if keys_pressed[pygame.K_1] or keys_pressed[pygame.K_KP_1]:
                text += '1'
                dummy.append(1)
            if keys_pressed[pygame.K_2] or keys_pressed[pygame.K_KP_2]:
                text += '2'
                dummy.append(1)
            if keys_pressed[pygame.K_3] or keys_pressed[pygame.K_KP_3]:
                text += '3'
                dummy.append(1)
            if keys_pressed[pygame.K_4] or keys_pressed[pygame.K_KP_4]:
                text += '4'
                dummy.append(1)
            if keys_pressed[pygame.K_5] or keys_pressed[pygame.K_KP_5]:
                text += '5'
                dummy.append(1)
            if keys_pressed[pygame.K_6] or keys_pressed[pygame.K_KP_6]:
                text += '6'
                dummy.append(1)
            if keys_pressed[pygame.K_7] or keys_pressed[pygame.K_KP_7]:
                text += '7'
                dummy.append(1)
            if keys_pressed[pygame.K_8] or keys_pressed[pygame.K_KP_8]:
                text += '8'
                dummy.append(1)
            if keys_pressed[pygame.K_9] or keys_pressed[pygame.K_KP_9]:
                text += '9'
                dummy.append(1)
            
        if keys_pressed[pygame.K_LSHIFT] or keys_pressed[pygame.K_RSHIFT] or capslock:
            if keys_pressed[pygame.K_q]:
                text += 'Q'
                dummy.append(1)
            if keys_pressed[pygame.K_w]:
                text += 'W'
                dummy.append(1)
            if keys_pressed[pygame.K_e]:
                text += 'E'
                dummy.append(1)
            if keys_pressed[pygame.K_r]:
                text += 'R'
                dummy.append(1)
            if keys_pressed[pygame.K_t]:
                text += 'T'
                dummy.append(1)
            if keys_pressed[pygame.K_y]:
                text += 'Y'
                dummy.append(1)
            if keys_pressed[pygame.K_u]:
                text += 'U'
                dummy.append(1)
            if keys_pressed[pygame.K_i]:
                text += 'I'
                dummy.append(1)
            if keys_pressed[pygame.K_o]:
                text += 'O'
                dummy.append(1)
            if keys_pressed[pygame.K_p]:
                text += 'P'
                dummy.append(1)
            if keys_pressed[pygame.K_a]:
                text += 'A'
                dummy.append(1)
            if keys_pressed[pygame.K_s]:
                text += 'S'
                dummy.append(1)
            if keys_pressed[pygame.K_d]:
                text += 'D'
                dummy.append(1)
            if keys_pressed[pygame.K_f]:
                text += 'F'
                dummy.append(1)
            if keys_pressed[pygame.K_g]:
                text += 'G'
                dummy.append(1)
            if keys_pressed[pygame.K_h]:
                text += 'H'
                dummy.append(1)
            if keys_pressed[pygame.K_j]:
                text += 'J'
                dummy.append(1)
            if keys_pressed[pygame.K_k]:
                text += 'K'
                dummy.append(1)
            if keys_pressed[pygame.K_l]:
                text += 'L'
                dummy.append(1)
            if keys_pressed[pygame.K_z]:
                text += 'Z'
                dummy.append(1)
            if keys_pressed[pygame.K_x]:
                text += 'X'
                dummy.append(1)
            if keys_pressed[pygame.K_c]:
                text += 'C'
                dummy.append(1)
            if keys_pressed[pygame.K_v]:
                text += 'V'
                dummy.append(1)
            if keys_pressed[pygame.K_b]:
                text += 'B'
                dummy.append(1)
            if keys_pressed[pygame.K_n]:
                text += 'N'
                dummy.append(1)
            if keys_pressed[pygame.K_m]:
                text += 'M'
                dummy.append(1)
            if keys_pressed[pygame.K_1]:
                text += '!'
                dummy.append(1)
            if keys_pressed[pygame.K_2]:
                text += '@'
                dummy.append(1)
            if keys_pressed[pygame.K_3]:
                text += '#'
                dummy.append(1)
            if keys_pressed[pygame.K_4]:
                text += '$'
                dummy.append(1)
            if keys_pressed[pygame.K_5]:
                text += '%'
                dummy.append(1)
            if keys_pressed[pygame.K_6]:
                text += '^'
                dummy.append(1)
            if keys_pressed[pygame.K_7]:
                text += '&'
                dummy.append(1)
            if keys_pressed[pygame.K_8]:
                text += '*'
                dummy.append(1)
            if keys_pressed[pygame.K_9]:
                text += '('
                dummy.append(1)
            if keys_pressed[pygame.K_0]:
                text += ')'
                dummy.append(1)
            if keys_pressed[pygame.K_MINUS]:
                text += '_'
                dummy.append(1)
            if keys_pressed[pygame.K_EQUALS]:
                text += '+'
                dummy.append(1)
        else:
            if keys_pressed[pygame.K_q]:
                text += 'q'
                dummy.append(1)
            if keys_pressed[pygame.K_w]:
                text += 'w'
                dummy.append(1)
            if keys_pressed[pygame.K_e]:
                text += 'e'
                dummy.append(1)
            if keys_pressed[pygame.K_r]:
                text += 'r'
                dummy.append(1)
            if keys_pressed[pygame.K_t]:
                text += 't'
                dummy.append(1)
            if keys_pressed[pygame.K_y]:
                text += 'y'
                dummy.append(1)
            if keys_pressed[pygame.K_u]:
                text += 'u'
                dummy.append(1)
            if keys_pressed[pygame.K_i]:
                text += 'i'
                dummy.append(1)
            if keys_pressed[pygame.K_o]:
                text += 'o'
                dummy.append(1)
            if keys_pressed[pygame.K_p]:
                text += 'p'
                dummy.append(1)
            if keys_pressed[pygame.K_a]:
                text += 'a'
                dummy.append(1)
            if keys_pressed[pygame.K_s]:
                text += 's'
                dummy.append(1)
            if keys_pressed[pygame.K_d]:
                text += 'd'
                dummy.append(1)
            if keys_pressed[pygame.K_f]:
                text += 'f'
                dummy.append(1)
            if keys_pressed[pygame.K_g]:
                text += 'g'
                dummy.append(1)
            if keys_pressed[pygame.K_h]:
                text += 'h'
                dummy.append(1)
            if keys_pressed[pygame.K_j]:
                text += 'j'
                dummy.append(1)
            if keys_pressed[pygame.K_k]:
                text += 'k'
                dummy.append(1)
            if keys_pressed[pygame.K_l]:
                text += 'l'
                dummy.append(1)
            if keys_pressed[pygame.K_z]:
                text += 'z'
                dummy.append(1)
            if keys_pressed[pygame.K_x]:
                text += 'x'
                dummy.append(1)
            if keys_pressed[pygame.K_c]:
                text += 'c'
                dummy.append(1)
            if keys_pressed[pygame.K_v]:
                text += 'v'
                dummy.append(1)
            if keys_pressed[pygame.K_b]:
                text += 'b'
                dummy.append(1)
            if keys_pressed[pygame.K_n]:
                text += 'n'
                dummy.append(1)
            if keys_pressed[pygame.K_m]:
                text += 'm'
                dummy.append(1)
            if keys_pressed[pygame.K_MINUS]:
                text += '-'
                dummy.append(1)
            if keys_pressed[pygame.K_EQUALS]:
                text += '='
                dummy.append(1)
            if keys_pressed[pygame.K_COMMA]:
                text += ','
                dummy.append(1)
            if keys_pressed[pygame.K_PERIOD]:
                text += '.'

    return text