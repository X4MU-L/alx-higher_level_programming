#!/usr/bin/node
const request = require('request');

/**
 * Asynchronously fetches a charcter with {@link url}
 * @param url
 * @returns a promise that either resolves or rejects on error
 */
const getCharacter = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

/**
 * Asynchronously fetches all characters with array of urls for
 * characters and prints each name
 * @param charactersUrl
 * @returns void
 */
const getCharacters = async (charactersUrl) => {
  for (const characterUrl of charactersUrl) {
    const character = await getCharacter(characterUrl);
    console.log(character.name);
  }
};

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (!err) {
    const charactersUrl = JSON.parse(body).characters;
    getCharacters(charactersUrl);
  }
});
