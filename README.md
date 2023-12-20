# ERPG5 - Project

## ESI Lecture

**Gestion de librairies**

## Utilisation du client Django

Avant de lancer le serveur, il faut s'assurer que Docker et les images Odoo tournent

Une fois le serveur lancé, on arrive sur une page pour se connecter au serveur Odoo. Si l'authentification est réussie, alors on est redirigé sur une page pour rechercher des livres par leur nom. Si des livres sont trouvés, une page affiche les résultats et on peut liker le livre que l'on veut.

WARNING : le like fonctionne dans un seul sens sur le client Django (fonctionne correctement via Odoo). Si on unlike un livre, cela ne sera pas pris en compte par Django malheuresement

## Pistes d'amélioration

Notre application est fonctionnelle et comporte tout ce qui a été demandé mais nous avons pu trouver des pistes d'améliorations que nous n'avons pas pu combler par manque de temps au vu des nombreux cours que nous avons dû remettre récemment

* Odoo : gestion des erreurs, afficher des pop up, ... et gestion de la cohérence pour certaines choses
* Django : la sécurité, routes accessibles, peu de vérifications, ...

## Backend

The goal is to develop a book sales module with the following functionalities:

- Consult/add/delete/modify the list of books.
- View authors of books and rank them by the number of registered books.
- Allow users to like a book.

### Use of Web Service

A RPC and python script is available at `script_rpc/script.py` to search books.

Details of the implementation of these calls are available in the [documentation](https://www.odoo.com/documentation/14.0/fr/developer/api/external_api.html).

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
> Mamoun El Benmassoud <br>
> Cameron Noupoue

## Credits 
**School:** École Supérieure d’Informatique  
**Academic Year:** 2023 – 2024
