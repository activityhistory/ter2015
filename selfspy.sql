DROP TABLE IF EXISTS "bookmark";
CREATE TABLE bookmark (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	time VARCHAR, 
	PRIMARY KEY (id)
);
DROP TABLE IF EXISTS "click";
CREATE TABLE click (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	button INTEGER NOT NULL, 
	press BOOLEAN NOT NULL, 
	x INTEGER NOT NULL, 
	y INTEGER NOT NULL, 
	nrmoves INTEGER NOT NULL, 
	path BLOB, 
	timings BLOB, 
	process_id INTEGER NOT NULL, 
	window_id INTEGER NOT NULL, 
	geometry_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (press IN (0, 1)), 
	FOREIGN KEY(process_id) REFERENCES process (id), 
	FOREIGN KEY(window_id) REFERENCES window (id), 
	FOREIGN KEY(geometry_id) REFERENCES geometry (id)
);

DROP TABLE IF EXISTS "debrief";
CREATE TABLE debrief (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	experience_id INTEGER NOT NULL, 
	doing_report VARCHAR, 
	audio_file VARCHAR, 
	memory_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(experience_id) REFERENCES experience (id)
);
DROP TABLE IF EXISTS "experience";
CREATE TABLE experience (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	message VARCHAR, 
	screenshot VARCHAR, 
	user_initiated BOOLEAN, 
	ignored BOOLEAN, 
	after_break BOOLEAN, 
	PRIMARY KEY (id), 
	CHECK (user_initiated IN (0, 1)), 
	CHECK (ignored IN (0, 1)), 
	CHECK (after_break IN (0, 1))
);

DROP TABLE IF EXISTS "geometry";
CREATE TABLE geometry (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	xpos INTEGER NOT NULL, 
	ypos INTEGER NOT NULL, 
	width INTEGER NOT NULL, 
	height INTEGER NOT NULL, 
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS "keys";
CREATE TABLE keys (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	text BLOB NOT NULL, 
	started VARCHAR NOT NULL, 
	process_id INTEGER NOT NULL, 
	window_id INTEGER NOT NULL, 
	geometry_id INTEGER NOT NULL, 
	nrkeys INTEGER, 
	keys BLOB, 
	timings BLOB, 
	PRIMARY KEY (id), 
	FOREIGN KEY(process_id) REFERENCES process (id), 
	FOREIGN KEY(window_id) REFERENCES window (id), 
	FOREIGN KEY(geometry_id) REFERENCES geometry (id)
);

DROP TABLE IF EXISTS "location";
CREATE TABLE location (
    "id" INTEGER NOT NULL,
    "created_at" VARCHAR,
    "lat" INTEGER NOT NULL,
    "lon" INTEGER NOT NULL,
    "time" BLOB
);

DROP TABLE IF EXISTS "privacy_keywords";
CREATE TABLE "privacy_keywords" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "keyword" TEXT NOT NULL,
    "isApp" BLOB DEFAULT (0),
    "isprivate" BLOB DEFAULT (1)
);

DROP TABLE IF EXISTS "privacy_locations";
CREATE TABLE privacy_locations (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "longitude" REAL,
    "latitude" REAL,
    "isprivate" BLOB DEFAULT (1),
    "address" TEXT
);

DROP TABLE IF EXISTS "privacy_time";
CREATE TABLE "privacy_time" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "weekEnd" BLOB,
    "week" BLOB,
    "fromHour" TEXT,
    "toHour" TEXT
);
INSERT INTO "privacy_time" VALUES(2,0,1,'08:00','20:00');

DROP TABLE IF EXISTS "process";
CREATE TABLE process (
    "id" INTEGER NOT NULL,
    "created_at" VARCHAR,
    "name" VARCHAR
, "isprivate" BLOB  NOT NULL  DEFAULT (0));

DROP TABLE IF EXISTS "processevent";
CREATE TABLE processevent (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	process_id INTEGER NOT NULL, 
	event_type VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(process_id) REFERENCES process (id)
);

DROP TABLE IF EXISTS "recordingevent";
CREATE TABLE recordingevent (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	event_type VARCHAR, 
	time VARCHAR, 
	PRIMARY KEY (id)
);

DROP TABLE IF EXISTS "window";
CREATE TABLE window (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	title VARCHAR, 
	browser_url VARCHAR, 
	process_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(process_id) REFERENCES process (id)
);

DROP TABLE IF EXISTS "windowevent";
CREATE TABLE windowevent (
	id INTEGER NOT NULL, 
	created_at VARCHAR, 
	window_id INTEGER NOT NULL, 
	event_type VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(window_id) REFERENCES window (id)
);