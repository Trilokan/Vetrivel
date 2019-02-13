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

        # Sequence
        "sequence/person.xml",
        "sequence/product.xml",
        "sequence/store.xml",

        # Hr
        "views/hr/employee.xml",
        "views/hr/category.xml",
        "views/hr/department.xml",
        "views/hr/designation.xml",
        "views/hr/experience.xml",
        "views/hr/identities.xml",
        "views/hr/address.xml",
        "views/hr/qualification.xml",

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
        # "views/store/stock_adjustment.xml",
        # "views/store/store_request.xml",
        # "views/store/store_issue.xml",
        # "views/store/store_return.xml",
        # "views/store/store_accept.xml",
        # "views/store/arc_move.xml",
        "views/configuration/store_config.xml",

        # Asserts

        # Menu
        "views/menu/main_menu.xml",
        "views/menu/hr.xml",
        "views/menu/inventory.xml",
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