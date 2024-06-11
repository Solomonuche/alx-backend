import { createClient, print } from 'redis';

const client = createClient();
client.connect()
client.on('connect', () => {
    client.hSet('HolbertonSchools',  'Portland', 50, print);
    client.hSet('HolbertonSchools',  'Seattle', 80, print);
    client.hSet('HolbertonSchools',  'New York', 20, print);
    client.hSet('HolbertonSchools',  'Bogota', 20, print);
    client.hSet('HolbertonSchools',  'Cali', 40, print);
    client.hSet('HolbertonSchools',  'Paris', 2, print);
    client.hGetAll('HolbertonSchools', (err, value) => {
    console.log(value);
    });
})
