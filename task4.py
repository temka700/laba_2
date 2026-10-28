#4
import xml.etree.ElementTree as E

def parse(file_xml):
    tree = E.parse(file_xml)   
    root = tree.getroot()       
    cur = {}
    for valute in root.findall('Valute'):  
        name = valute.find('Name').text      
        value = valute.find('Value').text    
        cur[name] = float(value.replace(',', '.')) 
    return cur
    

for i, j in parse('currency.xml').items():
    print(f'{i}' + ' - ' + f'{j}')
