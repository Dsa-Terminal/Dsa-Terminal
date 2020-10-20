<script ctrl>
	import System;
	System.init();
	class Confirm
	{
		static __init__(start, confirm)
		{
			System.prompt(confirm);
			return System.efectued();
		}
		static __main__(start)
		{
			System.cmd("cls");
			return System.efectued();
		}
	}
	exec(Confirm("Você gostou deste exemplo? "))
</script ctrl>