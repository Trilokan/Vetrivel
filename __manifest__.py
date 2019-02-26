# -*- coding: utf-8 -GPK*-

{
    "name": "VETRIVEL",
    "version": "1.0",
    "author": "La Mars",
    "website": "http://",
    "category": "VETRIVEL",
    "sequence": 1,
    "summary": "Hospital Management System",
    "description": """

    Hospital Management System

    Patient Management
    Employee Management
    Purchase Management
    Pharmacy Management
    Assert Management
    Accounts Management

    """,
    "depends": ["base", "mail"],
    "data": [
        "views/assert_backend.xml",

        # Data
        "data/vendor_type.xml",
        "data/employee_type.xml",

        # Sequence
        "sequence/person.xml",
        "sequence/employee.xml",
        "sequence/product.xml",
        "sequence/store.xml",
        "sequence/purchase.xml",

        # Account
        "views/account/account.xml",
        "views/account/period.xml",
        "views/account/journal.xml",
        "views/account/journal_item.xml",
        "views/account/journal_type.xml",
        "views/account/reconcile.xml",

        # Base
        "views/base/users.xml",
        "views/base/company.xml",

        # Person
        "views/person/person.xml",
        "views/person/vendor_type.xml",

        # Contact
        "views/contact/doctor.xml",
        "views/contact/nurse.xml",
        "views/contact/staff.xml",
        "views/contact/driver.xml",
        "views/contact/patient.xml",
        "views/contact/supplier.xml",
        "views/contact/service.xml",
        "views/contact/others.xml",

        # Hr
        "views/hr/employee.xml",
        "views/hr/employee_type.xml",
        "views/hr/category.xml",
        "views/hr/department.xml",
        "views/hr/designation.xml",
        "views/hr/experience.xml",
        "views/hr/identities.xml",
        "views/hr/address.xml",
        "views/hr/qualification.xml",

        # Time management
        "views/time/shift.xml",
        "views/time/week_schedule.xml",
        "views/time/month_attendance.xml",
        "views/time/month_attendance_wiz.xml",
        "views/time/daily_attendance.xml",
        "views/time/shift_change.xml",
        "views/time/holiday_change.xml",
        "views/time/add_employee.xml",
        "views/time/time_sheet.xml",
        "views/time/time_sheet_application.xml",
        "views/time/work_sheet.xml",
        "views/configuration/time_config.xml",

        # Leave Management
        "views/leave/leave_application.xml",
        "views/leave/comp_off.xml",
        "views/leave/permission.xml",
        "views/leave/on_duty.xml",
        "views/leave/leave_level.xml",
        "views/leave/leave_type.xml",
        "views/leave/leave_availability.xml",
        "views/configuration/leave_config.xml",

        # Payroll
        "views/payroll/hr_pay_update_wiz.xml",
        "views/payroll/hr_pay.xml",
        "views/payroll/payroll_generation.xml",
        "views/payroll/payslip.xml",
        "views/payroll/salary_rule.xml",
        "views/payroll/salary_rule_slab.xml",
        "views/payroll/salary_structure.xml",

        # Product
        "views/product/product.xml",
        "views/product/product_group.xml",
        "views/product/sub_group.xml",
        "views/product/uom.xml",
        "views/product/tax.xml",
        "views/product/category.xml",

        # Store
        "views/stock/location.xml",
        "views/stock/warehouse.xml",
        "views/stock/stock_adjustment.xml",
        "views/stock/store_request.xml",
        "views/stock/store_issue.xml",
        "views/stock/store_return.xml",
        "views/stock/store_accept.xml",
        "views/stock/arc_move.xml",
        "views/stock/material_in.xml",
        "views/configuration/store_config.xml",

        # Asserts

        # Purchase
        "views/purchase/indent.xml",
        "views/purchase/direct_purchase.xml",

        # Invoice
        "views/invoice/invoice.xml",

        # Hospital
        "views/hospital/ward.xml",
        "views/hospital/bed.xml",
        "views/hospital/notes.xml",
        "views/hospital/reminder.xml",
        "views/hospital/doctor_timing.xml",

        # Appointment
        "views/appointment/opt.xml",

        # Menu
        "views/menu/main_menu.xml",
        "views/menu/account.xml",
        "views/menu/contact.xml",
        "views/menu/hr.xml",
        "views/menu/inventory.xml",
        "views/menu/purchase.xml",
        "views/menu/hospital.xml",
        # "views/menu/asserts.xml",


    ],
    "demo": [

    ],
    "qweb": [

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}