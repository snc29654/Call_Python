using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace Call_Python
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\MP4_play\MP4_play.py";
            Process.Start(pInfo);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\list_jpg_disp\list_jpg_disp.py";
            Process.Start(pInfo);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\select_jpg_disp\select_jpg_disp.py";
            Process.Start(pInfo);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\tkinter_memo\tkinter_memo.py";
            Process.Start(pInfo);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\button_jpg_folder\button_jpg_folder.py";
            Process.Start(pInfo);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\kenban\kenban.py";
            Process.Start(pInfo);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\janken\janken.py";
            Process.Start(pInfo);

        }

        private void button8_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\jpg_list_rgb\jpg_list_rgb.py";
            Process.Start(pInfo);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\diary_memo\diary_memo.py";
            Process.Start(pInfo);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\large_and_small\large_and_small.py";
            Process.Start(pInfo);

        }
    }
}
