<script ctrl>
    import System;
    System.init();
    class firmware
    {
        static void __init__(start, String[])
        {
            var pkg = System.openAndRead("packge.json")
            while true
            {
                var cmd = System.prompt("Code:\> ")
                if (cmd == new System(pkg))
                {
                    var result = new System(pkg)
                }
                if (cmd == 'exit')
                {
                    break
                }
                else
                {
                    System.echo(cmd, ": Informação não encontrada!")
                }
            }
            return System.efectued()
        }
    }
</script ctrl>