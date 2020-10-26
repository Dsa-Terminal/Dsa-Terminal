<script ctrl>
    import System;
    System.init()
    class sample
    {
        var sample_file = System.openAndRead("sample.query")
        while true
        {
            var sample_line = System.prompt("SampleLine:\>_")
            if (sample_file == sample_line)
            {
                System.echo("Sample require filed check!")
                break
            }
            else
            {
                continue
            }
            return System.efected()
        }
    }
</script ctrl>