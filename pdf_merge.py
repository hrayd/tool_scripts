# 将指定目录下的所有PDF文件合并成一个PDF文件
from pypdf import PdfWriter
import os
import glob

# 指定PDF文件所在目录
filePath = "/Users/ss/Desktop"
# 指定输出PDF文件
output = "./output/merged-pdf.pdf"

def find_pdf_files(directory):  
    # 初始化一个空列表来存储找到的文件路径  
    pdf_files = []  
  
    # 遍历目录及其子目录  
    for root, dirs, files in os.walk(directory):  
        # 使用glob模块匹配PDF文件  
        for file in glob.glob(os.path.join(root, '*.pdf')):  
            pdf_files.append(file)  
  
    pdf_files.sort()
    return pdf_files  

def main():
    inputFiles = find_pdf_files(filePath)
    merger = PdfWriter()
    for pdf in inputFiles:
        merger.append(pdf)
    merger.write(output)
    merger.close()

main()
