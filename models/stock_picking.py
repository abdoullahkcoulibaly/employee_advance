# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = "stock.picking"

    is_employee_advance = fields.Boolean("Avance employé")
    employee_id = fields.Many2one('hr.employee', 'Employé')

    def button_validate(self):
        res = super().button_validate()
        if self.is_employee_advance:
            total_amount = sum(move.product_uom_qty * move.standard_price for move in self.move_ids_without_package)
            salary_attachment_vals = {
                'employee_ids': [(4, self.employee_id.id)],
                'description': self.name,
                'deduction_type_id': self._get_default_deduction_type_id(),
                'monthly_amount': total_amount,
                'total_amount': total_amount,
            }
            self.env['hr.salary.attachment'].create(salary_attachment_vals)
        return res

    def _get_default_deduction_type_id(self):
        default_type = self.env['hr.salary.attachment.type'].search([], limit=1)
        return default_type.id if default_type else False
