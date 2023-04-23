--
-- File generated with SQLiteStudio v3.4.4 on Tue Apr 18 15:06:19 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: borrow
CREATE TABLE IF NOT EXISTS borrow (
    fk_product_id INTEGER        NOT NULL
                                 REFERENCES product (id),
    fk_user_id    INTEGER        NOT NULL
                                 REFERENCES user (id),
    quantity      INTEGER (0)    NOT NULL
                                 DEFAULT (1),
    returned      INTEGER (0, 1) NOT NULL
                                 DEFAULT (0),
    estimated_return_date INTEGER (0) NOT NULL DEFAULT (0),
    borrowed_at   INTEGER (0)    NOT NULL,
    created_at    INTEGER (0)    NOT NULL,
    PRIMARY KEY (fk_product_id, fk_user_id)
);

-- Table: manufacturer
CREATE TABLE IF NOT EXISTS manufacturer (id INTEGER PRIMARY KEY NOT NULL UNIQUE, name TEXT NOT NULL);

-- Table: ordered
CREATE TABLE IF NOT EXISTS ordered (
    fk_product_id INTEGER        REFERENCES product (id) 
                                 NOT NULL,
    fk_vendor_id  INTEGER        REFERENCES vendor (id),
    ordered       INTEGER (0, 1) DEFAULT (0) 
                                 NOT NULL,
    delivered     INTEGER (0, 1) NOT NULL
                                 DEFAULT (0),
    ordered_at    INTEGER (0)    NOT NULL,
    PRIMARY KEY (fk_product_id, fk_vendor_id)
);

-- Table: product
CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY UNIQUE NOT NULL, fk_manufacturer_id INTEGER REFERENCES manufacturer (id), fk_category_id INTEGER REFERENCES product_category (id), fk_vendor_id INTEGER REFERENCES vendor (id), model TEXT (0, 255) NOT NULL, quantity INTEGER (1) NOT NULL, price_when_bought INTEGER (1) NOT NULL, description TEXT, EAN TEXT, created_at INTEGER (0) NOT NULL, updated_at INTEGER (0) NOT NULL);

-- Table: product_category
CREATE TABLE IF NOT EXISTS product_category (id INTEGER PRIMARY KEY UNIQUE NOT NULL, name TEXT NOT NULL);

-- Table: vendor
CREATE TABLE IF NOT EXISTS vendor (id INTEGER PRIMARY KEY UNIQUE NOT NULL, name TEXT NOT NULL, website TEXT (0, 255));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

