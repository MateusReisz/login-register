import os
import xml.etree.ElementTree as Et
from datetime import date


class XmlReader():
    def __init__(self, directory) -> None:
        self.directory = directory
    

    def all_files(self):
        """
    Retorna uma lista de caminhos completos para todos os arquivos XML no diretório especificado.

    Returns:
        list: Uma lista contendo os caminhos completos para os arquivos XML no diretório especificado.

    Example:
        Se o diretório self.directory contiver os seguintes arquivos:
        - 'arquivo1.xml'
        - 'arquivo2.xml'
        - 'texto.txt'

        A chamada da função all_files() irá retornar:
        ['caminho/completo/arquivo1.xml', 'caminho/completo/arquivo2.xml']
    """
        return [ os.path.join(self.directory, file) for file 
                in os.listdir(self.directory) if file.lower().endswith('.xml')]
    

    def nfe_data(self, xml):
        root = Et.parse(xml).getroot()
        nsNfe = {"ns": "http://www.portalfiscal.inf.br/nfe"}

        #DADOS DA NFE
        nfe = self.check_none(root.find(
            './ns:NFe/ns:infNFe/ns:ide/ns:nNF', nsNfe))
        serial = self.check_none(root.find(
            "./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNfe))
        date_issue = self.check_none(root.find(
            './ns:NFe/ns:infNFe/ns:ide/ns:dhEmi',nsNfe))
        date_issue = f'{date_issue[8:10]}/{date_issue[5:7]}/{date_issue[:4]}'
        
        # DADOS EMITENTES
        key = self.check_none(root.find(
            './ns:protNFe/ns:infProt/ns:chNFe', nsNfe))
        cnpj_issuer = self.check_none(root.find(
            './ns:NFe/ns:infNFe/ns:emit/ns:CNPJ', nsNfe))
        name_issuer = self.check_none(root.find(
            './ns:NFe/ns:infNFe/ns:emit/ns:xNome', nsNfe))
        
        cnpj_issuer = self.format_cnpj(cnpj_issuer)
        value_nfe = self.check_none(root.find(
            './ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF', nsNfe))
        date_import = date.today()
        date_import = date_import.strftime('%d/%m/%Y')
        date_output = ''
        user = ''

        item_note = 1
        notes = []
        for item in root.findall('./ns:NFe/ns:infNFe/ns:det', nsNfe):
            # DADOS DO ITEM
            cod = self.check_none(item.find('.ns:prod/ns:cProd', nsNfe))
            amount = self.check_none(item.find('.ns:prod/ns:qCom', nsNfe))
            description = self.check_none(item.find('.ns:prod/ns:xProd', nsNfe))
            unit_measurement = self.check_none(item.find(
                '.ns:prod/ns:UCom', nsNfe))
            production_value = self.check_none(item.find(
                '.ns:prod/ns:vProd', nsNfe))

            data = [nfe, serial, date_issue, key, cnpj_issuer, name_issuer,
                    value_nfe, item_note, cod, amount, description,
                    unit_measurement, production_value, date_import, user, date_output]
            
            notes.append(data)
            item_note += 1
        return notes
    
    def check_none(self, var):
        if var == None:
            return ''
        else:
            try: 
                return var.text.replace('.', ',')
            except:
                return var.text

    def format_cnpj(self, cnpj):
        try:
            cnpj = ''.join(filter(str.isdigit, cnpj))
            # Formata o CNPJ
            cnpj = '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
            return cnpj
        except:
            return ''

if __name__ == '__main__':
    xml = XmlReader('C:\\Users\\mateu\\OneDrive\\Documentos\\xml-files')
    all = xml.all_files()
    all_results = []  # Lista para armazenar todos os resultados
    for i in all:
        result = xml.nfe_data(i)
        all_results.extend(result)  # Adiciona os resultados à lista
    print(all_results)