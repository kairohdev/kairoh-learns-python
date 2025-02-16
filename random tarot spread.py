# Produces a random single card tarot spread.
import random
tarot = { 
    1:	{
        'name': 'The Magician',
        'about': 'The Magician symbolizes manifestation and personal power, reminding you that you have all the tools you need to create your desired reality. It calls for confidence in your abilities to transform ideas into action.',
    },
    2: {
        'name': 'The High Priestess',
        'about': 'The High Priestess represents intuition, mystery, and hidden knowledge, urging you to trust your inner voice and the secrets beneath the surface. She embodies a connection to the subconscious and spiritual wisdom.',
    },
    3: {
        'name': 'The Empress',
        'about': 'The Empress is a symbol of fertility, abundance, and nurturing energy, celebrating creativity, growth, and the beauty of nature. She encourages you to embrace your nurturing side and foster a sense of care and comfort.',
    },
    4: {
        'name': 'The Emperor',
        'about': 'The Emperor embodies authority, structure, and control, encouraging a disciplined approach to life\'s challenges. He represents leadership, stability, and the need to set boundaries and maintain order.',
    },
    5: {
        'name': 'The Hierophant',
        'about': 'The Hierophant stands for tradition, spirituality, and conformity, guiding you toward established systems of wisdom and belief. He often points to mentorship or the pursuit of higher knowledge through conventional paths.',
    },
    6: {
        'name': 'The Lovers',
        'about': 'The Lovers card represents deep connections, partnerships, and choices that shape your path. It highlights the importance of balance and alignment in relationships, emphasizing harmony and mutual understanding.',
    },    
}

spread = {}

cardNum = random.randint(1,7)

def tarotSpread(cardNum):
    spread["first"] = tarot.pop(cardNum)
    for card, cardDetails in spread.items():
        return "For your single card spread, you got the {} card. About this card: {}".format(cardDetails['name'], cardDetails['about'])

print(tarotSpread(cardNum))



