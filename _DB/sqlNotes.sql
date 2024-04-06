
CREATE TABLE hero (id INTEGER NOT NULL, name VARCHAR NOT NULL,)
CREATE INDEX ix_hero_name ON hero (name)

SELECT name FROM hero WHERE name = 'Deadpond'
INSERT INTO hero (id, name) VALUES (1, 'Deadpond')
UPDATE hero SET name = 'Deadpond' WHERE name = 'Deadpond'

DELETE FROM hero WHERE name = 'Deadpond'

TRUNCATE TABLE hero
DROP TABLE IF EXISTS hero