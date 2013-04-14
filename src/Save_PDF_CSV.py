# -*- coding: utf-8 -*-
'''
Created on 14 de Abr de 2013

@author: admin1
'''
from fpdf import FPDF
from xlwt import Workbook
from xlwt.Formatting import Borders
import xlwt


class ExportData(object):
    def __init__(self):
        wb = Workbook()
        self.createXLS(wb)
        wb.save('saida.xls')
        pass
        
    def createXLS(self, wb):
        #Nome Folha
        ws0 = wb.add_sheet('Folha')
    
        #Estilos
        style = xlwt.easyxf('pattern: pattern solid, fore_colour green')
        borders = Borders()
        borders.left    = 5
        borders.right   = 5
        borders.top     = 5
        borders.bottom  = 5
        style.borders = borders
        
        listaCAB = ["Teste", "Teste1"]
        
        #Cabeçalhos do XLS
        col = 0
        row = 0
        for lCab in listaCAB:
            ws0.write(row, col, lCab, style)
            col += 1
        
        lista = []
        
        for a in range(0, 10):
            lista.append([a, 0, 0])
            
        row = 1
        col = 0
       
        for linha in lista:
            for l in linha:
                ws0.write(row, col, l)
                col += 1
            col = 0
            row += 1
            pass
        pass
    
    def createPDF(self):
        pass

 
########################################################################
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('/home/admin1/Mestrado/2Trimestre/LPD/TrabalhoPratico/logo_estig.png',10,8,33)
        # Arial bold 15
        self.set_font('Arial','B',15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30,10,'Title',1,0,'C')
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
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times','',12)
    for i in range(1,41):
            pdf.cell(0,10,'Printing line number '+str(i),0,1)
    pdf.output('tuto2.pdf','F')

#if __name__ == '__main__':
#    ExportData()            