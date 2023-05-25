BEGIN TRANSACTION;
CREATE TABLE images (uid text unique, owner text, name text, timestamp text);
INSERT INTO images VALUES('3afadaa2a3cbc1fffc6d8229ca1936b9760e1c56','TEST','made-with-flask.png','2017-07-08 10:49:19.018804');
INSERT INTO images VALUES('f739cc0a8bc1c3d17cc3dcc4fc5ff70b8266998b','TEST','flask-project.png','2017-07-08 10:57:45.759152');
INSERT INTO images VALUES('cbebc37b8e9ae56d722fc3966bb78da4ce48f9a6','ADMIN','flask.png','2017-07-08 11:37:04.630910');
COMMIT;
