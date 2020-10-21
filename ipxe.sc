/*
Console de opereções loteadas do Dsa Terminal v1.0.9
Disponivel no Github.com (https://github.com/Dsa-Terminal/Dsa-Terminal)
License: Mit | Copyright (c) 2020
*/
<script ctrl>
	import System;
	System.init();
	class ipxe
	{
		static void __init__(start, String[])
		{
			System.cmd("cls")
			System.suspendConsole()
			System.wait(1)
			while true
			{
				var cmd = System.prompt("Code:\>_")
				if (cmd == 'start')
				{
					System.terminal()
					return System.efectued()
				}
				if (cmd == 'exit'):
					System.close()
					return System.personalized(System.close())
				else
				{
					continue
				}
			}
		}
		static void __main__(start, System)
		{
			var a = new __init__("./Terminal.exe" "")
			while true
			{
				var b = System.efectued()
				if (a == b)
				{
					return System.efectued()
					break
				}
				else
				{
					return System.personalized(false)
					break
				}
			}
		}
	}
	exec(ipxe("", './Terminal.exe'))
</script ctrl> 