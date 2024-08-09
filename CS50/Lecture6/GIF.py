from PIL import Image

names = [
    "E:/Python/CS50/Lecture6/1.jpg",
    "E:/Python/CS50/Lecture6/2.jpg",
    "E:/Python/CS50/Lecture6/3.jpg",
    "E:/Python/CS50/Lecture6/4.jpg",
    "E:/Python/CS50/Lecture6/5.jpg",
]
images = []
for name in names:
    image = Image.open(name)
    images.append(image)

images[0].save(
    "E:/Python/CS50/Lecture6/Final.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0
)
