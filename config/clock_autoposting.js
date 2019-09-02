var CronJob = require('cron').CronJob;
var bot = require('child_process').exec;

var job = new CronJob({
  cronTime: "0 */8 * * *", // every 8 hours
  onTick: bot('services/autoposting/tweet_posting.rb'),
  start: true,
  timeZone: "America/Los_Angeles"
});

job.start();