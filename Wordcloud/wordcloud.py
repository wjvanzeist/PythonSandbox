# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:54:04 2019

@author: vzeist
"""
import os
import wordcloud

import PyPDF4
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open('Matthijs.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(40)
# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())
