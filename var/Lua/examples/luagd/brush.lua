require "gd"

im = gd.createTrueColor(400, 400)
assert(im)

black = im:colorAllocate(0, 0, 0)
white = im:colorAllocate(255, 255, 255)

brush = gd.createFromPng("paper.png")
im:setBrush(brush)
im:line(60, 60, 70, 70, gd.BRUSHED)
im:line(120, 120, 130, 130, gd.BRUSHED)
im:line(180, 180, 190, 190, gd.BRUSHED)
im:line(240, 240, 250, 250, gd.BRUSHED)
im:line(300, 300, 310, 310, gd.BRUSHED)

im:png("out.png")
os.execute("out.png")
