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
INSERT INTO items (type, name, rarity,image, value) VALUES ('Sword', 'Sword of the Greats ','rare', 'sword.png', 1000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Axe', 'Oh Dear Axe', 'common', 'axe.png', 500);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Staff', 'Fly you Fools', 'ultra', 'staff.png', 5000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Helmet', 'Helm of Oblivion', 'ultra', 'helmet.png', 10000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Battle Axe', 'Thorkill', 'ultra', 'glassaxe.png', 8000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Scyche', 'Death''s Gambit', 'ultra', 'scythe.png', 8000);


-- INSERT INTO items (type, name, rarity, value)
-- VALUES (
--     'Helmet', 'The Helmet of Bravery', 
--     CASE floor(random() * 3) 
--         WHEN 0 THEN 'Common'
--         WHEN 1 THEN 'Rare'
--         ELSE 'Ultra'
--     END,
--     floor(random() * 10000) + 100
-- );


INSERT INTO adventurers (name) VALUES ('Store');
INSERT INTO adventurers (name) VALUES ('Thornforg');
INSERT INTO adventurers (name) VALUES ('Odinthin');
INSERT INTO adventurers (name) VALUES ('Alexandra');

INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,8);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,9);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,10);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,11);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,12);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,13);

-- SELECT adventurers.* FROM adventurers INNER JOIN item_adv ON item_adv.adventurer_id = adventurers.id WHERE item_adv.loot_id = 1
-- This query tells me the number of adventurers that own ID 1 in this case a rusty helmet.