# ESI Lecture

ESI Lecture is a webapp designed and build with Odoo and Django to manage a book library

## Prerequisites

* Python3
* Docker and an image of odoo and postgresql on the port 8069 and the name of the db has to be `dev01`
* Load data must also be loaded
  
## Launch

* Install our Odoo module in your instance
* * execute `make` at the root of the repository

## Backend

A backend is developed with Odoo 14 and serves to
- Consult/add/delete/modify the list of books.
- View authors of books and rank them by the number of registered books.
- Allow users to like a book.
- Buy books
- Manage books' stock


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
* Cameron Noupoue
* Mamoun El Benmassoud

## Credits 
**School:** École Supérieure d’Informatique  
**Academic Year:** 2023 – 2024
