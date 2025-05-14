
import pygame

class Snake:

    def __init__(self, start_pos, r, g, b):
    # Initialize snake's body segments individually
        self.head = start_pos
        self.seg1 = None
        self.seg2 = None
        self.seg3 = None
        self.seg4 = None
        self.seg5 = None
        self.seg6 = None
        self.seg7 = None
        self.seg8 = None
        self.seg9 = None
        self.seg10 = None
        self.seg11 = None
        self.seg12 = None
        self.seg13 = None
        self.seg14 = None
        self.seg15 = None
        self.seg16 = None
        self.seg17 = None
        self.seg18 = None
        self.seg19 = None
        self.seg20 = None
        self.seg21 = None
        self.seg22 = None
        self.seg23 = None
        self.seg24 = None
        self.seg25 = None
        self.seg26 = None
        self.seg27 = None
        self.seg28 = None
        self.seg29 = None
        self.seg30 = None
        self.seg31 = None
        self.seg32 = None
        self.seg33 = None
        self.seg34 = None
        self.seg35 = None
        self.seg36 = None
        self.seg37 = None
        self.seg38 = None
        self.seg39 = None
        self.seg40 = None
        self.seg41 = None
        self.seg42 = None
        self.seg43 = None
        self.seg44 = None
        self.seg45 = None
        self.seg46 = None
        self.seg47 = None
        self.seg48 = None
        self.seg49 = None
        self.seg50 = None
        self.seg51 = None
        self.seg52 = None
        self.seg53 = None
        self.seg54 = None
        self.seg55 = None
        self.seg56 = None
        self.seg57 = None
        self.seg58 = None
        self.seg59 = None
        self.seg60 = None
        self.seg61 = None
        self.seg62 = None
        self.seg63 = None
        self.seg64 = None
        self.seg65 = None
        self.seg66 = None
        self.seg67 = None
        self.seg68 = None
        self.seg69 = None
        self.seg70 = None
        self.seg71 = None
        self.seg72 = None
        self.seg73 = None
        self.seg74 = None
        self.seg75 = None
        self.seg76 = None
        self.seg77 = None
        self.seg78 = None
        self.seg79 = None
        self.seg80 = None

        # Other attributes
        self.color = (r, g, b)
        self.grow = False
        self.length = 1  #Only head at the start


    def move(self, direction):
        # Compute new head position
        x, y = self.head
        if direction == "UP":
            new_head = (x, y - 1)
        elif direction == "DOWN":
            new_head = (x, y + 1)
        elif direction == "LEFT":
            new_head = (x - 1, y)
        elif direction == "RIGHT":
            new_head = (x + 1, y)
        else:
            return

        # If not growing, drop the last segment by not shifting a new one into it
        if not self.grow:
            #make sure size doesn't grow when moving
            #Reverse order to not lose references
            if self.seg80:
                self.seg80 = self.seg79
            if self.seg79:
                self.seg79 = self.seg78
            if self.seg78:
                self.seg78 = self.seg77
            if self.seg77:
                self.seg77 = self.seg76
            if self.seg76:
                self.seg76 = self.seg75
            if self.seg75:
                self.seg75 = self.seg74
            if self.seg74:
                self.seg74 = self.seg73
            if self.seg73:
                self.seg73 = self.seg72
            if self.seg72:
                self.seg72 = self.seg71
            if self.seg71:
                self.seg71 = self.seg70
            if self.seg70:
                self.seg70 = self.seg69
            if self.seg69:
                self.seg69 = self.seg68
            if self.seg68:
                self.seg68 = self.seg67
            if self.seg67:
                self.seg67 = self.seg66
            if self.seg66:
                self.seg66 = self.seg65
            if self.seg65:
                self.seg65 = self.seg64
            if self.seg64:
                self.seg64 = self.seg63
            if self.seg63:
                self.seg63 = self.seg62
            if self.seg62:
                self.seg62 = self.seg61
            if self.seg61:
                self.seg61 = self.seg60
            if self.seg60:
                self.seg60 = self.seg59
            if self.seg59:
                self.seg59 = self.seg58
            if self.seg58:
                self.seg58 = self.seg57
            if self.seg57:
                self.seg57 = self.seg56
            if self.seg56:
                self.seg56 = self.seg55
            if self.seg55:
                self.seg55 = self.seg54
            if self.seg54:
                self.seg54 = self.seg53
            if self.seg53:
                self.seg53 = self.seg52
            if self.seg52:
                self.seg52 = self.seg51
            if self.seg51:
                self.seg51 = self.seg50
            if self.seg50:
                self.seg50 = self.seg49
            if self.seg49:
                self.seg49 = self.seg48
            if self.seg48:
                self.seg48 = self.seg47
            if self.seg47:
                self.seg47 = self.seg46
            if self.seg46:
                self.seg46 = self.seg45
            if self.seg45:
                self.seg45 = self.seg44
            if self.seg44:
                self.seg44 = self.seg43
            if self.seg43:
                self.seg43 = self.seg42
            if self.seg42:
                self.seg42 = self.seg41
            if self.seg41:
                self.seg41 = self.seg40
            if self.seg40:
                self.seg40 = self.seg39
            if self.seg39:
                self.seg39 = self.seg38
            if self.seg38:
                self.seg38 = self.seg37
            if self.seg37:
                self.seg37 = self.seg36
            if self.seg36:
                self.seg36 = self.seg35
            if self.seg35:
                self.seg35 = self.seg34
            if self.seg34:
                self.seg34 = self.seg33
            if self.seg33:
                self.seg33 = self.seg32
            if self.seg32:
                self.seg32 = self.seg31
            if self.seg31:
                self.seg31 = self.seg30
            if self.seg30:
                self.seg30 = self.seg29
            if self.seg29:
                self.seg29 = self.seg28
            if self.seg28:
                self.seg28 = self.seg27
            if self.seg27:
                self.seg27 = self.seg26
            if self.seg26:
                self.seg26 = self.seg25
            if self.seg25:
                self.seg25 = self.seg24
            if self.seg24:
                self.seg24 = self.seg23
            if self.seg23:
                self.seg23 = self.seg22
            if self.seg22:
                self.seg22 = self.seg21
            if self.seg21:
                self.seg21 = self.seg20
            if self.seg20:
                self.seg20 = self.seg19
            if self.seg19:
                self.seg19 = self.seg18
            if self.seg18:
                self.seg18 = self.seg17
            if self.seg17:
                self.seg17 = self.seg16
            if self.seg16:
                self.seg16 = self.seg15
            if self.seg15:
                self.seg15 = self.seg14
            if self.seg14:
                self.seg14 = self.seg13
            if self.seg13:
                self.seg13 = self.seg12
            if self.seg12:
                self.seg12 = self.seg11
            if self.seg11:
                self.seg11 = self.seg10
            if self.seg10:
                self.seg10 = self.seg9
            if self.seg9:
                self.seg9 = self.seg8
            if self.seg8:
                self.seg8 = self.seg7
            if self.seg7:
                self.seg7 = self.seg6
            if self.seg6:
                self.seg6 = self.seg5
            if self.seg5:
                self.seg5 = self.seg4
            if self.seg4:
                self.seg4 = self.seg3
            if self.seg3:
                self.seg3 = self.seg2
            if self.seg2:
                self.seg2 = self.seg1
            if self.seg1:
                self.seg1 = self.head
        else:
            # Growing: shift everything including the last one
            self.seg80 = self.seg79
            self.seg79 = self.seg78
            self.seg78 = self.seg77
            self.seg77 = self.seg76
            self.seg76 = self.seg75
            self.seg75 = self.seg74
            self.seg74 = self.seg73
            self.seg73 = self.seg72
            self.seg72 = self.seg71
            self.seg71 = self.seg70
            self.seg70 = self.seg69
            self.seg69 = self.seg68
            self.seg68 = self.seg67
            self.seg67 = self.seg66
            self.seg66 = self.seg65
            self.seg65 = self.seg64
            self.seg64 = self.seg63
            self.seg63 = self.seg62
            self.seg62 = self.seg61
            self.seg61 = self.seg60
            self.seg60 = self.seg59
            self.seg59 = self.seg58
            self.seg58 = self.seg57
            self.seg57 = self.seg56
            self.seg56 = self.seg55
            self.seg55 = self.seg54
            self.seg54 = self.seg53
            self.seg53 = self.seg52
            self.seg52 = self.seg51
            self.seg51 = self.seg50
            self.seg50 = self.seg49
            self.seg49 = self.seg48
            self.seg48 = self.seg47
            self.seg47 = self.seg46
            self.seg46 = self.seg45
            self.seg45 = self.seg44
            self.seg44 = self.seg43
            self.seg43 = self.seg42
            self.seg42 = self.seg41
            self.seg41 = self.seg40
            self.seg40 = self.seg39
            self.seg39 = self.seg38
            self.seg38 = self.seg37
            self.seg37 = self.seg36
            self.seg36 = self.seg35
            self.seg35 = self.seg34
            self.seg34 = self.seg33
            self.seg33 = self.seg32
            self.seg32 = self.seg31
            self.seg31 = self.seg30
            self.seg30 = self.seg29
            self.seg29 = self.seg28
            self.seg28 = self.seg27
            self.seg27 = self.seg26
            self.seg26 = self.seg25
            self.seg25 = self.seg24
            self.seg24 = self.seg23
            self.seg23 = self.seg22
            self.seg22 = self.seg21
            self.seg21 = self.seg20
            self.seg20 = self.seg19
            self.seg19 = self.seg18
            self.seg18 = self.seg17
            self.seg17 = self.seg16
            self.seg16 = self.seg15
            self.seg15 = self.seg14
            self.seg14 = self.seg13
            self.seg13 = self.seg12
            self.seg12 = self.seg11
            self.seg11 = self.seg10
            self.seg10 = self.seg9
            self.seg9 = self.seg8
            self.seg8 = self.seg7
            self.seg7 = self.seg6
            self.seg6 = self.seg5
            self.seg5 = self.seg4
            self.seg4 = self.seg3
            self.seg3 = self.seg2
            self.seg2 = self.seg1
            self.seg1 = self.head
            self.grow = False  # Reset grow flag
        # Place new head
        self.head = new_head

    def draw(self, screen):
        
        # Draw the head segments with full color
        rect = pygame.Rect(self.head[0] * 25 + 189, self.head[1] * 25 + 189, 23, 23)
        pygame.draw.rect(screen, self.color, rect)
        
        # Draw the body segments with a darker shade
        if self.seg1:
            rect = pygame.Rect(self.seg1[0] * 25 + 189, self.seg1[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg2:
            rect = pygame.Rect(self.seg2[0] * 25 + 189, self.seg2[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg3:
            rect = pygame.Rect(self.seg3[0] * 25 + 189, self.seg3[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg4:
            rect = pygame.Rect(self.seg4[0] * 25 + 189, self.seg4[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg5:
            rect = pygame.Rect(self.seg5[0] * 25 + 189, self.seg5[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg6:
            rect = pygame.Rect(self.seg6[0] * 25 + 189, self.seg6[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg7:
            rect = pygame.Rect(self.seg7[0] * 25 + 189, self.seg7[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg8:
            rect = pygame.Rect(self.seg8[0] * 25 + 189, self.seg8[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg9:
            rect = pygame.Rect(self.seg9[0] * 25 + 189, self.seg9[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg10:
            rect = pygame.Rect(self.seg10[0] * 25 + 189, self.seg10[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg11:
            rect = pygame.Rect(self.seg11[0] * 25 + 189, self.seg11[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg12:
            rect = pygame.Rect(self.seg12[0] * 25 + 189, self.seg12[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg13:
            rect = pygame.Rect(self.seg13[0] * 25 + 189, self.seg13[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg14:
            rect = pygame.Rect(self.seg14[0] * 25 + 189, self.seg14[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg15:
            rect = pygame.Rect(self.seg15[0] * 25 + 189, self.seg15[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg16:
            rect = pygame.Rect(self.seg16[0] * 25 + 189, self.seg16[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)
        
        if self.seg17:
            rect = pygame.Rect(self.seg17[0] * 25 + 189, self.seg17[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg18:
            rect = pygame.Rect(self.seg18[0] * 25 + 189, self.seg18[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg19:
            rect = pygame.Rect(self.seg19[0] * 25 + 189, self.seg19[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg20:
            rect = pygame.Rect(self.seg20[0] * 25 + 189, self.seg20[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg21:
            rect = pygame.Rect(self.seg21[0] * 25 + 189, self.seg21[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg22:
            rect = pygame.Rect(self.seg22[0] * 25 + 189, self.seg22[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg23:
            rect = pygame.Rect(self.seg23[0] * 25 + 189, self.seg23[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg24:
            rect = pygame.Rect(self.seg24[0] * 25 + 189, self.seg24[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg25:
            rect = pygame.Rect(self.seg25[0] * 25 + 189, self.seg25[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg26:
            rect = pygame.Rect(self.seg26[0] * 25 + 189, self.seg26[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg27:
            rect = pygame.Rect(self.seg27[0] * 25 + 189, self.seg27[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg28:
            rect = pygame.Rect(self.seg28[0] * 25 + 189, self.seg28[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg29:
            rect = pygame.Rect(self.seg29[0] * 25 + 189, self.seg29[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg30:
            rect = pygame.Rect(self.seg30[0] * 25 + 189, self.seg30[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg31:
            rect = pygame.Rect(self.seg31[0] * 25 + 189, self.seg31[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg32:
            rect = pygame.Rect(self.seg32[0] * 25 + 189, self.seg32[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg33:
            rect = pygame.Rect(self.seg33[0] * 25 + 189, self.seg33[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg34:
            rect = pygame.Rect(self.seg34[0] * 25 + 189, self.seg34[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg35:
            rect = pygame.Rect(self.seg35[0] * 25 + 189, self.seg35[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg36:
            rect = pygame.Rect(self.seg36[0] * 25 + 189, self.seg36[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg37:
            rect = pygame.Rect(self.seg37[0] * 25 + 189, self.seg37[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg38:
            rect = pygame.Rect(self.seg38[0] * 25 + 189, self.seg38[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg39:
            rect = pygame.Rect(self.seg39[0] * 25 + 189, self.seg39[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg40:
            rect = pygame.Rect(self.seg40[0] * 25 + 189, self.seg40[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg41:
            rect = pygame.Rect(self.seg41[0] * 25 + 189, self.seg41[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg42:
            rect = pygame.Rect(self.seg42[0] * 25 + 189, self.seg42[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg43:
            rect = pygame.Rect(self.seg43[0] * 25 + 189, self.seg43[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg44:
            rect = pygame.Rect(self.seg44[0] * 25 + 189, self.seg44[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg45:
            rect = pygame.Rect(self.seg45[0] * 25 + 189, self.seg45[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg46:
            rect = pygame.Rect(self.seg46[0] * 25 + 189, self.seg46[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg47:
            rect = pygame.Rect(self.seg47[0] * 25 + 189, self.seg47[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg48:
            rect = pygame.Rect(self.seg48[0] * 25 + 189, self.seg48[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg49:
            rect = pygame.Rect(self.seg49[0] * 25 + 189, self.seg49[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg50:
            rect = pygame.Rect(self.seg50[0] * 25 + 189, self.seg50[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg51:
            rect = pygame.Rect(self.seg51[0] * 25 + 189, self.seg51[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg52:
            rect = pygame.Rect(self.seg52[0] * 25 + 189, self.seg52[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg53:
            rect = pygame.Rect(self.seg53[0] * 25 + 189, self.seg53[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg54:
            rect = pygame.Rect(self.seg54[0] * 25 + 189, self.seg54[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg55:
            rect = pygame.Rect(self.seg55[0] * 25 + 189, self.seg55[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg56:
            rect = pygame.Rect(self.seg56[0] * 25 + 189, self.seg56[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg57:
            rect = pygame.Rect(self.seg57[0] * 25 + 189, self.seg57[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg58:
            rect = pygame.Rect(self.seg58[0] * 25 + 189, self.seg58[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg59:
            rect = pygame.Rect(self.seg59[0] * 25 + 189, self.seg59[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg60:
            rect = pygame.Rect(self.seg60[0] * 25 + 189, self.seg60[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg61:
            rect = pygame.Rect(self.seg61[0] * 25 + 189, self.seg61[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg62:
            rect = pygame.Rect(self.seg62[0] * 25 + 189, self.seg62[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)
        
        if self.seg63:
            rect = pygame.Rect(self.seg63[0] * 25 + 189, self.seg63[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg64:
            rect = pygame.Rect(self.seg64[0] * 25 + 189, self.seg64[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg65:
            rect = pygame.Rect(self.seg65[0] * 25 + 189, self.seg65[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg66:
            rect = pygame.Rect(self.seg66[0] * 25 + 189, self.seg66[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg67:
            rect = pygame.Rect(self.seg67[0] * 25 + 189, self.seg67[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg68:
            rect = pygame.Rect(self.seg68[0] * 25 + 189, self.seg68[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg69:
            rect = pygame.Rect(self.seg69[0] * 25 + 189, self.seg69[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg70:
            rect = pygame.Rect(self.seg70[0] * 25 + 189, self.seg70[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg71:
            rect = pygame.Rect(self.seg71[0] * 25 + 189, self.seg71[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg72:
            rect = pygame.Rect(self.seg72[0] * 25 + 189, self.seg72[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg73:
            rect = pygame.Rect(self.seg73[0] * 25 + 189, self.seg73[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg74:
            rect = pygame.Rect(self.seg74[0] * 25 + 189, self.seg74[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg75:
            rect = pygame.Rect(self.seg75[0] * 25 + 189, self.seg75[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg76:
            rect = pygame.Rect(self.seg76[0] * 25 + 189, self.seg76[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg77:
            rect = pygame.Rect(self.seg77[0] * 25 + 189, self.seg77[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg78:
            rect = pygame.Rect(self.seg78[0] * 25 + 189, self.seg78[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.0), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg79:
            rect = pygame.Rect(self.seg79[0] * 25 + 189, self.seg79[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

        if self.seg80:
            rect = pygame.Rect(self.seg80[0] * 25 + 189, self.seg80[1] * 25 + 189, 23, 23)
            r, g, b = self.color
            dark_color = (int(r * 0.7), int(g * 0.7), int(b * 0.7))
            pygame.draw.rect(screen, dark_color, rect)

    def check_collision(self, min_coord, max_coord):
        # Check wall collision for head
        head = self.head
        if head[0] < min_coord or head[0] > max_coord or head[1] < min_coord or head[1] > max_coord:
            return True

        # Check self-collision with hardcoded segments
        if head == self.seg1:
            return True
        if head == self.seg2:
            return True
        if head == self.seg3:
            return True
        if head == self.seg4:
            return True
        if head == self.seg5:
            return True
        if head == self.seg6:
            return True
        if head == self.seg7:
            return True
        if head == self.seg8:
            return True
        if head == self.seg9:
            return True
        if head == self.seg10:
            return True
        if head == self.seg11:
            return True
        if head == self.seg12:
            return True
        if head == self.seg13:
            return True
        if head == self.seg14:
            return True
        if head == self.seg15:
            return True
        if head == self.seg16:
            return True
        if head == self.seg17:
            return True
        if head == self.seg18:
            return True
        if head == self.seg19:
            return True
        if head == self.seg20:
            return True
        if head == self.seg21:
            return True
        if head == self.seg22:
            return True
        if head == self.seg23:
            return True
        if head == self.seg24:
            return True
        if head == self.seg25:
            return True
        if head == self.seg26:
            return True
        if head == self.seg27:
            return True
        if head == self.seg28:
            return True
        if head == self.seg29:
            return True
        if head == self.seg30:
            return True
        if head == self.seg31:
            return True
        if head == self.seg32:
            return True
        if head == self.seg33:
            return True
        if head == self.seg34:
            return True
        if head == self.seg35:
            return True
        if head == self.seg36:
            return True
        if head == self.seg37:
            return True
        if head == self.seg38:
            return True
        if head == self.seg39:
            return True
        if head == self.seg40:
            return True
        if head == self.seg41:
            return True
        if head == self.seg42:
            return True
        if head == self.seg43:
            return True
        if head == self.seg44:
            return True
        if head == self.seg45:
            return True
        if head == self.seg46:
            return True
        if head == self.seg47:
            return True
        if head == self.seg48:
            return True
        if head == self.seg49:
            return True
        if head == self.seg50:
            return True
        if head == self.seg51:
            return True
        if head == self.seg52:
            return True
        if head == self.seg53:
            return True
        if head == self.seg54:
            return True
        if head == self.seg55:
            return True
        if head == self.seg56:
            return True
        if head == self.seg57:
            return True
        if head == self.seg58:
            return True
        if head == self.seg59:
            return True
        if head == self.seg60:
            return True
        if head == self.seg61:
            return True
        if head == self.seg62:
            return True
        if head == self.seg63:
            return True
        if head == self.seg64:
            return True
        if head == self.seg65:
            return True
        if head == self.seg66:
            return True
        if head == self.seg67:
            return True
        if head == self.seg68:
            return True
        if head == self.seg69:
            return True
        if head == self.seg70:
            return True
        if head == self.seg71:
            return True
        if head == self.seg72:
            return True
        if head == self.seg73:
            return True
        if head == self.seg74:
            return True
        if head == self.seg75:
            return True
        if head == self.seg76:
            return True
        if head == self.seg77:
            return True
        if head == self.seg78:
            return True
        if head == self.seg79:
            return True
        if head == self.seg80:
            return True

        return False


    def eats(self, fruit_pos):
        
        # Check if head is on fruit
        if self.head == fruit_pos:
            self.grow = True
            return True
        return False
    
    def reverse(self, ):
        pass