#!/usr/bin/node
const arg = process.argv;
const myId = arg[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + myId;
const request = require('request');
request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const myData = JSON.parse(body).characters;
    // myData.forEach(async (character) => {
    for (const character of myData) {
      const p = new Promise(async (resolve, reject) => {
	     try {
	      await request(character, function (error, response, body) {
            if (error) {
              reject(error);
            }
            resolve(JSON.parse(body));
	    });
        // console.log(JSON.parse(body).name);
        }
	     // p.then(response => console.log(respnse))

	     catch (error) {
	     console.log(error);
        }
      });
	     p.then(response => console.log(response));
    }
  }
});
