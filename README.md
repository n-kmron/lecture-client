# ERPG5 - Project
## Project Information

**School:** École Supérieure d’Informatique  
**Program:** Bachelor en Informatique  
**Academic Year:** 2023 – 2024  

## ESI Lecture

**Gestion de librairies**

## Backend

The goal is to develop a book sales module with the following functionalities:

- Consult/add/delete/modify the list of books.
- View authors of books and rank them by the number of registered books.
- Allow users to like a book.

### Use of Web Service

To familiarize yourself with XML-RPC, write a Python script that:
- Asks the user for their login and password (or API key).
- Connects to your Odoo instance via XML-RPC.
- As long as the user wishes, searches for a book based on its name (title). Details of the implementation of these calls are available in the [documentation](https://www.odoo.com/documentation/14.0/fr/developer/api/external_api.html).

### Integration with Existing Modules

Transform our module to manage the stocks and sales of books. 

- Point of Sale: Manages sales in a store.
- Stock: Manages stocks and supplies.

## Frontend

A Django app as a client to allow users to interact with the Odoo esi-lecture module through an independent interface.

This project comprises two applications:
1. Configuration application for Odoo connection settings.
2. Book rating application.

## Authors
* Mamoun El Benmassoud
* Cameron Noupoue