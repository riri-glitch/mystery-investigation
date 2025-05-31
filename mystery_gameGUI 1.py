import customtkinter as ctk
from tkinter import messagebox


# Initialize the custom theme
ctk.set_appearance_mode("dark")  # Or "light"
ctk.set_default_color_theme("green")

# Setup main window
app = ctk.CTk()
app.title("Case of the Missing Mug")
app.geometry("800x500")

# Inventory list
inventory = []

def start_game():
    start_button.grid_remove()
    intro_scene()


# Function to update the main text area
def update_story(text, add_break=False):
    story_display.configure(state="normal")
    story_display.insert("end", text + "\n\n")
    if add_break:
        story_display.insert("end", "~"*60 + "\n\n")
    story_display.configure(state="disabled")
    story_display.see("end")


# Function to update inventory box
def update_inventory():
    inventory_box.configure(state="normal")
    inventory_box.delete("1.0", "end")
    for item in inventory:
        inventory_box.insert("end", f"- {item}\n")
    inventory_box.configure(state="disabled")

def show_intro_screen():
    # Clear the story area first
    story_display.configure(state="normal")
    story_display.delete("1.0", "end")
    story_display.insert("end", 
        "🕵️ Welcome to the *Case of the Missing Mug* — a mystery with more caffeine than clues.\n\n"
        "You are an unpaid intern turned detective because the boss (Ayodeji)'s favourite mug vanished.\n\n"
        "Suspects? A whole office of weirdos.\n\n"
        "Let's Begin..."
    )
    story_display.configure(state="disabled")

    # Hide other buttons
    choice_button_1.grid_remove()
    choice_button_2.grid_remove()
    choice_button_3.grid_remove()
    choice_button_4.grid_remove()
    choice_button_5.grid_remove()
    restart_button.grid_remove()

    # Show Start Game button
    start_button.grid(row=1, column=1, pady=10)

def intro_scene(): 
    update_story("", add_break=True)   
    update_story("You're in the break room. It's clean — well, mostly clean.")
    update_story("You see two things: a suspicious coffee stain and a locked drawer.")
    update_story("What do you want to do?", add_break=True)

    choice_button_1.configure(text="Inspect the coffee stain", command=inspect_stain)
    choice_button_2.configure(text="Try to open the drawer", command=open_drawer)
    choice_button_3.configure(text="Kick the vending machine", command=kick_machine)
    choice_button_4.grid_remove()  # New 4th button
    choice_button_5.grid_remove()
    choice_button_1.grid()
    choice_button_2.grid()
    choice_button_3.grid()


def scene_hallway():
    update_story("", add_break=True)
    update_story("You step into the hallway. It's eerily quiet...")
    update_story("Three doors ahead, which do you choose? ")
    update_story("1. Ayodeji's Office\n2. Mary from ServiceDesk's Desk\n3. Go back to Break Room", add_break=True)

    choice_button_1.configure(text="Enter Ayodeji's Office", command=scene_ayodeji_office)
    choice_button_2.configure(text="Check Mary’s Desk", command=scene_mary_desk)
    choice_button_3.configure(text="Back to Break Room", command=intro_scene)
    choice_button_4.configure(text="Question Someone", command=scene_interrogate_suspects)
    choice_button_1.grid()
    choice_button_2.grid()
    choice_button_3.grid()
    choice_button_4.grid()

def scene_ayodeji_office():
    update_story("", add_break=True)
    update_story("The door creaks open. Manager's office is messy, like a tornado hit it.")
    update_story("You spot a suspicious file labeled 'Operation: Hot Mug'. You pocket it.")
    if "Secret File" not in inventory:
        inventory.append("Secret File")
        update_inventory()

def scene_mary_desk():
    update_story("", add_break=True)
    update_story("Mary’s desk is guarded by a plastic flamingo and 5 mugs.")
    update_story("You find a sticky note that reads: 'He knows about the mug.'")
    if "Mary's Sticky Note" not in inventory:
        inventory.append("Mary's Sticky Note")
        update_inventory()


# Choice responses
def inspect_stain():
    update_story("", add_break=True)
    update_story("You inspect the stain... hazelnut coffee. The boss hates hazelnut.")
    choice_button_4.configure(text="Leave break room", command=scene_hallway)
    choice_button_4.grid()
    if "Hazelnut Coffee Clue" not in inventory:
        inventory.append("Hazelnut Coffee Clue")
        update_inventory()

def open_drawer():
    update_story("", add_break=True)
    update_story("The drawer is locked. You hear something rattling inside. Suspicious...")
    choice_button_4.configure(text="Leave break room", command=scene_hallway)
    choice_button_4.grid()

def kick_machine():
    update_story("", add_break=True)
    update_story("You kick the vending machine. A pack of stale pretzels falls out.")
    if "Suspicious Pretzels" not in inventory:
        inventory.append("Suspicious Pretzels")
        update_inventory()

def scene_interrogate_suspects():
    update_story(text="", add_break=True)
    update_story("🔍 Who would you like to question?")
    update_story("1. Mary (ServiceDesk)\n2. Oliver (IT)\n3. Jane (HR)\n4. Ayodeji (Manager)\n5. Done questioning — I want to accuse someone.")

    choice_button_1.configure(text="Question Mary", command=question_mary)
    choice_button_2.configure(text="Question Oliver", command=question_oliver)
    choice_button_3.configure(text="Question Jane", command=question_jane)
    choice_button_4.configure(text="Question Ayodeji", command=question_ayodeji)
    # Add a new 5th button for done
    choice_button_5.configure(text="Done Questioning", command=scene_accusation)
    choice_button_5.grid()
    choice_button_3.grid()
    choice_button_4.grid()


def question_mary():
    update_story(text="", add_break=True)
    update_story("You approach Mary’s desk. She's typing furiously with a very loud mechanical keyboard.")
    update_story("🗨️ Mary: ‘If this is about the mug, I didn’t take it. Unlike some people, I *buy* my own.’ She says without looking up.")
    update_story("🧠 You notice she has five mugs on her desk. All labeled ‘Mary’. All labeled ‘Mary’ in Comic Sans.")
    update_story("\nWhat do you want to ask?")
    
    choice_button_1.configure(text="Ask about the sticky note", command=mary_sticky_note)
    choice_button_2.configure(text="Ask why she needs five mugs", command=mary_five_mugs)
    choice_button_3.grid_remove()
    choice_button_4.grid_remove()
    choice_button_5.grid_remove()

def mary_sticky_note():
    update_story(text="", add_break=True)
    update_story("She scoffs. ‘That note was for Oliver. He kept “borrowing” the boss’s mug like it was community property.’")
    if "Mary accuses Oliver" not in inventory:
        inventory.append("Mary accuses Oliver")
        update_inventory()
    scene_interrogate_suspects()

def mary_five_mugs():
    update_story(text="", add_break=True)
    update_story("She glares at you. ‘Hydration is important. Do *you* want to get a kidney stone?’")
    scene_interrogate_suspects()


def question_oliver():
    update_story(text="", add_break=True)
    update_story("You find Oliver in the server room, surrounded by blinking lights and munching on crisps.")
    update_story("🗨️ Oliver: ‘If this is about the mug, ask Mary. She’s been weirdly possessive of the break room lately.’")
    update_story("\nWhat do you want to ask?")

    choice_button_1.configure(text="Ask if he ever used Ayodeji's mug", command=oliver_use_mug)
    choice_button_2.configure(text="Ask if he's seen anything suspicious on the security cameras", command=oliver_cams)
    choice_button_3.grid_remove()
    choice_button_4.grid_remove()
    choice_button_5.grid_remove()

def oliver_use_mug():
    update_story(text="", add_break=True)
    update_story("Oliver shrugs. ‘Maybe once or twice. It was clean. I needed caffeine. I was desperate.’")
    if "Oliver used the mug" not in inventory:
        inventory.append("Oliver used the mug")
        update_inventory()
    scene_interrogate_suspects()

def oliver_cams():
    update_story(text="", add_break=True)
    update_story("He leans in. ‘Jane erased some footage from the day it went missing. Said it was “an HR matter.”’")
    if "Jane erased footage" not in inventory:
        inventory.append("Jane erased footage")
        update_inventory()
    scene_interrogate_suspects()

def question_jane():
    update_story(text="", add_break=True)
    update_story("You enter HR and find Jane alphabetizing sticky notes. She looks up and smiles too warmly.")
    update_story("🗨️ Jane: ‘Hello! I’m sure you’re here about the mug. Such a tragedy. Do you have an appointment?’")
    update_story("\nDo you?")

    choice_button_1.configure(text="Ask about the deleted security footage", command=jane_deleted_foot)
    choice_button_2.configure(text="Ask if she knows who might have taken it", command=jane_who_took_it)
    choice_button_3.grid_remove()
    choice_button_4.grid_remove()
    choice_button_5.grid_remove()

def jane_deleted_foot():
    update_story(text="", add_break=True)
    update_story("Her smile tightens. ‘That footage was removed due to... privacy concerns. Not everything is your business, detective.’")
    if "Jane is hiding something" not in inventory:
        inventory.append("Jane is hiding something")
        update_inventory()
    scene_interrogate_suspects()

def jane_who_took_it():
    update_story(text="", add_break=True)
    update_story("She lowers her voice. ‘Ayodeji drinks from that mug like it’s sacred. I wouldn’t be surprised if he misplaced it himself.’")
    if "Jane suspects Ayodeji" not in inventory:
        inventory.append("Jane suspects Ayodeji")
        update_inventory()
    scene_interrogate_suspects()

def question_ayodeji():
    update_story(text="", add_break=True)
    update_story("You find Ayodeji dramatically gazing out the window like he's in a Netflix original series.")
    update_story("🗨️ Ayodeji: ‘That mug was a gift from my mentor. Do you understand what that *means*?’ he says, turning slowly.")
    update_story("\nDo you?")

    choice_button_1.configure(text="Ask if he might have misplaced it", command=ayodeji_misplace)
    choice_button_2.configure(text="Ask if he suspects anyone", command = ayodeji_suspect)
    choice_button_3.grid_remove()
    choice_button_4.grid_remove()
    choice_button_5.grid_remove()

def ayodeji_misplace():
    update_story(text="", add_break=True)
    update_story("He gasps. ‘Are you implying I’m careless? I kept it in a drawer. A drawer I *locked*.’")
    if "Mug was in locked drawer" not in inventory:
        inventory.append("Mug was in locked drawer")
        update_inventory()
    scene_interrogate_suspects()

def ayodeji_suspect():
    update_story(text="", add_break=True)
    update_story("He points dramatically. ‘Mary. She’s had it out for me ever since I didn’t approve her request for a sixth mug.’")
    if "Ayodeji accuses Mary" not in inventory:
        inventory.append("Ayodeji accuses Mary")
        update_inventory()
    scene_interrogate_suspects()

def scene_accusation():
    update_story(text="", add_break=True)
    update_story("🧠 Time to make your accusation. Who stole the sacred mug?")
    
    choice_button_1.configure(text="Accuse Mary", command=accuse_mary)
    choice_button_2.configure(text="Accuse Oliver", command=accuse_oliver)
    choice_button_3.configure(text="Accuse Jane", command=accuse_jane)
    choice_button_4.configure(text="Accuse Ayodeji", command=accuse_ayodeji)
    choice_button_5.configure(text="Leave... unsolved", command=accuse_nobody)

def accuse_mary():
    update_story(text="", add_break=True)
    if "Hazelnut Coffee Clue" in inventory and "Ayodeji accuses Mary" in inventory or "Mary accuses Oliver" in inventory:
        end_game("💥 BOOM. You confront Mary with the clues.\nShe breaks.\n  🗨️ Mary: ‘Fine! I took it! It was just... such a nice mug and Ayodeji wouldn't approve my sixth one.’\nJustice is served. You're still unpaid, but at least you're respected now.")
    else:
        end_game("Mary gasps.\n🗨️ Mary: ‘Me? How dare you!’\nWithout solid evidence, HR sends you to the meditation room for 'retraining.' Game over.")

def accuse_oliver():
    update_story(text="", add_break=True)
    end_game("You accuse Oliver. He just shrugs.\n 🗨️ Oliver: ‘Cool.’\nTurns out, he's been stealing office pens,and candy from desks not mugs. Wrong criminal.")

def accuse_jane():
    update_story(text="", add_break=True)
    end_game("You accuse Jane. She smiles and hands you a pamphlet.\nYou're now signed up for a mandatory empathy workshop. Turns out she deleted the footage because she was picking her nose.")

def accuse_ayodeji():
    update_story(text="", add_break=True)
    end_game("You accuse Ayodeji. He looks deeply offended and later posts a vague tweet about betrayal.\nStill no mug. You're off the case.")

def accuse_nobody():
    update_story(text="", add_break=True)
    end_game("You accuse... no one. The mug is never found.\nWeeks later, someone sees it on eBay. The case remains unsolved.")

def end_game(message):
    story_display.configure(state="normal")
    story_display.delete("1.0", "end")
    story_display.insert("end", f"🎉 {message}\n\n")
    story_display.insert("end", "🔚 Game Over\n\n")
    story_display.configure(state="disabled")

    # Hide all choice buttons
    choice_button_1.grid_remove()
    choice_button_2.grid_remove()
    choice_button_3.grid_remove()
    choice_button_4.grid_remove()
    choice_button_5.grid_remove()

    # Show a restart button using grid (not pack)
    restart_button.grid(row=3, column=1, pady=10)

def reset_game():
    inventory.clear()
    update_inventory()

    story_display.configure(state="normal")
    story_display.delete("1.0", "end")
    story_display.configure(state="disabled")

    # Show buttons again
    choice_button_1.grid()
    choice_button_2.grid()
    choice_button_3.grid()
    choice_button_4.grid()
    choice_button_5.grid()
    restart_button.grid_remove()

    show_intro_screen()

def confirm_exit():
    if messagebox.askyesno("Exit Game", "Are you sure you want to quit?"):
        app.destroy()




# Layout
left_frame = ctk.CTkFrame(app)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right_frame = ctk.CTkFrame(app, width=200)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

story_display = ctk.CTkTextbox(left_frame, wrap="word", height=300)
story_display.pack(fill="both", expand=True)
story_display.configure(state="disabled")

button_frame = ctk.CTkFrame(left_frame)
button_frame.pack(pady=10)

choice_button_1 = ctk.CTkButton(button_frame, text="Choice 1", command=None)
choice_button_1.grid(row=0, column=0, padx=5)

choice_button_2 = ctk.CTkButton(button_frame, text="Choice 2", command=None)
choice_button_2.grid(row=0, column=1, padx=5)

choice_button_3 = ctk.CTkButton(button_frame, text="Choice 3", command=None)
choice_button_3.grid(row=0, column=2, padx=5)

choice_button_4 = ctk.CTkButton(button_frame, text="Choice 4", command=None)
choice_button_4.grid(row=1, column=1, padx=5, pady=5)

choice_button_5 = ctk.CTkButton(button_frame, text="Choice 5", command=None)
choice_button_5.grid(row=3, column=1, padx=5, pady=5)

restart_button = ctk.CTkButton(button_frame, text="🔁 Try Again", command=reset_game)
restart_button.grid(row=3, column=1, pady=10)
restart_button.grid_remove()  # hide it initially

exit_button = ctk.CTkButton(button_frame, text="🚪 Exit Game", command=confirm_exit)
exit_button.grid(row=4, column=1, pady=10)

start_button = ctk.CTkButton(button_frame, text="▶️ Start Game", command=start_game)
start_button.grid(row=1, column=1, pady=10)
start_button.grid_remove()  # hide initially








inventory_label = ctk.CTkLabel(right_frame, text="🧾 Inventory", font=("Arial", 16))
inventory_label.pack(pady=(10, 5))

inventory_box = ctk.CTkTextbox(right_frame, height=200, width=180)
inventory_box.pack()
inventory_box.configure(state="disabled")

# Start game
show_intro_screen()
app.mainloop()
