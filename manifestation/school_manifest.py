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

        # Sequence
        "sequence/person.xml",
        "sequence/employee.xml",
        "sequence/product.xml",
        "sequence/stores.xml",
        "sequence/asserts.xml",
        "sequence/purchase.xml",
        "sequence/order.xml",
        "sequence/invoice.xml",
        "sequence/school.xml",

        # Base
        "views/base/users.xml",
        "views/base/company.xml",

        # Register
        "views/patient/patient.xml",
        "views/hr/employee.xml",
        "views/academic/student.xml",
        "views/school/student.xml",
        "views/person/person.xml",

        # Contact
        "views/contact/contact.xml",
        "views/contact/doctor.xml",
        "views/contact/nurse.xml",
        "views/contact/staff.xml",
        "views/contact/driver.xml",
        "views/contact/patient.xml",
        "views/contact/supplier.xml",
        "views/contact/service.xml",
        "views/contact/student.xml",
        "views/contact/teacher.xml",

        # Hospital
        "views/hospital/admission.xml",
        "views/hospital/discharge.xml",
        "views/hospital/admission_reason.xml",
        "views/hospital/discharge_reason.xml",
        "views/hospital/ambulance.xml",

        # Doctor
        "views/doctor/doctor_availability.xml",
        "views/doctor/doctor_timing.xml",

        # Notes
        "views/hospital/notes.xml",
        "views/hospital/reminder.xml",

        # Ward
        "views/ward/ward.xml",
        "views/ward/bed.xml",
        "views/ward/patient_shifting.xml",
        "views/ward/bed_status.xml",

        # Appointment
        "views/appointment/appointment.xml",
        "views/appointment/my_appointment.xml",
        "views/appointment/opt.xml",
        "views/appointment/ot.xml",
        "views/appointment/meeting.xml",
        "views/appointment/appointment_reason.xml",

        # Operation
        "views/operation/operation_theater.xml",
        "views/operation/ot_status.xml",
        "views/operation/operation_list.xml",
        "views/operation/operation.xml",

        # Account
        "views/account/account.xml",
        "views/account/period.xml",
        "views/account/journal.xml",
        "views/account/journal_item.xml",
        "views/account/journal_type.xml",
        "views/account/reconcile.xml",
        "views/configuration/account_config.xml",

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

        # Recruitment
        "views/recruitment/resume_bank.xml",
        "views/recruitment/vacancy_position.xml",
        "views/recruitment/appointment_order.xml",

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
        "views/payroll/salary_rule_code.xml",
        "views/payroll/salary_structure.xml",

        # HR Actions
        "views/hr_action/hiring.xml",
        "views/hr_action/promotion.xml",
        "views/hr_action/complaint.xml",
        "views/hr_action/resignation.xml",

        # Notice Board
        "views/notice_board/notice.xml",
        "views/notice_board/event.xml",

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
        "views/stock/material_transact_in.xml",
        "views/stock/material_transact_out.xml",
        "views/configuration/store_config.xml",

        # Asserts
        "views/asserts/asserts_capitalisation.xml",
        "views/asserts/asserts.xml",
        "views/asserts/asserts_maintenance.xml",
        "views/asserts/asserts_reminder.xml",

        # Purchase
        "views/purchase/indent.xml",

        # Order
        "views/order/purchase_order.xml",
        "views/order/purchase_return.xml",
        "views/order/sales_order.xml",
        "views/order/sales_return.xml",

        # Invoice
        "views/invoice/invoice.xml",
        "views/invoice/purchase_invoice.xml",
        "views/invoice/purchase_return_invoice.xml",
        "views/invoice/sales_invoice.xml",
        "views/invoice/sales_return_invoice.xml",

        # School
        "views/school/year.xml",
        "views/school/standard.xml",
        "views/school/section.xml",
        "views/school/subject.xml",
        "views/school/complaint.xml",
        "views/school/disciplinary_action.xml",
        "views/school/co_curricular.xml",
        "views/school/extra_curricular.xml",
        "views/school/admission.xml",
        "views/school/transfer.xml",
        "views/school/student.xml",

        # Academic
        "views/academic/academic.xml",
        "views/academic/standard.xml",
        "views/academic/section.xml",
        "views/academic/student.xml",

        # Menu
        "views/menu/school.xml",
        "views/menu/school_sub_menu.xml",
        "views/menu/hospital.xml",
        "views/menu/hospital_sub_menu.xml",

    ],
    "demo": [

    ],
    "qweb": [

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}