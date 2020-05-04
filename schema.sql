CREATE TABLE StatcastData (
   lastName varchar(30),
   firstName varchar(30), 
   playerID int,
   attempts int,
   avgHitAngle double,
   sweetSpotPercentage double,
   maxHitSpeed double,
   avgHitSpeed double,
   fbld double,
   gb double,
   maxDistance int,
   avgDistance int,
   avgHRDistance int default 0,
   ev95plus int,
   ev95percent double,
   barrels int,
   barrelPercentage double,
   barrelPerPA double,

   PRIMARY KEY (playerID)
);

CREATE TABLE StatcastDataExpectedHitting (
   lastName varchar(30),
   firstName varchar(30),
   playerID int,
   year int,
   pa int,
   bip int,
   ba double,
   xBA double,
   xBADiff double,
   slg double,
   xslg double,
   xslgDiff double,
   woba double,
   xwoba double,
   xwobaDiff double,

   PRIMARY KEY (playerID)
);