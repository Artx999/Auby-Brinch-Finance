BEGIN TRANSACTION;
CREATE TABLE notes (owner text, timestamp text, note text, note_id text);
INSERT INTO notes VALUES('TEST','2017-07-03 22:22:03.301170','This is a note of user TEST.','1e3acedb82a9d9bdbd75723a3ea215059159fc21');
INSERT INTO notes VALUES('ADMIN','2017-07-03 22:22:18.457563','This is a note of user ADMIN.','1f90a08ac4e231db43a20905adf448dd42482230');
COMMIT;
