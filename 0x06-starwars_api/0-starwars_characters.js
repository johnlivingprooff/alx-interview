#!/usr/bin/node
const request = require('request');

const number = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${number}/`;
const promises = [];

function findCharacter (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (error) reject(error);
      resolve(JSON.parse(body).name);
    });
  });
}

request(url, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body);
  data.characters.forEach(function (chrtr) {
    promises.push(findCharacter(chrtr));
  });
  Promise.all(promises).then((names) => {
    names.forEach((name) => console.log(name));
  });
});
