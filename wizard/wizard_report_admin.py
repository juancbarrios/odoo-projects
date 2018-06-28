# -*- coding: utf-8 -*-

from odoo import api, fields, models


class WizardReportCompras(models.TransientModel):
    #Modelo representado en el Wizard
    _name = "impuestos.wizard.compras"
    _description = "Wizar Libro de Compras"

    #Indica el Mes al que se le hará el reporte
    periodo_compras_inicio = fields.Selection([('01','Enero'),
                                                ('02','Febrero'),
                                                ('03','Marzo'),
                                                ('04','Abril'),
                                                ('05','Mayo'),
                                                ('06','Junio'),
                                                ('07','Julio'),
                                                ('08','Agosto'),
                                                ('09','Septiembre'),
                                                ('10','Octubre'),
                                                ('11','Noviembre'),
                                                ('12','Diciembre'),
                                                ], string= 'Mes', required=True)

    #Indica el Mes al que se le hará el reporte
    periodo_compras_fin = fields.Selection([('2010','2010'),
                                                ('2011','2011'),
                                                ('2012','2012'),
                                                ('2013','2013'),
                                                ('2014','2014'),
                                                ('2015','2015'),
                                                ('2016','2016'),
                                                ('2017','2017'),
                                                ('2018','2018'),
                                                ('2019','2019'),
                                                ('2020','2020'),
                                                ], string= 'Año', required=True)

    excel_true_or_false1 = fields.Boolean('Descargar en Excel', default=False)

    @api.multi
    def action_report(self):
        #Método que llama la lógica para imprimir el reporte PDF del Libro de Compras
        excel = self.read(['excel_true_or_false1'])
        #Verificar si se quiere imprimir el reporte en formato EXCEL
        if excel == True:
            self.print_xls_report()
        else:
            data = {}
            res = self.read(['periodo_compras_inicio', 'periodo_compras_fin'])
            data['form'] = res[0]
            return self.env['report'].get_action([], 'impuestos1.test_template', data=data)

    @api.multi
    def print_xls_report(self):
        #Método que llama la lógica para imprimir el reporte EXCEL del Libro de Compras
        data = self.read('periodo_compras_inicio', 'periodo_compras_fin')[0]
        return {'type': 'ir.actions.report.xml',
                'report_name': 'impuestos1.test_template.xlsx',
                'datas': data
                }

    @api.multi
    def action_report_ventas(self):
        #Método que llama la lógica para imprimir el reporte PDF del Libro de Ventas
        data = {}
        res = self.read(['periodo_compras_inicio', 'periodo_compras_fin'])
        data['form'] = res[0]
        return self.env['report'].get_action([], 'impuestos1.test_template', data=data)

    @api.multi
    def print_xls_report_ventas(self, cr, uid, ids, context=None):
        #Método que llama la lógica para imprimir el reporte EXCEL del Libro de Ventas
        data = self.read(cr, uid, ids)[0]
        return {'type': 'ir.actions.report.xml',
                'report_name': 'impuestos1.test_template.xlsx',
                'datas': data
                }