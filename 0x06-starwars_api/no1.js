#!/usr/bin/node
const arg = process.argv;
const myId = arg[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + myId;
const request = require('request');
request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    myArray = []
    const myData = await JSON.parse(body).characters;
    myData.forEach(async (character) => {
      const myArr = []
      myArray = await request(character, async function (error, response, body) {
        if (error) {
          console.log(error);
        }
	/*myArr.push(JSON.parse(body).name)*/
	await Promise.all(myArray)
        console.log(JSON.parse(body).name);
	/*await Promise.all(myData)*/
	/*console.log(res)*/
      });
    });
  }
});
