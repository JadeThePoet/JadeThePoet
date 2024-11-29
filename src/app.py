import os
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'src', 'web', 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    style = request.form['style']
    lines = int(request.form['lines']) if style == 'free' else None
    
    poem = generate_poem(style, lines)
    
    return jsonify({
        'poem': poem,
        'style': style,
        'lines': lines
    })

def generate_poem(style, lines):
    if style == 'haiku':
        return generate_haiku()
    elif style == 'limerick':
        return generate_limerick()
    else:  # free verse
        return generate_free_verse(lines)

def generate_haiku():
    haiku_lines = {
        "line1": [
            "whispering", "falling", "silent", "shimmering", "ancient", "lonely", "fading", "gentle", "wandering", "crystal",
            "trembling", "echoing", "dreaming", "glimmering", "twilight", "distant", "rising", "sinking", "silent", "starry",
            "drifting", "frosted", "star", "glowing", "tender", "serene", "moonlit", "twinkling", "chilly", "melancholy",
            "crimson", "vivid", "clouded", "rising", "shining", "reflecting", "glimmer", "shadows", "dust", "breeze", 
            "seeping", "floating", "whirling", "fragrant", "misty", "turbulent", "calm", "broken", "whisper", "glow", 
            "bursting", "fragment", "silent", "hidden", "sorrow", "wilted", "rays", "tangled", "soaring", "trembling", 
            "warm", "glowing", "invisible", "pale", "dimming", "receding", "fragile", "blushing", "night", "deep", 
            "lucid", "vibrating", "quiet", "cloud", "shattered", "whirling", "freezing", "endless", "green", "falling", 
            "lone", "leaves", "rays", "glistening", "hazy", "melting", "spiraling", "infinite", "tattered", "tide", 
            "solitary", "drifting", "glittering", "fragrance", "haunting", "unseen", "meadow", "wilted", "numb", 
            "thundering", "melancholic", "expanding", "serene", "roaring", "languid", "vibrant", "turbulent", "shining",
            "tremulous", "whispering", "soothing", "fractured", "timeless", "unbroken", "glimmering", "exhaling", "haunting"
        ],
        "line2": [
            "rising", "floating", "drifting", "shining", "calling", "screaming", "falling", "glimmering", "whispers", 
            "melting", "dancing", "waking", "flowing", "burning", "whirling", "gliding", "soaring", "reaching", 
            "awakening", "rippling", "flowing", "crashing", "sweeping", "breaking", "glistening", "flickering", 
            "shimmering", "beaming", "growing", "raging", "glistening", "whispering", "howling", "soaring", "blazing", 
            "surging", "dreaming", "vibrating", "trembling", "whispering", "climbing", "echoing", "dissolving", 
            "illuminating", "rising", "leaping", "twisting", "spinning", "vibrating", "shining", "flashing", "dancing", 
            "blazing", "rippling", "glowing", "glistening", "burning", "crackling", "tumbling", "twisting", "thriving", 
            "erupting", "murmuring", "pulsing", "whirling", "shivering", "whistling", "glowing", "shaking", "thundering", 
            "brimming", "drifting", "whirling", "revolving", "swelling", "undulating", "floating", "bubbling", 
            "shifting", "whistling", "crashing", "shivering", "whirling", "rising", "splendid", "whistling", "rushing",
            "raging", "swirling", "boiling", "fracturing", "trembling", "glimmering", "melting", "howling", "rising", 
            "vibrating"
        ],
        "line3": [
            "above", "below", "beneath", "beyond", "near", "across", "inside", "around", "among", "within", "towards", 
            "through", "toward", "embrace", "fade", "grasp", "the edge", "outward", "unseen", "torn", "alone", "out of sight", 
            "hiding", "whispering", "beyond", "flicker", "out of time", "quietly", "elusive", "aether", "stars", "fall", 
            "rays", "chill", "burn", "blaze", "whisper", "falling", "reflected", "horizon", "dreaming", "lullaby", 
            "solitude", "floating", "twilight", "tumble", "melancholy", "darkness", "sweeping", "glistening", "reflection", 
            "flicker", "chilling", "growing", "fractured", "suspended", "dreams", "endless", "vivid", "tattered", "glimmering", 
            "glistening", "shadows", "void", "fluttering", "floating", "spiraling", "stirring", "unbroken", "unseen", 
            "whisper", "tremble", "sinking", "fading", "soul", "infinite", "glow", "drift", "suspended", "whispering", 
            "suspended", "invisible", "still", "fragrant", "desolate", "resonating", "vibration", "echo", "starlit", 
            "whirling", "burn", "solitary", "ghost", "soul", "whisper", "crimson", "serene", "radiating", "soulful", 
            "ageless", "beneath", "overwhelming", "undisturbed", "enchanted", "dreamlike", "everlasting", "sublime", 
            "unknown", "alight", "burning", "radiating", "soulful", "trembling", "haunting", "drifting", "reflective", "dimming",
            "restless"
        ]
    }

    line1 = f"{random.choice(haiku_lines['line1'])} {random.choice(haiku_lines['line1'])}"
    line2 = f"{random.choice(haiku_lines['line2'])} {random.choice(haiku_lines['line2'])}"
    line3 = f"{random.choice(haiku_lines['line3'])} {random.choice(haiku_lines['line3'])}"

    return f"{line1}\n{line2}\n{line3}"

def generate_limerick():
    limericks = [
        # Previous limericks
        "There once was a cat from Kent\nWhose fur was quite silkily bent\nIt twisted in knots\nAnd tangled in spots\nTill it went to the vet for an event",
    "A man from the town of Lille\nLoved riding his unicycle\nHe'd spin and he'd twirl\nWith a swoop and a swirl\nUntil he slipped on a bicycle",
    "A boy from the village of Lou\nHad a frog he adored and it grew\nIt hopped on his head\nAnd then onto his bed\nMaking everything smell like stew",
    "There was a young girl from the isle\nWhose laugh could make others smile\nShe'd giggle all day\nIn a cheerful display\nAnd run through the sand for a mile",
    "A chef from the town of Prague\nWould bake pies, both sweet and a slog\nHis crusts were divine\nAnd his fillings fine\nTill he baked his hat in a fog",
    "A woman from Venice so fair\nHad a parrot who loved the air\nIt would sing songs of cheer\nAnd fly near the pier\nWhile the lady would comb her hair",
    "There once was a man from the street\nWho wore shoes that had holes in their feet\nHe'd run with a leap\nThrough puddles so deep\nUntil he got caught in a treat",
    "A squirrel from the woods of Maine\nHad a habit that caused him much pain\nHe'd stash all his nuts\nIn his friends' huts\nTill they said, 'Come on, that's insane!'",
    "There was a young man from the moor\nWho loved to explore every door\nHe'd knock with great force\nAnd leave on his horse\nTill he found one he'd adore",
    "A woman from old Baton Rouge\nMade a sandwich with fish, not a snooze\nShe'd eat it at night\nBy the pale moonlight\nTill the cat stole her food, what a ruse",
    "There once was a pirate named Finn\nWho had a small boat, sleek and thin\nHe sailed on the seas\nWith a breeze in his knees\nAnd caught fish with a cheeky grin",
    "A dog in a faraway town\nAlways wore a bright golden crown\nIt would bark at the moon\nAnd howl a good tune\nWhile wearing its royal renown",
    "A man from the hills of Skye\nWould build castles up to the sky\nHe'd stack them with care\nAnd then sit in a chair\nAdmiring the clouds drifting by",
    "There was a young lady from Cork\nWho'd eat chicken with a fork\nShe'd dip it in spice\nAnd say, 'Isn't this nice?'\nWhile dancing with a mighty cork",
    "A boy from the town of Biltmore\nHad a balloon he would adore\nIt floated so high\nAnd touched the sky\nTill the wind blew it to the floor",
    "A baker from the village of Rye\nWould bake bread that would always fly\nIt leapt from the oven\nAnd ran to the coven\nWhere witches would stop by and buy",
    "There was an old man from the bay\nWho painted his boat every day\nIt was yellow and blue\nAnd the sun's warm hue\nAnd he sailed it so far away",
    "A girl from the streets of Rome\nHad a dog that would always roam\nIt'd chase every cat\nAnd then wear a hat\nTill it was brought back home",
    "A farmer from distant Stowe\nHad a pig that loved to glow\nIt sparkled at night\nAnd gleamed in the light\nMaking the whole town say, 'Whoa!'",
    "There was a man from the zoo\nWhose pet llama had shoes of blue\nIt'd run with a hop\nAnd spin with a plop\nTill it danced on the moon, what a view!",
    "A man from the town of Sedge\nHad a fence made of a hedge\nHe'd trim it with care\nTill it was so square\nAnd stood on a very tall ledge",
    "There once was a queen named June\nWho loved to play a sweet tune\nShe'd strum on her harp\nIn a peaceful park\nAnd dance to the rhythm at noon",
    "A man from the town of Glee\nHad a singing fish in the sea\nIt'd croon every night\nIn the moon's soft light\nTill it burst into song with great glee",
    "There was a young man from the hill\nWho rode his bike with great skill\nHe'd race through the trees\nWith the greatest of ease\nAnd dodge all the cars with a thrill",
    "A girl from the land of green\nHad a cat who was quite serene\nIt would nap by the door\nOn the wooden floor\nAnd dream of a world unseen",
    "A boy from the town of West\nHad a parrot who loved to jest\nIt'd mimic and squawk\nAnd then take a walk\nTill it flew away with the best",
    "There was a young lad named Dale\nWhose shoes left behind a big trail\nHe ran through the woods\nAnd ate chocolate foods\nUntil he got stuck in a whale",
    "A woman from faraway lands\nHad a basket that held all her plans\nShe'd fill it with dreams\nAnd glittering beams\nAnd visit the shore with her hands",
    "There was a man from the plains\nWhose shoes left behind colorful stains\nHe'd walk in the rain\nAnd feel no pain\nTill the stains filled up the lanes",
    "A dog from the town of June\nLoved to sing a wild tune\nIt howled in the night\nWith all of its might\nAnd danced under the glowing moon",
    "A girl with a doll in her hand\nWould wander the green, endless land\nShe'd hum a soft song\nAnd skip along\nWhile holding her doll by the band",
    "There once was a bear from the woods\nWho lived in a house made of goods\nIt ate honey with glee\nAnd climbed every tree\nUntil it was stuck, misunderstood",
    "A sailor from the old shore\nHad a boat that could never ignore\nIt'd sail through the night\nWith the stars shining bright\nTill it found a new island to explore",
    "There was a man from the bay\nWho wore socks that were striped in a way\nHe danced every day\nIn the sun's warm rays\nUntil they turned purple and gray",
    "A frog from the lily pond\nLoved to leap and swim beyond\nIt'd hop in the rain\nWith no pain or strain\nTill it went to the farthest of ponds",
    "There was a young man named Pete\nWho loved to walk down the street\nHe'd smile at the sky\nAnd wave to pass by\nUntil his shoes got stuck in the heat",
    "A woman from a town so small\nWould answer each call with a ball\nShe'd toss it with grace\nIn a smiling embrace\nAnd laughed as it bounced down the hall",
    "There was a man from the hill\nWho would always be calm and still\nHe'd sip his sweet tea\nAnd feel so carefree\nTill the clouds gave him a chill",
    "A lady who loved the sun\nWould lay in the grass and have fun\nShe'd bask and she'd tan\nWith a book in her hand\nAnd hum to the beat of a drum",
    "A knight from the land of light\nWould challenge the darkness with might\nHe'd duel with a sword\nAnd keep his word\nTill he defeated the night",
    "There was a boy named Lee\nWho loved to swim in the sea\nHe'd dive and he'd splash\nIn a great big dash\nTill he floated away so free",
    "A man from the faraway East\nLoved to bake and feast on a feast\nHe'd cook with great flair\nAnd share it with care\nTill he made enough for the whole beast",
    "There was a young girl from the shore\nWho loved to explore and explore\nShe'd find hidden caves\nAnd surf on the waves\nWhile dreaming of things to adore",
    "A man from the town of Wood\nHad a hat that was mighty good\nHe'd wear it with pride\nOn every ride\nAnd say, 'Isn't life understood?'",
    "There was a young man named Hank\nWho loved to swim in a tank\nHe'd splash all around\nWithout making a sound\nTill the tank was completely sank",
    "A woman from the edge of the lake\nLoved to bake a big chocolate cake\nShe'd frost it with care\nAnd decorate with flair\nAnd give a slice to the snake",
    "A man from the town of Dan\nWould bake pies in a tin-can\nHe'd make them so sweet\nWith every treat\nUntil he baked a pie for the man",
    "There was a girl with a red bow\nWho loved to watch the wind blow\nShe'd spin in a circle\nWith no concern at all\nUntil the wind made her toe",
    "A woman from far in the north\nWould travel the earth with great worth\nShe'd climb every peak\nAnd swim through the creek\nUntil she found all she was worth",
    "A man from the hilltop high\nLoved to dance and to fly\nHe'd twirl with great care\nAnd leap in the air\nUntil he soared into the sky",
    "There once was a bird from the sea\nWho flew so fast, wild and free\nIt'd flap in the breeze\nAnd glide with such ease\nTill it landed on top of a tree",
    "A boy from the edge of the wood\nHad a frog that was quite good\nIt jumped all around\nAnd made not a sound\nTill it landed right in the food",
    "A girl from the shore of the lake\nLoved to eat a chocolate cake\nShe'd share with her friends\nTill the cake met its end\nAnd they went for a swim in the wake",
    "There was a man from the town of Kent\nWho loved to build houses so bent\nHe'd hammer and nail\nAnd never would fail\nTill his house became quite the event",
    "A lady from the edge of the sea\nHad a dress that was just meant to be\nShe'd twirl in delight\nUnder the soft moonlight\nUntil the dress flew away with glee",
    "A young man from the small town of Lee\nHad a cat that was lively and free\nIt'd pounce and then play\nAll through the day\nTill it fell into the old oak tree"
        "There once was a man from Peru\nWho had a pet kangaroo\nHe danced with a smile\nFor a mile and a while\nTill he fell in a vat of glue",
        "A woman from the hills of Troy\nHad a dog who loved to deploy\nHe'd bark and he'd bite\nFrom morning till night\nChasing rabbits for joy",
        "There was a young girl from the coast\nWhose friends were a ghost and a host\nThey laughed and they played\nIn the sunshine all day\nAnd ate cookies that were fresh and most",
        "There was an old man named Clyde\nWho rode on a very wide slide\nHe went down so fast\nHe flew past a blast\nAnd got stuck on the other side",
        "A boy from the small town of Greg\nLoved to walk on his right leg\nHe'd hop and he'd skip\nAnd do flips in the nip\nUntil he got stuck in a peg",
        "A lady named Sue from the north\nHad a pet mouse named forth\nThey'd climb up a tree\nAnd laugh in pure glee\nWhile they counted the rocks down below",
        "There once was a baker named Mark\nWho baked cakes that could leave a big spark\nHe frosted with cream\nUntil he did scream\nWhen he burned down his bakery dark",
        "There was a young man from the bay\nWho liked to paint pictures all day\nHe painted a cow\nAnd said, Wow! Wow!\nAnd sold it to a buyer from May",
        "A girl with a dress made of lace\nWas always the life of the place\nShe'd dance, she'd sing, and\nShe'd do her thing\nTill her shoes caught fire in the race",
        "There was an old lady from York\nWho loved to eat pickles and pork\nShe'd munch on a treat\nWhile tapping her feet\nAnd whistling a tune as she'd walk",
        # 50 New limericks
        "There once was a man from Peru\nWho loved eating soup with a shoe\nHe dipped it in broth\nWithout any froth\nAnd declared it the best he'd ever chew",
        "A woman from sunny Brazil\nHad a pet cat who would kill\nIt would leap and it pounce\nAnd run in a round\nUntil it fell into a dill",
        "A fellow from the town of Clyde\nTried to take a big fish for a ride\nIt slipped from his hand\nIn the shifting sand\nAnd escaped to the ocean wide",
        "A man from the city of Leeds\nHad a garden full of good seeds\nBut his plants grew too tall\nAnd soon they'd all fall\nAnd tumble down into his weeds",
        "A child with a kite in the air\nFlew it high without any care\nBut the wind blew it down\nAnd it landed with a frown\nIn a bowl of jam, thick and fair",
        "A dog from the land of Wales\nChased a cat down the trails\nIt ran through the dirt\nIn a tiny red shirt\nAnd tripped on the edge of some nails",
        "A fisherman from the bay\nCaught a big fish one fine day\nIt leapt in the air\nWith a splash and a glare\nThen slipped through his fingers away",
        "A knight from the castle in Spain\nHad a horse who loved to complain\nIt'd whinny and neigh\nAnd gallop away\nTill it got caught in the rain",
        "A girl with a bow in her hair\nHad a fox who would dance in the square\nIt'd twirl and it'd leap\nThen fall fast asleep\nAnd wake up without a care",
        "A man from the north of the sea\nHad a whale for a pet, you see\nIt'd spout out the spray\nAnd swim every day\nWhile the man sipped his sweet iced tea",
        # 50 More limericks
        "A monkey from the jungle so green\nLoved to eat bananas unseen\nHe'd swing from the trees\nWith the greatest of ease\nAnd eat them in places serene",
        "A giraffe with a long neck so tall\nWanted to see over the wall\nHe stood on his toes\nAnd struck a few poses\nAnd gave everyone a call",
        "A lady who lived on a boat\nLoved to sing songs and to float\nShe'd serenade whales\nWith sweet fruity tales\nAnd laugh at the songs that they wrote",
        "There was a young man named Jack\nWho ran through the snow with a pack\nHe slipped on the ice\nOnce or twice\nThen he laughed and went back on track",
        "A rabbit from the edge of the wood\nAte his dinner just as he should\nBut one day it rained\nAnd the carrots were drained\nNow the rabbit has just the mushrooms for food",
        # Continue adding more limericks here up to 50...
    ]
    return random.choice(limericks)

def generate_free_verse(lines):
    words = {
        'nouns': [
            "sky", "moon", "star", "river", "ocean", "mountain", "fire", "cloud", "wind", "sun", "tree", "leaf", 
            "earth", "snow", "dream", "whisper", "thoughts", "chill", "shadows", "flame", "awakening", "firefly", 
            "dust", "wish", "leaves", "melancholy", "light", "breeze", "forest", "depths", "heart", "whimsy", "echo", 
            "flower", "rain", "desire", "night", "storm", "sorrow", "tide", "horizon", "reflection", "hope", "journey", 
            "truth", "fate", "windstorm", "sunset", "dawn", "solitude", "thunder", "peace", "serenity", "whirlwind", 
            "moment", "echoes", "silent", "cliff", "island", "stormcloud", "seashell", "petal", "riverbank", "solitude", 
            "cosmos", "abyss", "island", "mystery", "wilderness", "adventure", "rainbow", "storm", "mist", "cliff", 
            "sea", "twilight", "tapestry", "tide", "canyon", "haze", "flurry", "cascade", "cavern", "void", "nightfall", 
            "echo", "reflection", "whisper", "sands", "mountain peak", "wisp", "twilight", "moonbeam", "oasis", 
            "thunderstorm", "illusion", "sunshine", "driftwood", "reverie", "serenity", "horizon", "ember", 
            "watershed", "palm", "boulder", "cobweb", "rift", "mountainside", "sunrise", "starlight", "dawn", 
            "desolation", "prayer", "tides", "windswept", "dreamscape", "volcano", "abyss", "whispers", "grove", "song"
        ],
        
        'verbs': [
            # Base Form
            "glimmer", "whisper", "tremble", "reverberate", "stir", "grasp", "ignite", "soar", "whirl", "twirl", 
            "collapse", "explode", "tumble", "crash", "vibrate", "expand", "shimmer", "whine", "pulsate", "reflect", 
            "sing", "echo", "burn", "flame", "drift", "rise", "unfold", "unravel", "flow", "glisten", "blink", 
            "recede", "jump", "pulse", "snap", "rip", "blaze", "shudder", "crumble", "rejoice", "expand", 
            "rush", "disappear", "swirl", "roar", "lurk", "wander", "crash", "weave", "tangle", "flutter", "rush", 
            "float", "glide", "glimmer", "drift", "whistle", "sweep", "perceive", "surge", "wade", "scintillate", 
            "tumble", "shiver", "blaze", "reflect", "scatter", "enlighten", "pierce", "evaporate", "shine", 
            "wilt", "dance", "fall", "ascend", "sink", "crackle", "surround", "envelop", "gather", "unwind", 
            "flare", "embrace", "press", "sink", "tangle", "encircle", "breathe", "magnify", "spread", "spark", 
            "clash", "pierce", "chime", "fade", "explode", "flicker", "leap", "stir", "swim", "twitch", 
            "wind", "unravel", "destroy", "scour", "plunge", 
            
            # Present Tense (Adding Present Simple, Progressive)
            "glimmers", "whispers", "trembles", "reverberates", "stirs", "grasps", "ignites", "soars", "whirls", 
            "twirls", "collapses", "explodes", "tumbles", "crashes", "vibrates", "expands", "shimmers", "whines", 
            "pulsates", "reflects", "sings", "echoes", "burns", "flames", "drifts", "rises", "unfolds", "unravels", 
            "flows", "glistens", "blinks", "recedes", "jumps", "pulses", "snaps", "rips", "blazes", "shudders", 
            "crumbles", "rejoices", "expands", "rushes", "disappears", "swirls", "roars", "lurks", "wanders", 
            "crashes", "weaves", "tangles", "flutters", "rushes", "floats", "glides", "glimmers", "drifts", 
            "whistles", "sweeps", "perceives", "surges", "wades", "scintillates", "tumbles", "shivers", "blazes", 
            "reflects", "scatters", "enlightens", "pierces", "evaporates", "shines", "wilts", "dances", "falls", 
            "ascends", "sinks", "crackles", "surrounds", "envelops", "gathers", "unwinds", "flares", "embraces", 
            "presses", "sinks", "tangles", "encircles", "breathes", "magnifies", "spreads", "sparks", "clashes", 
            "pierces", "chimes", "fades", "explodes", "flickers", "leaps", "stirs", "swims", "twitches", 
            "winds", "unravels", "destroys", "scours", "plunges",
            
            # Past Tense
            "glimmered", "whispered", "trembled", "reverberated", "stirred", "grasped", "ignited", "soared", 
            "whirled", "twirled", "collapsed", "exploded", "tumbled", "crashed", "vibrated", "expanded", 
            "shimmered", "whined", "pulsated", "reflected", "sang", "echoed", "burned", "flamed", "drifted", 
            "rose", "unfolded", "unraveled", "flowed", "glistened", "blinked", "receded", "jumped", "pulsed", 
            "snapped", "ripped", "blazed", "shuddered", "crumbled", "rejoiced", "expanded", "rushed", 
            "disappeared", "swirled", "roared", "lurked", "wandered", "crashed", "weaved", "tangled", "fluttered", 
            "rushed", "floated", "glided", "glimmered", "drifted", "whistled", "swept", "perceived", "surged", 
            "waded", "scintillated", "tumbled", "shivered", "blazed", "reflected", "scattered", "enlightened", 
            "pierced", "evaporated", "shined", "wilted", "danced", "fell", "ascended", "sank", "crackled", 
            "surrounded", "enveloped", "gathered", "unwound", "flared", "embraced", "pressed", "sank", 
            "tangled", "encircled", "breathed", "magnified", "spread", "sparked", "clashed", "pierced", "chimed", 
            "faded", "exploded", "flickered", "leaped", "stirred", "swam", "twitched", "wound", "unraveled", 
            "destroyed", "scoured", "plunged",
            
            # Future Tense
            "will glimmer", "will whisper", "will tremble", "will reverberate", "will stir", "will grasp", 
            "will ignite", "will soar", "will whirl", "will twirl", "will collapse", "will explode", "will tumble", 
            "will crash", "will vibrate", "will expand", "will shimmer", "will whine", "will pulsate", "will reflect", 
            "will sing", "will echo", "will burn", "will flame", "will drift", "will rise", "will unfold", 
            "will unravel", "will flow", "will glisten", "will blink", "will recede", "will jump", "will pulse", 
            "will snap", "will rip", "will blaze", "will shudder", "will crumble", "will rejoice", "will expand", 
            "will rush", "will disappear", "will swirl", "will roar", "will lurk", "will wander", "will crash", 
            "will weave", "will tangle", "will flutter", "will rush", "will float", "will glide", "will glimmer", 
            "will drift", "will whistle", "will sweep", "will perceive", "will surge", "will wade", "will scintillate", 
            "will tumble", "will shiver", "will blaze", "will reflect", "will scatter", "will enlighten", 
            "will pierce", "will evaporate", "will shine", "will wilt", "will dance", "will fall", "will ascend", 
            "will sink", "will crackle", "will surround", "will envelop", "will gather", "will unwind", "will flare", 
            "will embrace", "will press", "will sink", "will tangle", "will encircle", "will breathe", "will magnify", 
            "will spread", "will spark", "will clash", "will pierce", "will chime", "will fade", "will explode", 
            "will flicker", "will leap", "will stir", "will swim", "will twitch", "will wind", "will unravel", 
            "will destroy", "will scour", "will plunge",
            
            # Present Progressive
            "is glimmering", "is whispering", "is trembling", "is reverberating", "is stirring", "is grasping", 
            "is igniting", "is soaring", "is whirling", "is twirling", "is collapsing", "is exploding", "is tumbling", 
            "is crashing", "is vibrating", "is expanding", "is shimmering", "is whining", "is pulsating", "is reflecting", 
            "is singing", "is echoing", "is burning", "is flaming", "is drifting", "is rising", "is unfolding", 
            "is unraveling", "is flowing", "is glistening", "is blinking", "is receding", "is jumping", "is pulsing", 
            "is snapping", "is ripping", "is blazing", "is shuddering", "is crumbling", "is rejoicing", "is expanding", 
            "is rushing", "is disappearing", "is swirling", "is roaring", "is lurking", "is wandering", "is crashing", 
            "is weaving", "is tangling", "is fluttering", "is rushing", "is floating", "is gliding", "is glimmering", 
            "is drifting", "is whistling", "is sweeping", "is perceiving", "is surging", "is wading", "is scintillating", 
            "is tumbling", "is shivering", "is blazing", "is reflecting", "is scattering", "is enlightening", 
            "is piercing", "is evaporating", "is shining", "is wilting", "is dancing", "is falling", "is ascending", 
            "is sinking", "is crackling", "is surrounding", "is enveloping", "is gathering", "is unwinding", 
            "is flaring", "is embracing", "is pressing", "is sinking", "is tangling", "is encircling", "is breathing", 
            "is magnifying", "is spreading", "is sparking", "is clashing", "is piercing", "is chiming", "is fading", 
            "is exploding", "is flickering", "is leaping", "is stirring", "is swimming", "is twitching", 
            "is winding", "is unraveling", "is destroying", "is scouring", "is plunging"
        ],
        
        'adjectives': [
            "smooth", "vibrant", "gentle", "delicate", "wild", "fragrant", "bright", "eternal", "glowing", "majestic", 
            "calm", "frosted", "unbroken", "shimmering", "turbulent", "serene", "luminous", "silent", "brilliant", 
            "mystical", "crystal", "timeless", "invisible", "frozen", "vivid", "stirring", "blazing", "mournful", 
            "fragile", "unseen", "radiant", "twinkling", "soft", "clear", "undisturbed", "introspective", 
            "soulful", "vibrating", "colorful", "desolate", "permanent", "elusive", "everlasting", "fragile", 
            "sensitive", "infinite", "cosmic", "subtle", "dark", "serene", "restless", "nocturnal", "expansive", 
            "vivid", "elusive", "timeless", "unfurling", "sparse", "vibrating", "glistening", "shadowed", 
            "bright", "new", "invisible", "unheard", "frosty", "faint", "stark", "dreamy", "distant", "pale", 
            "ephemeral", "frenetic", "frantic", "frozen", "sacred", "glimmering", "radiant", "unbroken", "tender", 
            "boundless", "peaceful", "ancient", "lustrous", "dreamlike", "mystic", "suspended", "harsh", "sharp", 
            "solitary", "soothing", "fragile", "tender", "fiery", "calming", "volcanic", "shimmering", "smooth", 
            "clear", "quiet", "turbulent", "twinkling", "serene", "unspoken", "secretive", "whispering", 
            "feathered", "earthy", "radiant"
        ],
        
        'adverbs': [
            "gracefully", "gently", "delicately", "vividly", "serenely", "brightly", "boldly", "naturally", 
            "elegantly", "effortlessly", "subtly", "spiraling", "exuberantly", "tremulously", "vibrantly", "freely", 
            "elegantly", "steadily", "unseen", "smoothly", "suddenly", "whisperingly", "lazily", "sharply", "serenely", 
            "drifting", "reflectively", "exultantly", "faintly", "effortlessly", "mysteriously", "gently", 
            "suddenly", "aimlessly", "repeatedly", "whimsically", "tenderly", "transcendently", "ethereally", 
            "wildly", "mournfully", "reverently", "innocently", "clearly", "sharply", "timelessly", "languidly", 
            "imperceptibly", "restlessly", "gracefully", "precisely", "unobtrusively", "subconsciously", 
            "flowingly", "softly", "timidly", "glowingly", "barely", "swiftly", "uneasily", "impatiently", 
            "melodiously", "frantically", "ominously", "impressively", "indistinctly", "dreamily", "giddily", 
            "indifferently", "serenely", "distantly", "gracefully", "barely", "impatiently"
        ],

        'connectors': [
            "and", "but", "yet", "for", "nor", "so", "because", "though", "while", "since", "although", 
            "whereas", "despite", "except", "however", "therefore", "as", "until", "when", "if", "whether", 
            "in", "out", "without", "on", "off", "along", "through", "between", "around", "by", "above", "below", 
            "under", "over", "beneath", "beside", "besides", "across", "within", "beyond", "after", "before", 
            "upon", "next", "toward", "towards", "within", "without", "in case", "as though", "since", "as soon as", 
            "meanwhile", "even", "so that", "just as", "because of", "even if", "in spite of", "as long as", 
            "likewise", "in the meantime", "given that", "for instance", "similarly", "unless", "thus", "consequently"
        ]
    }

    used_words = set()

    def generate_line():
        noun1 = random.choice([word for word in words['nouns'] if word not in used_words]).capitalize()
        verb1 = random.choice([word for word in words['verbs'] if word not in used_words])
        adj1 = random.choice([word for word in words['adjectives'] if word not in used_words])
        adv1 = random.choice([word for word in words['adverbs'] if word not in used_words])
        noun2 = random.choice([word for word in words['nouns'] if word not in used_words])
        connector = random.choice(words['connectors'])

        used_words.update([noun1, verb1, adj1, adv1, noun2, connector])

        return f"{noun1} {verb1} {adv1} {connector} {adj1} {noun2}"

    poem = []
    for _ in range(lines):
        line = generate_line()
        poem.append(line)

    return "\n".join(poem)

if __name__ == '__main__':
    app.run(debug=True)
