const fastify = require('fastify')({ logger: true })
const https = require("https")

fastify.get('/', (request, reply) => {
    let data;
    https.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2", resp => {
        resp.on("data", chunk => data += chunk);
        resp.on("end", () => reply.code(200).send(data));
        resp.on("error", (err) => console.log(err));
    });
})

const start = async () => {
    try {
        await fastify.listen(3000)
        fastify.log.info(`server listening on ${fastify.server.address().port}`)
    } catch (err) {
        fastify.log.error(err)
        process.exit(1)
    }
}
start()