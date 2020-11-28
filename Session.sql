BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Session" (
	"sessionID"	INTEGER NOT NULL,
	"startTime"	TEXT NOT NULL,
	"startMoney"	REAL NOT NULL,
	"addedMoney"	REAL NOT NULL,
	"stopTime"	TEXT NOT NULL,
	"stopMoney"	REAL NOT NULL,
	PRIMARY KEY("sessionID")
);
COMMIT;
