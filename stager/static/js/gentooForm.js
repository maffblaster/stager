var driveLetters = ["a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"];
var firstDriveDigit = 0;
var secondDriveDigit = 0;

var nextLetter = function () {
    if (firstDriveDigit > 25) {
        console.log(driveLetters[secondDriveDigit]+driveLetters[secondDriveDigit]);
        firstDriveDigit++;
        secondDriveDigit++;
    } else {
        console.log(driveLetters[firstDriveDigit]);
        firstDriveDigit++;
    }
};

var gentooForm = [
 {
    "type":"section",
    "htmlClass": "row", 
    "items": [
        {
          "type":"section",
          "htmlClass": "col-xs-4", 
           "items": ["name"]
        },
       {
         "type":"section",
         "htmlClass": "col-xs-8", 
         "items": ["email"]
        }
    ]
  },
  {
    "key": "comment",
    "type": "textarea",
    "placeholder": "Make a comment"
  },
{
  "type": "submit",
  "title": "Save",
}]




/* var gentooForm = ["*",
{
  "type": "submit",
  "title": "Save",
}] */


/*
{
    "key": "form",
    "properties": {
        "key": "dev",
        "properties": {
            "key": "sds",
            "add": "Add New",
            "remove": "Remove",

            "items": [
                {
                    "key": "sd[].partition",
                    "type": "object",
                    "properties": {
                        "parttype": {
                            "type": "string",
                            "title": "Partition Type"
                        },
                        "mountpoint": {
                            "type": "string",
                            "title": "Mount Point"
                        },
                        "opts": {
                            "type": "string",
                            "title": "Options"
                        },
                        "dump": {
                            "type": "boolean",
                            "title": "Dump"
                        },
                        "pass": {
                            "type": "boolean",
                            "title": "Pass"
                        }
                    }
                },
                "sd[].label"
            ]
        }
    }
},
{
  "type": "submit",
  "title": "Save"
}
*/
