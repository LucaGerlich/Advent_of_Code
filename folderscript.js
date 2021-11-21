var fs = require('fs');

for (let index = 0; index < 25; index++) {
    if (!fs.existsSync("Day_" + index)){
        console.log("Day_" + index);
        fs.mkdirSync("Day_" + index);
    }
}