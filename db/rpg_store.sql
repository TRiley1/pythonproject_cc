DROP TABLE IF EXISTS item_adv;
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
    name VARCHAR(255)
);

CREATE TABLE item_adv (
    id SERIAL PRIMARY KEY,
    adventurer_id INT NOT NULL REFERENCES adventurers(id) ON DELETE CASCADE,
    loot_id INT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    review TEXT
);

INSERT INTO items (type, name, rarity,image, value) VALUES ('helmet', 'rusty helmet', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('sword', 'dirty dagger', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('tunic', 'worn tunic', NULL, 'axe.png',NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('lamp', 'dusty lamp', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('helmet', 'cracked helmet', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('belt', 'tired belt', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('axe', 'brittle axe', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('shorts', 'sad shorts', NULL, 'axe.png', NULL);
INSERT INTO adventurers (name) VALUES ('Thorfin');
INSERT INTO adventurers (name) VALUES ('Thorkell');
INSERT INTO adventurers (name) VALUES ('Thor');
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,1);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (2,1);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,2);

-- SELECT adventurers.* FROM adventurers INNER JOIN item_adv ON item_adv.adventurer_id = adventurers.id WHERE item_adv.loot_id = 1
-- This query tells me the number of adventurers that own ID 1 in this case a rusty helmet.