from django.template.loader import render_to_string, get_template
import os
import json
import django
from sys import path
from os import environ
from io import BytesIO
from xhtml2pdf import pisa
from datetime import datetime
from pathlib import Path as Dir

BASE_DIR = Dir(__file__).resolve().parent
path.append(str(BASE_DIR) + '/')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'testepdf.settings')
django.setup()


class ConverterPdf:

    @staticmethod
    def montar_template_judicial():
        dados = {
            'id': '01',
            'avatar': 'https://panteu.com.br/wp-content/uploads/2022/07/Logo_Icone.png',
            'razaoSocial': 'Corretora SA',
            'fantasia': 'Corretora Fantasia',
            'numeroRegistro': '00.152.135/0001-15',
            'susep': '13245',
            'codigoDemanda': '01',
            'dataSolicitacao': '01/01/1901',
            'tomadorPrimeiroNome': 'Tomador SA',
            'tomadorNumeroRegistro': '00.123.456/0001-45',
            'tomadorEndereco': 'Rua João Oliveira, 32 - Centro, Florianópolis - SC - CEP 88.111-050',
            'seguradoraPrimeiroNome': 'Seguradora SA',
            'seguradoraNumeroRegistro': '00.234.567/0001-12',
            'seguradoraSusep': '98765',
            'cocorretoraPrimeiroNome': 'REVER',
            'cocorretoraNumeroRegistro': 'REVER',
            'cocorretoraSusep': 'REVER',
            'tipoDemanda': 'Nova',
            'modalidade': 'Qualquer uma',
            'tipoProcesso': 'Aqui vai o tipo de processo',
            'tipoRecurso': 'Aqui vaio o recurso',
            'numeroProcesso': '1234567-12.1234.1.12.1234',
            'autoInfracao': '0%',
            'cda': 'Não',
            'tributoCobrado': 'R$ 123,00',
            'juizoPrimeiroNome': 'Tribunal de Floripa',
            'juizoNumeroRegistro': '00.456.321/0001-45',
            'juizoEndereco': 'Rua João Oliveira, 32 - Centro, Florianópolis - SC - CEP 88.111-050',
            'seguradoPrimeiroNome': 'Josue de Oliviera Neto',
            'seguradoNumeroRegistro': '000.156.123-45',
            'seguradoEndereco': 'Rua João Oliveira, 32 - Centro, Florianópolis - SC - CEP 88.111-050',
            'varaNome': 'Primeira vara de Floripa',
            'tempoVigencia': '5 anos',
            'percentual': '0,10%',
            'tipoIndice': 'IPCA',
            'valorGarantia': 'R$ 1.450,50',
            'valorAgravo': 'R$ 250,00',
            'importanciaSegurada': 'R$ 2.500,00',
            'classificacaoExito': 'Remota',
            'historicoProcesso': 'sdkjfsdkjbfksdjfkjsdbfkjdsbfjkdsfbsdkj',
            'defesaSustentada': 'sdlkfdlokfnblsdnflknfdldks',
            'responsavelCorretora': 'Daniel de Barros',
            'assinatura': 'https://panteu.com.br/wp-content/uploads/2022/07/TOP_Logo_Panteu.png',
        }
        dir_path = os.path.dirname(os.path.realpath(__file__))
        template = get_template(f'proposta_judicial.html')
        html = template.render(dados)
        filename = f"tmp/proposta_{dados['id']}_{str(datetime.now().strftime('%Y%m%d%H%M%S'))}.pdf"
        result = open(filename, 'wb')
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        result.close()
        if not pdf.err:
            return filename
        return False


if __name__ == '__main__':
    print('Iniciando a conversão')
    resposta = ConverterPdf.montar_template_judicial()
    print(f'Proposta {resposta} gerada!')
