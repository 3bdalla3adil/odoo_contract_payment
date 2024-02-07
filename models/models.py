from odoo import api, fields, models, _


class ContractPayment(models.Model):
    _name = "contract.payment"
#     _inherit_id = "account.move"
    _order = "partner_id,payment_status"
    _description  = "Contract Payment"

#     transaction_ids = fields.Char('Sales')

    contract_date = fields.Date(string='Contract Date', )
#     company_name  = fields.Char(string='Company Name' , )
    partner_id    = fields.Many2one('res.partner',string='Company Name' , )
    due_date      = fields.Date(string='Due Date'     , )
    payment_rate  = fields.Float(string='Payment Rate', )
    payment_status= fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ], string='Payment Status',default='unpaid')
    paid_price   = fields.Float(string='Paid Price'  , compute="_compute_paid_price")
    remain_price = fields.Float(string='Remain Price', compute="_compute_remain_price")
    total_price  = fields.Float(string='Total Price')
    payment_date = fields.Date (string='Payment Date')


    @api.onchange("total_price","paid_price")
    def _compute_remain_price(self):
        # for all record in object
        for record in self:

            # Calculate Paid Price # Calculate Remaining Price

            record.remain_price = record.total_price - record.paid_price


    @api.onchange("total_price","paid_price")
    def _compute_remain_price(self):
        # for all record in object
        for record in self:

            # Calculate Paid Price # Calculate Remaining Price

            record.remain_price = record.total_price - record.paid_price

    @api.onchange("total_price","payment_rate")
    def _compute_paid_price(self):
        # for all record in object
        for record in self:

            # Calculate Paid Price # Calculate Remaining Price
            if record.payment_rate > 0 :
                record.paid_price = (record.total_price * record.payment_rate) / 100
