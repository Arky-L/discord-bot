from random import choice, randint
import random


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    oniichan_gifs = [
        # "https://media1.tenor.com/m/SzXHVmUledQAAAAd/doncheadlegoon-doncheadle.gif",
        "https://media1.tenor.com/m/gWuRQdhjSOYAAAAd/onii-chan-sigma.gif",
        # "https://media1.tenor.com/m/a4w9orEq9xYAAAAC/onii-chan.gif",
        # "https://media1.tenor.com/m/paqt70OGZCEAAAAd/oni-chan-memes-fatguyonichan.gif",
    ]

    babyVance_gifs = [
        "https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25d56fff-096b-4f24-a996-149cc73e9cf6_1055x1212.jpeg",
        "https://imageio.forbes.com/specials-images/imageserve/67ccc6e98666efd88c20fae0/JD-Vance-edited-into-an-iconic-image-of-Kim-Kardashian/0x0.jpg?format=jpg&width=1440",
        "https://pbs.twimg.com/media/GY4wlQKWwAAg7kQ?format=jpg&name=900x900",
        "https://pbs.twimg.com/media/GlZ_stLWAAAkVlK?format=jpg&name=medium",
        "https://pbs.twimg.com/media/GlXRgZDXMAAxiYH?format=jpg&name=900x900",
        "https://pbs.twimg.com/media/Gk7FVThX0AET7nH?format=jpg&name=large",
        "https://pbs.twimg.com/media/GlIM7QJWsAAssea?format=jpg&name=medium",
        "https://pbs.twimg.com/media/Glh7OfEXIAAzD0o?format=jpg&name=medium",
        "https://gizmodo.com/app/uploads/2025/03/Gross-896x558.jpg",
        "https://gizmodo.com/app/uploads/2025/03/McNuggetVance-879x1024.jpg",
        "https://gizmodo.com/app/uploads/2025/03/ToysVance.jpg",
        "https://pbs.twimg.com/media/GlJ1vHwWcAAr3ul?format=jpg&name=900x900",
        "https://pbs.twimg.com/media/GlKeJscXYAAFwG7?format=jpg&name=large",
        "https://i.imgur.com/RNikrFg.jpeg",
        "https://i.imgur.com/KXkZVuk.jpeg",
        "https://i.imgur.com/m7HTUz5.jpeg",
        "https://pbs.twimg.com/media/GlhZcqdXIAAqMev?format=jpg&name=large",
        "https://pbs.twimg.com/media/GlhZcqfXgAE6jlo?format=jpg&name=large",
        "https://gizmodo.com/app/uploads/2025/03/TrueSelf.jpg",
        "https://images.spot.im/image/upload/v200/280171e0-94ad-46fe-ac23-6393618013c9.jpg",
    ]

    weights = [5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    if lowered == "":
        return 'Ight good talk'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'roll spellcheck' in lowered:
        return 'You rolled spellcheck'
    elif 'oniichan' in lowered or 'onii chan' in lowered:
        return choice(oniichan_gifs)
    elif 'baby vance' in lowered:
        return random.choices(babyVance_gifs, weights=weights, k=1)[0]
    else:
        return