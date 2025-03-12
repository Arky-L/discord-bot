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
        "https://bigmemes123.funnyjunk.com/comments/Patriotswin+is+nothing+but+vance+ancient+memes+this+week+_b291c0f03acbe754a5dcc41318d45864.jpg",
        "https://bigmemes123.funnyjunk.com/comments/+_fbad4e435e405d6697bf3b6d2a81a4f3.png",
        "https://bigmemes123.funnyjunk.com/comments/+_d7074043aecc5436c7fbd59040ce2ef9.jpg",
        "https://bigmemes123.funnyjunk.com/comments/+_a761c493e4ff4e9b633a6af094d22b26.png",
        "https://bigmemes123.funnyjunk.com/comments/Trying+to+explain+this+to+a+middle+aged+female+democrat+_090e94a06b6405ac1d2c834fb2e09287.jpg",
        "https://loginportal123.funnyjunk.com/comments/Its+almost+as+if+none+of+these+guys+have+never+_87b84a03933faf3233e510253e7f7d52.jpg",
        "https://bigmemes123.funnyjunk.com/comments/Im+glad+these+are+a+thing+some+on+the+right+_9cce150b97521372aab912d861065b96.png",
        "https://bigmemes123.funnyjunk.com/comments/Idk+these+people+are+so+hardwired+to+slander+the+people+_dd43ec416a2b31543706564ba7c64340.jpg",
        "https://bigmemes123.funnyjunk.com/comments/Trying+to+explain+this+to+a+middle+aged+female+democrat+_090e94a06b6405ac1d2c834fb2e09287.jpg",
        "https://bigmemes123.funnyjunk.com/comments/+_62102565a37a013ed13281870d4906e7.png",
        "https://loginportal123.funnyjunk.com/comments/+_ac213e9c96ba0b693e872b2c0511c76c.jpg",
        "https://loginportal123.funnyjunk.com/comments/+_88d8d9ddb8ae273192d6937d868128bf.png",
        "https://bigmemes123.funnyjunk.com/comments/+_62929d17a5026d3e12337e6a7289b75f.jpg",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349221526779596862/Glt_n64bIAAz3LV.jpg?ex=67d24ff7&is=67d0fe77&hm=f0737ddcb9540087a7333950fcd261b27a62338f6da35688fc916a3ceebcc9fa&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349221527010410577/Glt_n63b0AEuzET.jpg?ex=67d24ff7&is=67d0fe77&hm=e9cca9ca5e934a9b2ec5b5f89f62cd0bebb87069983b7478ae894f9bf90d833b&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349221767763198024/Glu0hwWWYAAC8JU.jpg?ex=67d25030&is=67d0feb0&hm=4669e2ec3e59fde143c977bfe73f6a0c9173ccb2c1b207c9b1f809c628a7786d&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349221846117253241/GlwVTLSbAAA7mvU.jpg?ex=67d25043&is=67d0fec3&hm=f0f33f33cd09f68c319eab1e63cf47c3e39e29ccf82d3498120fe34cff9bd86f&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349221992749858877/GluGA6KWkAAGs7b.jpg?ex=67d25066&is=67d0fee6&hm=e0f9cef3ec032b4f5c2c42395f7ed29323cfffa76a240ef1122a239cdb98b136&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349222077256695838/GlxTJnnXIAArsDJ.jpg?ex=67d2507a&is=67d0fefa&hm=32fa553ad013b1168a79427b4fbb283e57ebfc557713a7aafd015caad8f7dba8&",
        "https://media.discordapp.net/attachments/112057524093452288/1349222122505113663/Glug3ZEbwAAGoBf.jpg?ex=67d25085&is=67d0ff05&hm=832ce17935a6211730623bea25d6cb4214497e9bad966d1b781aa5c214b2d254&=&format=webp&width=611&height=850",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349216865158959186/GlQRnrUWAAAX97i.jpg?ex=67d24b9f&is=67d0fa1f&hm=4aaeb8d05d8190ac7b7bbd1bc7e21352781e50a7cf2355e9a902105245454b5c&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349216936889684031/GlQR1paXQAAQH-O.jpg?ex=67d24bb0&is=67d0fa30&hm=d6f259e1ff4f794a75341286874a7fd28ad8343853d12690647191468f67e679&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349216986369888318/GlQR7Q_WIAA0k-h.jpg?ex=67d24bbc&is=67d0fa3c&hm=ce1198406536fdf9424d1092abc065178b4f7a34f8102c6c323e5f7c42e31fd9&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217011636506685/GlQR_x4WUAAvH-v.jpg?ex=67d24bc2&is=67d0fa42&hm=9909f37ef524c08329b003d352d446508e10af24b2a09da134d0ee94477e4b3d&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217058054864976/GlQSUNGXwAAr4cp.jpg?ex=67d24bcd&is=67d0fa4d&hm=f48d7a680e04379290bd0e375d32e26eaa5b8a8b720c76fcd76c2d286f7dc7ed&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217116481392712/GlQX2Fma4AEo4br.jpg?ex=67d24bdb&is=67d0fa5b&hm=36e5744d428c865bffe23fc22d89f3815a61333bb9a23cc17d2e3fb49e4f2ae8&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217116250833007/GlQdAw-XMAA55iA.png?ex=67d24bdb&is=67d0fa5b&hm=cf8b495bb9a5d0c3ea4e510bc2504af5f1a64aed9d28360913bfe4f0bc68d79e&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217116040986695/GlTMdC-WYAAkcz0.jpg?ex=67d24bdb&is=67d0fa5b&hm=6a479db6059d771ea8faa17386f72e0ddf9f646d95de89835292cdd879b27f13&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217136207462412/GlVLV7FasAAJbJZ.png?ex=67d24be0&is=67d0fa60&hm=5e04d52d3300f189f8c4991a753aa2d5ec5df86ea3baf26a77d65f5707443760&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217226762358856/GlQVIEyakAAodTO.jpg?ex=67d24bf6&is=67d0fa76&hm=30d28a72eabe0e47e5f5c1fe21ddfa961f6b1152315021b0291f987fa18ffc5c&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217310593777776/GlQh3W_a4AMHKj9.jpg?ex=67d24c0a&is=67d0fa8a&hm=e8388addf852b36951d881250dfa418c42747636b10d40bb783a77ef8701f21b&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217434808352949/GlQR8CCXkAA37Uw.jpg?ex=67d24c27&is=67d0faa7&hm=6f87af2c5441d9a6da95f71c8545f959d0b99eac135e36aba9a37cd653def5d8&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217435433304174/GlU-ZWxWcAECW2Z.jpg?ex=67d24c27&is=67d0faa7&hm=bdf6591d8f658a9796ad1cb6fb12e251ec1468b514fa35e82fbdd2b621da3376&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217435114405992/GlQ5hAcXoAAUTUG.png?ex=67d24c27&is=67d0faa7&hm=21b93f41e48418a4bb98964469e356295a1b920b0c87732d5733e9022b42e172&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217634666938389/GlS1ZN_WkAARdNm.jpg?ex=67d24c57&is=67d0fad7&hm=bb9e12c3456f131cfc19aab42e23f56cf11c99b9540d1677028ded63bf9b934e&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217723393114264/GlVdlHkWYAA5E0t.jpg?ex=67d24c6c&is=67d0faec&hm=1e8ff01f80f1ed3cdd481bafad9a22e380c9afdc656ff07f9bf69a002964bde6&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217738874294322/GldYXL6bwAAJfgD.jpg?ex=67d24c70&is=67d0faf0&hm=ede2a3412b235587e6bceca210906c49469607fdb5c5487ad36757a562531a41&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217854884675655/GlVRIeMXcAAvt7u.jpg?ex=67d24c8b&is=67d0fb0b&hm=dd2247e1063c0f40b3f2e67a5535c7383940e630212d1231280c05c52ad1ecd4&",
        "https://cdn.discordapp.com/attachments/112057524093452288/1349217855349981246/GlVTn9cWcAAwvjX.jpg?ex=67d24c8b&is=67d0fb0b&hm=ec19531bf570d73f440e3af4349b4a6c26a8b63e431612317e6bb2118a2b4c04&",
        "https://media.discordapp.net/attachments/112057524093452288/1349218005044690954/GlVTakCXwAAv0Hr.jpg?ex=67d24caf&is=67d0fb2f&hm=6c76b27c22b06339c9d6e035e279b1f8e028b394be11926ab1208b8beeec7747&=&format=webp&width=850&height=481",
    ]

    weights = [5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

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
    elif 'ball cancer check' in lowered:
        return "Yes, they have testicular cancer" if random.random() < 0.5 else "No, they do not have testicular cancer"
    else:
        return