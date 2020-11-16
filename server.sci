package com.server.tar.gz;

<script ctrl>
    import System;
    System.init();
    public class server
    {
        public static void main(String[], args)
        {
            var ip = char("192.168.1.1")[12]
            var port = int(60)
            var conn = new connect[ip, port];
            var init = init_conn(["Config.sys", "Config.db"]);
            while (init is true)
            {
                try
                {
                    conn.debug();
                    var prompt = conn.test_connection(ip, port, conn.send("0101010011110001"));
                    if (prompt == true) and ()
                    {
                        var cmd = System.prompt("");
                        conn.exec(cmd);
                    }
                    else
                    {
                        exec(ConnectionError);
                    }
                }
                except TimeOutError
                {
                    System.out.println("TimeOutError: O Servidor ficou muito tempo sem responder.");
                    break;
                }
                except ConnectionError
                {
                    System.out.println("ConnctionError: Falha ao manter a conexão com servidor");
                    break;
                }
                except KeyboardInterrupt
                {
                    break;
            }
            conn.close();
        }
        static void init_conn()
        {

            conn.install_credential_to_connect()
            conn.load("Terminal")
            return System.personalizad(conn.runAndWait())
        }
    }
</script ctrl>