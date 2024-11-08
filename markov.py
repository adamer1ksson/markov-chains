import random
import pprint 
pp = pprint.PrettyPrinter(indent=4)

ORDER = 3 
TEXT = """On a brisk autumn morning in New York, Ava stepped out of her apartment, inhaling the crisp air that carried hints of roasted coffee and warm bagels from a nearby cart. The city buzzed around her with its familiar rhythm: a mix of clattering footsteps, honking taxis, and faint strains of jazz drifting from a busker’s saxophone in the subway. Ava was headed to the park, her favorite escape from Manhattan’s concrete maze. She joined the rush of people, crossing streets with purposeful strides, each person wrapped up in their own world. As she reached Central Park, the towering buildings faded into the background, replaced by vibrant leaves that seemed to glow in the morning light. She found her usual bench near the pond, where ducks paddled lazily, oblivious to the city’s constant motion. She took out a sketchbook and began drawing, letting her pencil capture the morning scenes: a young couple laughing by the water, an elderly man feeding the birds, a child chasing after a golden retriever. New York was endless stories woven together, and she felt lucky to be a part of it, even if just as an observer. Ava sketched until the sun climbed higher, casting a warmer glow. The park was filling up now with joggers, picnickers, and families. As she packed up her things, she caught the eye of a street artist nearby, who gave her a nod and a smile. They didn’t need to exchange words; they both understood the magic of finding beauty in small moments. The day wore on, and Ava wandered through the city, exploring little shops, stumbling upon a street fair, and enjoying a slice of pizza at a tiny corner place she’d never noticed before. As the sun set, the city lights blinked on one by one, painting the streets in a golden hue. She lingered on a street corner, looking out at the skyline, with the Empire State Building glowing against the deep blue sky.In New York, no day was the same as the last, she thought with a smile."""

def markovGen(start: str, model: dict, size: int):
    res = start
    for i in range(size):
        if res[-ORDER-1:-1] in model:
            rand = random.randint(0, len(model[res[-ORDER-1:-1]]) -1) 
            res += model[res[-ORDER-1:-1]][rand]
        else:
            break
    return res 
     
def main():
    tokens = {}
    text = ""
    with open("./text.txt", "r",encoding="utf8") as handle:
        for line in handle:
            text += line.lower()
    length = len(text)
    for i in range(length-ORDER):
        token = text[i:i+ORDER]
        if token not in tokens:
            tokens[token] = [text[i+ORDER]] 
        tokens[token].append(text[i+ORDER])
    #pp.pprint(tokens)
    print(len(text[53:53 +ORDER]))
    for i in range(20):
        print(markovGen(text[53:53 +ORDER], tokens, 100))




if __name__ =="__main__":
    main()
