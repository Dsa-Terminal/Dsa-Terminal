Lua-GD, the gd bindings for the Lua Programming Language
(c) 2004-06 Alexandre Erwin Ittner <aittner@netuno.com.br>

These are the Windows binaries for Lua-GD for Lua 5.1, compiled with
mingw32 3.4.4. These binaries also work with LuaJit 1.1.0. GD and its
dependencies were included in the distribution package for convenience.

Please refer to 'README' For non-win32 specific information.


+ Licensing

Each library has its own license. Please carefully read the following files:

    gd-license.txt
    libfreetype-license.txt
    libjpeg-license.txt
    libpng-license.txt
    zlib-license.txt


+ Instalation

There is no automatic installation procedure for Windows. You must copy the
following DLLs to somewhere in your system path:

    freetype6.dll
    jpeg62.dll
    libgd2.dll
    libiconv2.dll
    libpng13.dll
    xpm4.dll
    zlib1.dll

and, finally, copy the file "gd.dll" to your Lua binary package directory.


+ URLs

Lua-GD: http://lua-gd.luaforge.net/
Lua binaries: http://luabinaries.luaforge.net/
GD binaries: http://gnuwin32.sourceforge.net/packages/gd.htm

