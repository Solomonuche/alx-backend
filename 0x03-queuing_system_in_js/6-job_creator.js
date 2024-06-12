const kue = require('kue')

const push_notification_code = kue.createQueue();
const data = {
    phoneNumber: 'string',
    message: 'string',
};
const stringifiedObj = JSON.stringify(data);

const job = push_notification_code.create(stringifiedObj);
job.on('enqueue', () => {
  console.log('Notification job created: ', job.id);
}).on('completed', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed')
});

job.save();
