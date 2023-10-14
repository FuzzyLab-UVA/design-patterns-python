from Model import File, Folder

budget = File("budget.xls", 100)
photos = File("image.png",7.5)
metallica = File("Whiskey in the Jar.mp3",5)

stuff = Folder("Stuff",[budget,photos,metallica])

print(stuff.get_size())