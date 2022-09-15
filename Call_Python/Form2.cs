using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace Call_Python
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\tkinter_scraping\tkinter_scraping.py";
            Process.Start(pInfo);

        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\pyramid_calc\pyramid_calc.py";
            Process.Start(pInfo);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_Python\list_text_disp\list_text_disp.py";
            Process.Start(pInfo);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\web_search\web_search.py";
            Process.Start(pInfo);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            ProcessStartInfo pInfo = new ProcessStartInfo();
            pInfo.FileName = "python";
            pInfo.Arguments = @"C:\github\Call_python\pdf_to_text\pdf_to_text.py";
            Process.Start(pInfo);

        }
    }
}
