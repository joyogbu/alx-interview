#!/usr/bin/node
const arg = process.argv;
const myId = arg[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + myId;
const request = require('request');
request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const myData = JSON.parse(body).characters;
    myData.forEach(async (character) => {
      await request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        }
	//});
        console.log(JSON.parse(body).name);
      });
    });
  }
});
