# -*- coding: utf-8 -*-
'''
Created on 14 de Abr de 2013

@author: admin1
'''
from fpdf import FPDF
from xlwt import Workbook
from xlwt.Formatting import Borders
import xlwt
from lxml.html.builder import TITLE


########################################################################
class PDF(FPDF):
   
    def setTitle(self, title):
        
        self.title = title
       
        pass
    
    def header(self,):
        # Logo
        #self.image('/home/admin1/Mestrado/2Trimestre/LPD/TrabalhoPratico/logo_estig.png',10,8,33)
        # Arial bold 15
        self.set_font('Arial','B',15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(len(self.title) * 3,10, self.title ,1,0,'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial','I',8)
        # Page number
        self.cell(0,10,'Pagina '+str(self.page_no()),0,0,'C')
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    pdf=PDF()
    pdf.setTitle("ola")
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times','',12)
    for i in range(1,41):
            pdf.cell(0,10,'Printing line number '+str(i),0,1)
    pdf.output('tuto2.pdf','F')

#if __name__ == '__main__':
#    ExportData()            