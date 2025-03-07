from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    oniichan_gifs = [
        # "https://media1.tenor.com/m/SzXHVmUledQAAAAd/doncheadlegoon-doncheadle.gif",
        "https://media1.tenor.com/m/gWuRQdhjSOYAAAAd/onii-chan-sigma.gif",
        # "https://media1.tenor.com/m/a4w9orEq9xYAAAAC/onii-chan.gif",
        # "https://media1.tenor.com/m/paqt70OGZCEAAAAd/oni-chan-memes-fatguyonichan.gif",
    ]

    if lowered == "":
        return 'Ight good talk'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'bitch' in lowered:
        return 'What the fuck did you just say to me? You little Bitch? I\'ll have you know ...'
    elif 'test' in lowered:
        return 'testing'
    elif 'roll spellcheck' in lowered:
        return 'You rolled spellcheck'
    elif 'oniichan' in lowered or 'onii chan' in lowered:
        return choice(oniichan_gifs)
    else:
        return