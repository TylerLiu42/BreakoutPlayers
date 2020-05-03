CREATE TABLE StatcastData (
   lastName varchar(30),
   firstName varchar(30), 
   year int,
   xba double,
   xslg double,
   woba double,
   xwoba double,
   xobp double,
   xiso double,
   exitVelo double,
   launchAngle double,
   sweetSpotPercentage double,
   barrelRate double,

   PRIMARY KEY (lastName, firstName)
);