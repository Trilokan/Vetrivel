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

        # Menu
        "views/menu/main_menu.xml",


    ],
    "demo": [

    ],
    "qweb": [

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}