import time
import os

# ANSI color codes for lights
COLORS = [
    '\033[91m',  # Red
    '\033[93m',  # Yellow
    '\033[92m',  # Green
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
]
RESET = '\033[0m'
GREEN = '\033[92m'

# Tree structure with positions for lights
tree_lines = [
    "       *       ",
    "      ***      ",
    "     *****     ",
    "    *******    ",
    "   *********   ",
    "  ***********  ",
    " ************* ",
    "      |||      "
]

# Light positions for each row (excluding star and trunk)
light_positions = [
    [1],           # row 1
    [0, 2],        # row 2
    [0, 2, 4],     # row 3
    [1, 3, 5],     # row 4
    [0, 3, 6, 8],  # row 5
    [1, 4, 7, 10], # row 6
    [0, 3, 6, 9, 12] # row 7
]

# Lyrics with timing
lyrics = [
    "A face on a lover",
    "With a fire in his heart",
    "A man undercover",
    "But you tore me apart",
    "Oh oh",
    "Oh oh",
    "Now I've found a real love",
    "You'll never fool me again"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_tree_with_lights(frame):
    """Generate tree with animated lights"""
    result = []
    
    # Star at top (always yellow)
    result.append(tree_lines[0].replace('*', f'{COLORS[1]}*{RESET}'))
    
    # Tree body with animated lights
    for i, line in enumerate(tree_lines[1:7]):
        colored_line = ""
        star_count = 0
        
        for char in line:
            if char == '*':
                # Check if this position should be lit
                if star_count in light_positions[i]:
                    # Cycle through colors based on frame
                    color_idx = (frame + star_count) % len(COLORS)
                    colored_line += f'{COLORS[color_idx]}●{RESET}'
                else:
                    colored_line += f'{GREEN}●{RESET}'
                star_count += 1
            else:
                colored_line += char
        
        result.append(colored_line)
    
    # Trunk
    result.append(tree_lines[7].replace('|', f'{COLORS[1]}|{RESET}'))
    
    return result

def display_frame(tree, lyric_index):
    """Display tree and lyrics side by side"""
    clear_screen()
    print("\n")
    
    # Display tree with lyrics on the right
    for i, tree_line in enumerate(tree):
        # Show lyrics aligned with tree rows
        if i < len(lyrics) and i <= lyric_index:
            if i == lyric_index:
                # Current lyric in bright green
                print(f"{tree_line}    {GREEN}{lyrics[i]}{RESET}")
            else:
                # Previous lyrics in white
                print(f"{tree_line}    {lyrics[i]}")
        else:
            print(tree_line)
    
    print()

def animate():
    """Main animation loop"""
    frame = 0
    lyric_index = 0
    interval = 1.5  # seconds between lyrics
    
    try:
        while lyric_index < len(lyrics):
            tree = get_tree_with_lights(frame)
            display_frame(tree, lyric_index)
            
            time.sleep(0.2)  # Fast animation for lights
            frame += 1
            
            # Change lyric every interval
            if frame % int(interval / 0.2) == 0 and lyric_index < len(lyrics) - 1:
                lyric_index += 1
        
        # Keep showing for a bit after last lyric
        for _ in range(15):
            tree = get_tree_with_lights(frame)
            display_frame(tree, lyric_index)
            time.sleep(0.2)
            frame += 1
            
    except KeyboardInterrupt:
        print("\n\n✨ Merry Christmas! ✨\n")

if __name__ == "__main__":
    animate()