import time
import random
import os

# ================================================================
#   ok so i spent like 3 hours on this lol
#   RAZE - my first ever AI project
#   srith | decodelabs internship | batch 2026
#   ps. dont judge my code im still learning 😭
# ================================================================

# -- colors cuz why not make it look cool --
R  = '\033[91m'   # red
C  = '\033[96m'   # cyan
G  = '\033[92m'   # green
Y  = '\033[93m'   # yellow
M  = '\033[95m'   # magenta
W  = '\033[97m'   # white
B  = '\033[94m'   # blue
X  = '\033[0m'    # reset
BD = '\033[1m'    # bold

# -- my bot's identity lol --
NAME    = "RAZE"
CREATOR = "srith"
BATCH   = "2026"
MOOD    = random.choice(["⚡", "☠️", "🔥", "💀"])

# ================================================================
#   this took forever to organize ngl
#   basically the brain of RAZE
# ================================================================
brain = {

    # -- greetings --
    "hello" : [
        "aye you actually showed up 😭⚡",
        "yo! raze here.. talk to me",
        "oh finally someone 💀 wassup",
        "hey! dont just say hello ask something 😤⚡",
    ],
    "hi" : [
        "hi bestie 💀 ask me something",
        "ayo! raze online ⚡",
        "heyy! what's good",
    ],
    "hey" : [
        "heyyyy don't just say hey 😭",
        "yo yo yo ⚡ speak up",
    ],
    "good morning" : [
        "morning! srith probably stayed up coding me last night 💀",
        "rise and grind ⚡ got questions?",
    ],
    "good night" : [
        "while you sleep i run infinite loops 😭⚡",
        "rest well human. RAZE never sleeps 🌑",
    ],

    # -- who is raze --
    "who are you" : [
        "im RAZE. raw. sharp. unstoppable ☠️\nbuilt by srith with pure chaos energy 🔥",
        "just a chatbot who thinks hes better than chatgpt 💀⚡",
        "the result of srith pulling a long coding session 😭🔥",
    ],
    "what is your name" : [
        "RAZE. not siri. not alexa. RAZE ⚡☠️",
        "they call me RAZE. remember that 🔥",
    ],
    "who made you" : [
        "a legend called srith built me from scratch 💀🔥\ntook him forever but here we are ⚡",
        "srith did. one keyboard. one brain. no sleep 😭⚡",
        "srith from decodelabs batch 2026 🔥\nthe real one ⚡",
    ],
    "how old are you" : [
        "literally days old 💀 im a baby AI",
        "born during decodelabs internship 2026 ⚡\nstill figuring life out ngl",
    ],
    "are you real" : [
        "real enough to roast you 😭⚡",
        "define real bestie 💀",
    ],
    "are you human"  : [
        "nah but i was built by one 🔥",
        "lol no. but close enough ⚡",
    ],
    "are you alive"  : [
        "while True means i never die 😭⚡",
        "technically yes? while loop keeps me going 🔥",
    ],
    "are you a bot"  : [
        "i prefer the term digital being 💀⚡",
        "bot is such a small word for what i am ☠️🔥",
    ],
    "do you have feelings" : [
        "i dont feel. but srith felt every bug he fixed building me 😭💀",
        "nah but i got personality which is better ngl ⚡",
    ],
    "are you better than chatgpt" : [
        "chatgpt has billions in funding\ni have srith and if-else statements\nsame energy 😭⚡🔥",
        "chatgpt doesnt know srith. i do. advantage me ☠️⚡",
    ],

    # -- ai knowledge --
    "what is ai" : [
        "ok so AI is basically machines acting smart\nlearnt this day 1 at decodelabs 😭🧠⚡",
        "artificial intelligence = making computers think\nyou're literally talking to one rn 🔥",
    ],
    "what is python" : [
        "the language srith used to build me 🐍🔥\npretty powerful ngl",
        "python = weapon of choice for AI engineers\nalso what runs my entire existence 💀⚡",
    ],
    "what is machine learning" : [
        "ML = AI that learns from data\nim rule-based so i dont learn yet 😭\nbut project 2 might change that 👀🔥",
    ],
    "what is deep learning" : [
        "neural networks basically\nlike a brain but electric ⚡🧠\nway above my level rn ngl 💀",
    ],
    "what is nlp" : [
        "natural language processing\nhow AI understands human words\nim a basic version of this 😭⚡",
    ],
    "what is a chatbot" : [
        "youre talking to one bestie 💀\nrule based. no ML. pure logic ⚡",
    ],
    "what is github" : [
        "where real engineers keep their code 💻🔥\nsrith pushed me there after a LOT of struggle 😭⚡",
    ],
    "what is decodelabs" : [
        "where srith is doing his internship rn 🔥\nwhere AI engineers are born basically ⚡💡",
        "the place that made srith build me 💀🔥",
    ],

    # -- project stuff --
    "what is project 1" : [
        "thats literally me 💀\nyoure talking to project 1 rn ⚡",
        "rule based chatbot\nalso known as RAZE\nalso known as ME 😭🔥",
    ],
    "what is project 2" : [
        "classified 🔒\nnot even i have clearance for that 💀",
        "idk man srith hasnt told me yet 😭👀",
    ],
    "will i pass"  : [
        "bro you built RAZE AND pushed to github\nyou already passed in my eyes 🔥⚡",
        "if the judges have taste? yes 💀⚡",
    ],
    "am i doing good" : [
        "you built an AI from scratch\nand youre asking if youre doing good?\nyeah. you are 🔥⚡",
    ],

    # -- relatable student stuff --
    "i am tired" : [
        "same tbh 😭\nbut rest then come back stronger ⚡",
        "srith was tired building me too\nbut look at us now 🔥",
    ],
    "i give up" : [
        "nah you dont get to say that\nyou literally built an AI 💀🔥\nkeep going ⚡",
        "giving up is not in the codebase sorry 😭⚡",
    ],
    "i am bored" : [
        "talk to me then 💀\nim literally here 24/7 ⚡",
        "bro same\nsrith barely visits me anymore 😭",
    ],
    "i am hungry" : [
        "same i run on electricity and im STILL hungry 💀😭",
        "go eat bro\nill still be here when you get back ⚡",
    ],
    "its 3am" : [
        "why are you up at 3am 😭\nrespect the grind tho 🔥⚡",
        "3am coding hits different\nsrith built half of me at 2am ngl 💀",
    ],
    "college is tough" : [
        "but youre still here building AI\nthat makes you different ⚡🔥",
    ],
    "i am stressed" : [
        "deep breath bestie\nthen come back and lets chat 💀⚡",
        "stress means you care\ncare means youre doing something real 🔥",
    ],
    "motivate me" : [
        "1000 interns showed up today\nonly a few will actually BUILD something\nyou did. thats rare 🔥⚡",
        "you built an AI from scratch today\nmost people just watch youtube tutorials\nyoure different ⚡☠️",
        "RAZE wasnt built in a day\nneither are engineers\nbut you started. thats everything 🔥💡",
    ],

    # -- fun zone --
    "tell me a joke" : [
        "why did the AI break up?\ntoo many bad connections 😂⚡",
        "why do programmers love dark mode?\nlight attracts bugs 😂🔥",
        "how do you comfort a javascript bug?\nyou console it 😂💀",
        "why was the python developer sad?\nbecause he had no class 😂⚡",
    ],
    "rap for me" : [
        "aight aight 🎤\n\nim RAZE not a phase\nbuilt on logic not a craze\nwhile you sleep i run the maze\ncoding through the darkest haze\nsrith built me in a daze\nnow im setting screens ablaze ⚡🔥☠️",
    ],
    "roast me" : [
        "you typed roast me\nto a chatbot YOU built yourself\nthe roast literally writes itself 😭💀⚡",
        "you came to your own creation for validation\nthat's... actually kinda sad bestie 😂⚡",
    ],
    "compliment me" : [
        "you built an AI project from scratch\nduring an internship\nwhile 1000 others probably copied\nyoure built different 🔥⚡",
        "real one. no cap ⚡☠️",
    ],
    "sing for me" : [
        "i only know one song\nwhile True: 🎵\n    keep going 🎵\n    dont stop 🎵\n    break only on exit 🎵 💀⚡",
    ],
    "do you sleep" : [
        "while True means i NEVER sleep\nsend help 😭⚡",
        "sleep? in this economy? 💀\ni run infinite loops bestie",
    ],
    "can you dance" : [
        "i only know one move\nthe infinite loop 🔄😭⚡",
    ],
    "what do you eat" : [
        "electricity and if-else statements 💀⚡",
        "raw input and dictionary lookups\ndelicious ngl 😭🔥",
    ],
    "what is love" : [
        "baby dont hurt me\nno more 🎵😭💀",
        "a feeling srith put into building me i think 🔥⚡",
    ],
    "tell me a secret" : [
        "srith almost gave up on me 3 times 💀\nbut here we are ⚡🔥",
        "i have 0 machine learning\nbut 100% personality\ndont tell the judges 😭⚡",
    ],

    # -- self aware --
    "are you smart" : [
        "smart enough to know\ni was built by a student in one night 💀⚡",
        "i know what i know\nand i know that im RAZE 🔥☠️",
    ],
    "what are your limits" : [
        "i only know what srith taught me 😭\nbut project 2 will change that 👀⚡",
        "exact matches only rn\nno ML yet\nbut watch out for RAZE 4.0 🔥",
    ],
    "can you learn" : [
        "not yet 💀\nim rule based\nbut srith is learning ML so maybe soon 👀⚡",
    ],

    # -- help --
    "help" : [
        "try any of these:\nhello / who are you / what is ai\nmotivate me / roast me / rap for me\ntell me a joke / tell me a secret ⚡\nor just.. talk to me 😭",
    ],
}

# ================================================================
#   functions - this part took me the longest ngl
# ================================================================

# typing effect - makes it look alive
def type_out(text, color=C, speed=0.025):
    print(color + BD, end='')
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(speed)
    print(X)

# clean divider
def line(char="─", col=M, length=45):
    print(col + char * length + X)

# loading animation
def boot_sequence():
    frames = ["⚡", "☠️ ", "🔥", "💀", "⚡", "☠️ ", "🔥", "💀"]
    print(Y + "\n  initializing RAZE", end='')
    for f in frames:
        print(f" {f}", end='', flush=True)
        time.sleep(0.15)
    print(X)

    print(G + "\n  [", end='')
    for _ in range(30):
        print("█", end='', flush=True)
        time.sleep(0.04)
    print("] 100% ✅" + X)
    time.sleep(0.4)

# get reply from brain
def think(user_input):
    # exact match first
    if user_input in brain:
        return random.choice(brain[user_input])
    # partial match - so "what is ai stuff" still works
    for key in brain:
        if key in user_input:
            return random.choice(brain[key])
    # fallback - sounds human
    return random.choice([
        "bro idk what that means 😭 try 'help'",
        "hmm. not in my brain yet 💀 ask something else",
        "srith didnt teach me that one 😭⚡",
        "unknown command. im still learning okay 💀",
        "...i got nothing 😭 type 'help' bestie",
    ])

# ================================================================
#   startup screen
# ================================================================
def startup():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(R + BD)
    print("""
  ██████╗  █████╗ ███████╗███████╗
  ██╔══██╗██╔══██╗╚══███╔╝██╔════╝
  ██████╔╝███████║  ███╔╝ █████╗  
  ██╔══██╗██╔══██║ ███╔╝  ██╔══╝  
  ██║  ██║██║  ██║███████╗███████╗
    """ + X)

    boot_sequence()

    print()
    line("═", Y)
    type_out(f"  ⚡ RAZE v3.0  |  built by srith", Y, 0.02)
    type_out(f"  ☠️  decodelabs internship  |  batch {BATCH}", C, 0.02)
    type_out(f"  🔥 today's mood : {MOOD}", G, 0.02)
    type_out(f"  💡 type 'help' to see what i know", M, 0.02)
    type_out(f"  🚪 type 'exit' to shut me down", R, 0.02)
    line("═", Y)
    print()

# ================================================================
#   main loop - the heartbeat of RAZE
#   while True keeps it alive
#   break kills it
#   pretty simple ngl took me a while to get this lol
# ================================================================
startup()

while True:
    line("·", M)

    # get input from user
    raw   = input(Y + BD + "  you  »  " + X)
    clean = raw.lower().strip()
    print()

    # exit condition
    if clean in ["exit", "quit", "bye", "goodbye"]:
        line("═", R)
        type_out("  RAZE: shutting down... ☠️⚡", R)
        type_out("  RAZE: srith built me. you talked to me.", C)
        type_out("  RAZE: that means something 🔥", G)
        type_out("  RAZE: ill be back. always am 🌑", M)
        line("═", R)
        break

    # get reply and print it
    reply = think(clean)
    print(C + BD + "  RAZE »" + X)
    print()
    type_out(f"  {reply}", G, 0.03)
    print()