using System;
using System.IO;

namespace DefaultUser
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Username: " + Environment.UserName);

            string newContent = Environment.UserName;

            System.IO.StreamWriter file = new System.IO.StreamWriter(@"user.txt");
            file.WriteLine(newContent);
            Console.ReadLine();
        }
    }
}
