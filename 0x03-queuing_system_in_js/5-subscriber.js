import { createClient } from "redis";

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('err', (err) => {
    console.log('Redis client not connected to the server: ', err)
  });
client.connect();

client.subscribe('holberton school channel', (message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
  console.log(message);
})