Lua-GD, the gd bindings for the Lua Programming Language
(c) 2004-06 Alexandre Erwin Ittner <aittner@netuno.com.br>


+ Introduction

"gd" is a C graphics library created by Thomas Boutell that allows your
code to quickly draw complete images with lines, polygons, arcs, text,
multiple colors, cut and paste from other images, flood fills, read in
or write out images in the PNG, JPEG or GIF format. This is particularly
useful in World Wide Web applications, where PNG and JPEG are two of the
formats accepted for inline images by most browsers. gd does not provide
for every possible desirable graphics operation. It is not necessary or
desirable for gd to become a kitchen-sink graphics package, but it does
include most frequently requested features, including both truecolor
and palette images, resampling (smooth resizing of truecolor images)
and so forth. You can get more information about gd from it's homepage.

Lua-GD is a "binding": a library that exports gd functions to the Lua
Programming Language, allowing you to use gd from Lua. The API was
NOT literally exported, but changed in a way that make it familiar to
Lua users.

Lua-GD is a programming library, not a paint program. If you are looking
for that or are not familiar to the Lua Programming Language, you are
in the wrong place.


+ Documentation

See doc/index.html for installation instructions and API documentation.


+ License

Lua-GD is copyrighted free software, distributed under the MIT license
(the same used by Lua 5.1) and it can be used at no cost for both academic
and commercial purpouses. Or, more precisely:

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHOR OR COPYRIGHT HOLDER BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

If you use this package in a product, an acknowledgment in the product
documentation would be greatly appreciated (but it is not required).
