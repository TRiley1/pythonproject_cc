DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS adventurers;
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    rarity VARCHAR(255),
    image VARCHAR(255),
    value INT
);

CREATE TABLE adventurers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    wallet INT
);

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    adventurer_id INT NOT NULL REFERENCES adventurers(id) ON DELETE CASCADE,
    item_id INT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    review TEXT
);

INSERT INTO items (type, name, rarity,image, value) VALUES ('helmet', 'rusty helmet', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('sword', 'dirty dagger', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('tunic', 'worn tunic', NULL, 'axe.png',NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('lamp', 'dusty lamp', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('helmet', 'cracked helmet', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('belt', 'tired belt', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('axe', 'brittle axe', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Sword', 'Sword of the Greats ','rare', 'sword.png', 1000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Axe', 'Oh Dear Axe', 'common', 'axe.png', 500);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Staff', 'Fly you Fools', 'ultra', 'staff.png', 5000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Helmet', 'Helm of Oblivion', 'ultra', 'helmet.png', 10000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Battle Axe', 'Thorkill', 'ultra', 'glassaxe.png', 8000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Scyche', 'Death''s Gambit', 'ultra', 'scythe.png', 8000);




INSERT INTO adventurers (name, wallet) VALUES ('Thornforg', 10000);
INSERT INTO adventurers (name, wallet) VALUES ('Odinthin', 20000);
INSERT INTO adventurers (name, wallet) VALUES ('Alexandra', 40000);


