require "gd"

im = gd.createPalette(120, 120)
assert(im)

black = im:colorAllocate(0, 0, 0)
blue = {}
for i = 1, 20 do
  blue[i] = im:colorAllocate(0, 0, 120+6*i)
end

fp = io.open("out.gif", "w")
assert(fp, "Failed to open file for writting")

fp:write(im:gifAnimBeginStr(true, 0))

for i = 1, 20 do
  tim = gd.createPalette(120, 120)
  tim:paletteCopy(im)
  tim:arc(60, 60, 6*i, 6*i, 0, 360, blue[21-i])
  fp:write(tim:gifAnimAddStr(false, 0, 0, 5, gd.DISPOSAL_NONE))
end

fp:write(gd.gifAnimEndStr())
fp:close()

print("Gif animation written to file 'out.gif'.")
