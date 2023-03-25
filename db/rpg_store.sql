DROP TABLE IF EXISTS item_adv;
DROP TABLE IF EXISTS adventurers;
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    rarity VARCHAR(255),
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

INSERT INTO items (type, name, rarity, value) VALUES ('helmet', 'rusty helmet', NULL, NULL);
INSERT INTO items (type, name, rarity, value) VALUES ('sword', 'dirty dagger', NULL, NULL);
INSERT INTO adventurers (name) VALUES ('Thorfin');
INSERT INTO adventurers (name) VALUES ('Thorkell');
INSERT INTO adventurers (name) VALUES ('Thor');
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,1);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (2,1);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,2);

-- SELECT adventurers.* FROM adventurers INNER JOIN item_adv ON item_adv.adventurer_id = adventurers.id WHERE item_adv.loot_id = 1